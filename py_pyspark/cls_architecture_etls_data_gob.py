"""
@author: ronald.barberi

crate_at: 2025-07-11 09:20
update_at: 2025-10-21 10:04

@editor: ronald.barberi
"""

# Imported libraries

import time
import uuid
import pandas as pd
from pydoop import hdfs
from pyspark.sql import Row
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import DateType
from datetime import datetime, timedelta
from py4j.java_gateway import java_import
from pyspark.sql.functions import col, to_date, udf, sha2


# Create class

class ArchitectureETLs:
    
    @staticmethod
    def start_sesion_spark(name_sesion: str):

        conf = SparkConf()
        conf.set('spark.sql.orc.write.batch.size', '100_000')
        conf.set('spark.sql.shuffle.partitions', '100')

        spark = SparkSession.builder \
            .appName(name_sesion) \
            .config(conf=conf) \
            .master('yarn') \
            .enableHiveSupport() \
            .getOrCreate()

        return spark
        

    @staticmethod
    def insert_to_view_spark(
        spark_sesion,
        job_name: str,
        environment: str,
        df_gob,
        schema: str,
        table: str,
        path_file: str,
        _overwrite=False,
        _partitions=False,
        cols_partition=None,
        clear_file=False
    ):

        df_gob.createOrReplaceTempView('tb_tmp_view_insert_etl')

        table_exists = spark_sesion.sql(f"SHOW TABLES IN {schema}").filter(f"tableName = '{table}'").count() > 0
        if not table_exists:
            print(f'[INFO] table {schema}.{table} does not exist. Creating...')

            writer = df_gob.write.mode('overwrite')

            if _partitions:
                if not cols_partition:
                    raise ValueError("[ERROR] you must provide 'cols_partition' if _partitions=True")
                if isinstance(cols_partition, str):
                    cols_partition = [cols_partition]
                writer = writer.partitionBy(cols_partition)

            writer.saveAsTable(f"{schema}.{table}")
            print(f'[OK] table {schema}.{table} created successfully')

        if _overwrite is True:
            type_insert = 'OVERWRITE'
        elif _overwrite is False:
            type_insert = ''
        else:
            print(f'[ERROR] value _overwrite incorrect: {_overwrite}')

        if _partitions is True:
            if not cols_partition:
                raise ValueError("[ERROR] you must provide 'cols_partition' if _partitions=True")
            
            if isinstance(cols_partition, str):
                cols_partition = [cols_partition]
            partitions_qry = f"PARTITION ({', '.join(cols_partition)})"

        elif _partitions is False:
            partitions_qry = ''
        else:
            print(f'[ERROR] value _partitions incorrect: {_partitions}')

        spark_sesion.sql('SET hive.exec.dynamic.partition=true')
        spark_sesion.sql('SET hive.exec.dynamic.partition.mode=nonstrict')

        sql_query_etl = f"""
        INSERT {type_insert} TABLE {schema}.{table} {partitions_qry}
        SELECT *
        FROM tb_tmp_view_insert_etl
        """

        print('[INFO] SQL INSERT QUERY:\n', sql_query_etl.strip())
        try:
            
            spark_sesion.sql(sql_query_etl)
            print('[OK] succes insert')

            try:
                records_read = df_gob.count()
                cols_read = len(df_gob.columns)
                ArchitectureETLs.save_logs_intakes(spark_sesion, job_name, environment, cols_read, records_read, schema, table, path_file, 'success', '')

                print('[OK] save log intake success')
            except Exception as e:
                print(f'[ERROR] save log intake failed: {e}')

            if clear_file is True:
                ArchitectureETLs.delte_file_hdfs(spark_sesion, path_file)

        except Exception as e:
            print(f'[ERROR] failed insert: {e}')
            records_read = df_gob.count()
            cols_read = len(df_gob.columns)
            ArchitectureETLs.save_logs_intakes(spark_sesion, job_name, environment, cols_read, records_read, schema, table, path_file, 'failed', e)


    @staticmethod
    def validate_input_file(
        spark_sesion,
        path_file: list,
        range_days: int,
        wait_time=None,
        max_retries=None,
        _sep=None,
        col_incremental=None
    ):
    
        today = datetime.today().date()
        day_min = today - timedelta(days=range_days)

        if isinstance(path_file, str):
            path_file = [path_file]

        for path in path_file:
            try:
                java_import(spark_sesion._jvm, 'org.apache.hadoop.fs.FileSystem')
                java_import(spark_sesion._jvm, 'org.apache.hadoop.fs.Path')
                fs = spark_sesion._jvm.FileSystem.get(spark_sesion._jsc.hadoopConfiguration())
                path_hdp = spark_sesion._jvm.Path(path)

                attempt = 0
                max_tries = max_retries if max_retries is not None else 1
                file_updated = False

                while attempt < max_tries:
                    attempt += 1
                    print(f'[INFO] attempt {attempt}/{max_tries}...')

                    if fs.exists(path_hdp):
                        last_mod_date = datetime.fromtimestamp(
                            fs.getFileStatus(path_hdp).getModificationTime() / 1_000
                        ).date()

                        if last_mod_date >= day_min:
                            print(f'[INFO] file {path_hdp} is updated (last modified: {last_mod_date})')

                            if col_incremental:
                                date_max_col_inct = ArchitectureETLs.get_max_date_from_column(
                                    spark_sesion, path, _sep, col_incremental
                                )

                                if date_max_col_inct and date_max_col_inct >= day_min:
                                    print(f'[INFO] column "{col_incremental}" is up to date (max date: {date_max_col_inct})')
                                    file_updated = True
                                    break
                                else:
                                    print(f'[INFO] column "{col_incremental}" outdated or null (max date: {date_max_col_inct})')
                                    file_updated = False
                            else:
                                file_updated = True
                                break
                        else:
                            print(f'[ERROR] file exists but not recently updated (last modified: {last_mod_date})')
                    else:
                        print(f'[ERROR] file {path_hdp} does not exist')

                    if wait_time and attempt < max_tries:
                        time.sleep(wait_time)

                if not file_updated:
                    raise FileNotFoundError(
                        f'[ERROR] file no update range days: ({range_days}) - tries: {max_tries} - file: {path}'
                    )

            except Exception as err:
                print('[ERROR] error in validate_input_file:', err)
                raise


    @staticmethod
    def get_max_date_from_column(spark_sesion, path_file: list, _sep=',', col_incremental=None):
        df_val_inct = (
            spark_sesion
                .read
                .option('header', True)
                .option('delimiter', _sep)
                .csv(path_file)
                .select(col_incremental)
        )

        if not isinstance(df_val_inct.schema[col_incremental].dataType, DateType):
            df_val_inct = df_val_inct.withColumn('date_incremental', to_date(col(col_incremental), 'yyyy-MM-dd'))
            col_to_check = 'date_incremental'
        else:
            col_to_check = col_incremental

        date_max_col_inct = df_val_inct.agg({col_to_check: 'max'}).first()[0]
        return date_max_col_inct


    @staticmethod
    def delte_file_hdfs(spark_sesion, path_file: str):
        java_import(spark_sesion._jvm, 'org.apache.hadoop.fs.FileSystem')
        java_import(spark_sesion._jvm, 'org.apache.hadoop.fs.Path')

        fs = spark_sesion._jvm.FileSystem.get(spark_sesion._jsc.hadoopConfiguration())
        path_hdp = spark_sesion._jvm.Path(path_file)

        if fs.exists(path_hdp):
            fs.delete(path_hdp, True)
            print(f'[OK] clear success - file delete: {path_file}')
        else:
            print(f'[ERROR] clear failed - retrie delete: {path_file}')


    @staticmethod
    def save_logs_intakes(
        spark_sesion,
        job_name: str,
        environment: str,
        cols_read: int,
        records_read: int,
        schema: str,
        table: str,
        source_path: str,
        status: str,
        error_message: str
    ):

        now = datetime.now()
        start_time = now.strftime('%Y-%m-%d %H:%M:%S')
        start_date = now.strftime('%Y-%m-%d')
        execution_id = str(uuid.uuid4())
        
        if environment == 'P':
            environment_name = 'PRODUCCION'
        elif environment == 'D':
            environment_name = 'DESARROLLO'
        else:
            raise ValueError(f'[ERROR] environment insert is not correct.')

        log_row = Row(
            date_start=start_time,
            execution_id=execution_id,
            spark_app_id=spark_sesion.sparkContext.applicationId,
            job_name=job_name,
            environment=environment_name,
            cols_read=cols_read,
            records_read=records_read,
            schema=schema.lower(),
            table=table.lower(),
            source_path=source_path,
            status=status,
            proccess_messages=error_message,
            date_partition_logs=start_date
        )

        log_df = spark_sesion.createDataFrame([log_row]) \
            .select(
                'date_start',
                'execution_id',
                'spark_app_id',
                'job_name',
                'environment',
                'cols_read',
                'records_read',
                'schema',
                'table',
                'source_path',
                'status',
                'proccess_messages',
                'date_partition_logs'
            )

        log_df.write.mode('append').insertInto('staging.tb_gbdt_logs_intakes')


    @staticmethod
    def print_statistics(df_gob, rows_view: int = 10):
        df_gob.printSchema()
        df_gob.show(rows_view, truncate=False)
    

    @staticmethod
    def hash_col(col_name: str, new_name_col: str = None, df_gob = None):
        out_col = new_name_col or col_name
        if df_gob:
            return df_gob.withColumn(out_col, sha2(col(col_name).cast('string'), 256))
        if df_gob is None:
            return sha2(col(col_name).cast('string'), 256)


    @staticmethod
    def read_pandas_to_pyspark(spark_sesion, path_file: str, cols_rename=None, delimiter_value=None, name_sheet=None):
        with hdfs.open(path_file, 'rb') as hdfs_file:
            if delimiter_value and name_sheet:
                df_pd = pd.read_excel(hdfs_file, sep=delimiter_value, sheet_name=name_sheet, dtype=str).fillna('')
            elif name_sheet:
                df_pd = pd.read_excel(hdfs_file, sheet_name=name_sheet, dtype=str).fillna('')
            else:
                df_pd = pd.read_excel(hdfs_file, dtype=str).fillna('')
            
            if cols_rename:
                df_ps = spark_sesion.createDataFrame(df_pd).toDF(*cols_rename)
            else:
                df_ps = spark_sesion.createDataFrame(df_pd)
            
            return df_ps
