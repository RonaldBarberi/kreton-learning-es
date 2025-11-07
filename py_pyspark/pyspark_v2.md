# PySpark


## Configuración de entorno PySpark.
1. Es necesario contar con Java, se debe descargar e instalar desde Oracle.
2. Descomprime en C:\spark.
3. Añade el winutils.exe descargado a una carpeta de winutils en C:. Debiendo quedar así:
    ```bash
    C:\winutils\bin\winutils.exe
    ```
4. Desde el cmd ejecuta: "cd C:\winutils\bin" y después: "winutils.exe chmod 777\tmp\hive".
5. Añade las variables de entorno.
   - HADOOP_HOME = "C:\winutils"
   - SPARK_HOME = "C:\spark"
   - JAVA_HOME = "C\jdk"

## Tipos de datos.
|Tipo de Dato|Descripción|
|------------|-----------|
|StringType|Cadenas de texto (str).|
|IntegerType|Enteros de 32 bits (int).|
|LongType|Enteros de 64 bits (int de mayor tamaño).|
|FloatType|Números decimales de precisión simple (float).|
|DoubleType|Números decimales de doble precisión (float en Python).|
|BooleanType|Valores booleanos (True o False).|
|DateType|Fechas (sin hora).|
|TimestampType|Tiempos con fecha y hora (precisión hasta microsegundos).|
|BinaryType||

```python
from pyspark.sql.types import (
    StructType, StructField,
    StringType, FloatType, IntegerType,
    DoubleType, BooleanType, DateType,
    TimestampType, DecimalType, BinaryType,
    ArrayType, MapType, StructType
)

schema_spark = StructType([
    StructField("columna1", StringType(), True),
    StructField("columna2", FloatType(), True),
    StructField("columna3", IntegerType(), True),
    StructField("columna4", DoubleType(), True),
    StructField("columna5", BooleanType(), True),
    StructField("columna6", DateType(), True),
    StructField("columna7", TimestampType(), True),
    StructField("columna8", DecimalType(10, 2), True),
    StructField("columna9", BinaryType(), True),
    StructField("columna10", ArrayType(StringType()), True),
    StructField("columna11", MapType(StringType(), IntegerType()), True),
    StructField("columna12", StructType([
        StructField("subcol1", StringType(), True),
        StructField("subcol2", FloatType(), True)
    ]), True)
])
```

## Distintas formas de crear un DataFrame y de exportarlos.

|MODO|DESCRIPCIÓN|
|----|-----------|
|append|Agrega los datos del DataFrame a la lista de archivos que ya existen en la ubicación de destino especificada.|
|overwrite|Sobrescribe completamente cualquier archivo de datos que ya exista en la ubicación de destino especificada con los datos del DataFrame.|
|error errorIfExist default|Es el modo por defecto. Si existe la ubicación de destino especificada, DataFrameWriter arrojará un error.|
|ignore|Si existe la ubicación de destino especificada, simplemente no hará nada.|

- Leyendo la tabla HIVE como DataFrame.
    ```python
    df = spark.table('bbdd_name'.'tb_name')
    ```

- Guardar el DataFrame como tabla HIVE
    ```python
    df.write.saveASTable('bbdd_name.tb_name')

    # append, error (otros modos para poderlo guardar)
    df.write.saveASTable('bbdd_name.tb_name', mode='overwrite')

    # guardarlo como una tabla externa HIVE
    df.write.saveASTable('bbdd_name.tb_name', path=<ruta/de/tabla/externa>)
    ```
 
- Crear el DataFrame a partir de un archivo CSV.
    ```python
    df = spark.read.csv('ruta/de/archivo/csv', sep=',', header=True, inferSchema=True)
    ```

- Guardar el DataFrame a partir de un archivo CSV.
    ```python
    df.write.csv('ruta/de/archivo/csv', sep=';', header=True, mode='overwrite')

    df.write.format('csv').option('sep', ',').save('ruta/de/archivo/nombreArchivoSinExtencion') # Esto devolvera un archivo csv por cada partición que haya.

    df.coalesce(1).write.format('csv').option('sep', ',').save('ruta/de/archivo/nombreArchivoSinExtencion')# Esto devolvera solo 1 archivo con toda la data.

    ruta_salida = r'C:\Users\rbarberi\Documents\01_github\claro_pqrs\data\pqrs\interno\testt'
        rdd = rdd.coalesce(1) \
            .write \
            .option('header', True) \
            .option('delimiter', ',') \
            .mode('overwrite') \
            .csv(ruta_salida)
    ```

- Guardar el DataFrame en un txt.
    ```python
    df.coalesce(1).saveAsTextFile('ruta/de/archivo/txt')
    ```

- Crear un DataFrame a partir de una tabla Relacional.
    ```python
    df = spark.read.format('jdbc')
                .options(url=url, dbtable= <tb_name>, user= <user_name>, password = <password>)
                .load()
    ```

- Guardar un DataFrame en una tabla Relacional.
    ```python
    df = spark.writte.format('jdbc')
                .options(url=url, dbtable= <tb_name>, user= <user_name>, password = <password>)
                .mode('overwrite')
                .save()
    ```

- Crear un DataFrame a partir de un RDD
    ```python
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType

    schema = StructType(
        [
            StructField('column_id', IntegerType(), False), # True es para indicar si o no pueden haber valores NULL/NaN
            StructField('column_name', StringType(), True),
            StructField('column_salary', StringType(), True),
        ]
    )

    df = spark.createDataFrame(rdd, schema=schema)
    ```

- Crear un DataFrame a partir de un Json
    ```python
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType

    schema_json = StructType(
        [
            StructField('column_id', IntegerType(), False), # True es para indicar si o no pueden haber valores NULL/NaN
            StructField('column_name', StringType(), True),
            StructField('column_salary', StringType(), True),
        ]
    )

    df = spark.read.schema(schema_json).json('ruta/de/archivo/json')
    ```


## Operaciones bascias en DataFrames

- Para contar el número de filas count, countDistinct
    
    ```python
    from pyspark.sql.functions import count, countDistinct

    df.count()

    df.select(
        countDistinct('column_id').alias('count_ids'),
        count('column_country').alias('count_country')
    )
    ```

- Para saber el nombre de las columnas
    
    ```python
    df.columns
    ```

- Para saber el tipo de datos de cada columna

    ```python
    df.dtypes
    ```

- Para saber como Spark almacena el esquema del DataFrame

    ```python
    df.schema
    df.printSchema()
    ```

- Para seleccionar columnas del DataFrame.

    ```python
    df.select('id', 'name').show()
    ```

- Para filtrar el DataFrame.
    ```python
    df = df.filter(df['id'] == 1).show()
    
    # o
    df = df.filter(df.id == 1).show()
    
    # o
    from pyspark.sql.functions import col
    df = df.filter(col('id') == 1).show()
    
    # o
    df = df.filter('id == 1').show()
    
    # o filtrado más especifico por cada fila del RDD
    df = df.filter(lambda x: x % 2 == 0)
    
    # & (AND) y | (OR)
    df = df.filter((df['id'] == 1) | (df['id'] == ''))

    # o podemos utilizar 'where'
    df = df.where(col('id') == 1)
    df = df.where("id = 1 AND column_dept = 'tecnologia'")

    # ejemplo más complejo del where

    df = df.select(
        col('id'),
        (col('column_deslikes') / col('column_likes')).alias('new_name_column')
    ).where("id = 1 AND column_dept = 'tecnologia'")
    ```

- Para eliminar columnas del DataFrame (Recordemos que realmente no elimina la columna ya que los DF con de naturaleza inmutable, si no que en su lugar, genera una copia con la modificación).
    ```python
    df = df.drop('id')
    ```

- Para realizar la agrupación de datos en el DataFrame.
    ```python
    from pyspark.sql.functions import min, max, avg, col
    
    df = (df.groupBy('column_dept')
        .agg(
            count('column_salary').alias('count'), # countar elementos de la columna
            sum('column_salary').alias('sum') # sumar valores númericos de la columna
            max('column_salary').alias('max') # obtener el maximo de la columna
            min('column_salary')alias('min') # obtener el minimo de la columna
            avg('column_salary').alias('avg') # obtener el promedio de datos en una columna
        )
    )

    # con uso de pivot
    df = (
        df.groupBy('column_dept').pivot('column_sexo')
        .agg(
            avg('column_salary')
        )
    )
    ```

- Para ordenar los datos del DataFrame.
    ```python
    from pyspark.sql.functions import desc

    df = df.sort('column_salary') # Ascendente
    df = df.sort(desc('column_salary')) # Descendente

    # con oderBy, sería de la siguiente manera:
    df = df.orderBy(col('column_salary')) # Ascendente
    df = df.orderBy(col('column_salary').desc()) # Descendente
    df = df.orderBy(col('column_id'), col('column_salary').desc()) # varios criterios de organización.
    ```

- Función withColumn y withColumnRenamed.
    ```python
    from psyspark.sql.functions import col
    # para solo un criterio.
    df = df.withColumn('column_aprovacion', col('column_likes')- col('column_deslikes'))
    
    # para varios criterios.
    df = (df.withColumn('column_aprovacion', col('column_likes') % col('column_deslikes'))
            .withColumn('column_diferencia', col('column_aprovacion') - 0.9)
    )
    
    # withColumnRenamed renombrar una columna ya existente.
    df = df.withColumnRenamed('column_salary', 'colunm_rename')
    ```

- Para generar columnas derivadas (columnas que proviene de otras columnas existentes).
    ```python
    df.withColumn('column_bono', col('column_salary') * 0.1).show()
    ```

- Join para realizar combinaciones de varios DataFrames. Con PySpark existen los siguientes:
    1. Left Outer: Traerá siempre todos los datos de el DF_A, y los que crucen del DF_B.
    2. Right Join: Traerá siempre todos los datos de el DF_B, y los que crucen del DF_A (Siendo DF_A el principal).
    3. Full Outer: Traerá todos los registros de ambos DFs.
    4. Inner: Traerá todos los registros que crucen del DF_A y el DF_B.
    5. Left Anti: Traera solo los reegistros del DF_A que no crucen con el DF_B.
    6. Right Anti: Traera solo los reegistros del DF_B que no crucen con el DF_A (Siendo DF_A el principal).

    ```python
    left_join = DF_A.join(DF_B, DF_A["id_user"] == DF_B["id_sueldo"], how="left") # Left Outer
    right_join = DF_A.join(DF_B, DF_A["id_user"] == DF_B["id_sueldo"], how="right") # Right Join
    full_outer_join = DF_A.join(DF_B, DF_A["id_user"] == DF_B["id_sueldo"], how="outer") # Full Outer
    inner_join = df_A.join(df_B, DF_A["id_user"] == DF_B["id_sueldo"], how="inner") # Inner
    left_anti = DF_A.join(DF_B, DF_A["id_user"] == DF_B["id_sueldo"], how="left_anti") # Left Anti
    right_anti = DF_A.join(DF_B, DF_A["id_user"] == DF_B["id_sueldo"], how="right_anti") # Right Anti
    ```

- Función UNION, se utiliza para unir DF o RDD los cuales posean las mismas columnas.
    ```python
    df_union_all = df_1.union(df_2)
    ```

- Función map(), para poder realizar transformaciones a cada elemento de un RDD (Resilient Distributed Dataset).
    ```python
    # Poner cada elemento del RDD en mayusculas.
    df = df.map(lambda x: x.upper())
    ```

- Función flatMap()
    ```python
    # Aplana el resultado, si se utilizará map(), devolvería una array, pero con flatMap(), devuelve los valores planos.
    df = df.flatMap(lambda x: (x, x ** 2))
    ```

- Función para agrupar las particiones realizadas en los RDD: Coalesce().
    ```python
    # Cambiara el número d particiones del RDD a solo 5, pudiendo pasar de 10 a solo 5.
    df_5 = df.coalesce(5)
    ```

- Función para transformar las particiones agrupandolas o repartiendolas conforme a la necesidad.
    ```python
    # El RDD cuenta con 3 particiones, podemos aumentarle el número de particiones a 5.
    df_5 = df.repartition(5)
    ```

- Función para fucionar los valores de cada clave usando una función asociativa.
    ```python
    df = spark.parallelize(
        [
            ('casa', 2),
            ('parque', 1),
            ('que', 5),
            ('casa', 1),
            ('escuela', 2),
            ('casa', 1),
            ('que', 1),
        ]
    )

    df_reducido = df.reduceByKey(lambda x,y: x + y)
    df_reducido.collect()
    ```

- Función DISTINCT.
    ```python
    # buscará todas las filas que sean únicas:
    df = df.distinct()

    # para eliminar todos los registros duplicados de una columna:
    df = df.dropDuplicates(['column_id'])
    ```

- Función LIMIT.
    ```python
    df = df.limit(100)
    df = df.orderBy(col('column_salary')).limit(100)
    ```

- Función Drop.
    ```python
    df = df.drop('column_salary') # Eliminar columnas especificas.
    
    df = df.drop('column_salary', 'column_deslike', 'column_like') # Eliminar varias columnas.
    ```

- Función sample.
    ```python
    df = df.sample(fraction=0.8, seed=1234) # Devuelve un conjunto de filas seleccionados de manera aleatoria de un dataframe, recibe un valor porcentual.
    # Se le puede brindar la semilla 'seed' para que los traiga de la misma forma aleatoria.
    ```

- Función randomSplit.
    ```python
    # Genera la partición del DataFrame, brindado el 80% para entrenar el modelo ML y el 20% restante para testear el modelo.
    train, test = df.randomSplit([0.8, 0.2], seed=1234)
    ```

- Función para poder agregar columnas con valores predeterminados.
    ```python
    from pyspark.sql.functions import lit
    
    df = df.withColumn("NUEVA_COLUMNA1", lit("valor1")) \
       .withColumn("NUEVA_COLUMNA2", lit("valor2"))
    ```

### Funciones de fecha y hora.
- Transformar a tipo de datos fecha ( to_date, to_timestamp).
```python
from pyspark.sql.functions import col, to_date, to_timestamp

df = df.select(
    to_date(col('date')).alias('columna_fecha'), # una columna con el correcto formato yyyy-mm-dd lo transforma directamente a tipo de dato date
    to_timestamp(col('datetime')).alias('columna_fecha_hora'), # una columna con el correcto formato yyyy-mm-dd hh:mm:ss lo transforma directamente a tipo de dato datetime

    # si tiene otro formato, sel e indica cual es para que la procese y ajuste al tipo de dato.
    to_date(col('date_bad'), 'dd/MM/yyyy ').alias('columna_formateada_fecha'),
    to_timestamp(col('datetime_bad'), 'dd/MM/yyyy mm:ss').alias('columna_fecha_hora')
)
```
- Para darles formato a las fechas (date_format).
    ```python
    from pyspark.sql.functions import date_format

    df = df.select(
        date_format(col('date'), 'dd-MM-yyyy')
    )
    ```

- Realizar calculos con fechas (datediff, months_between, last_day).
    ```python
    from pyspark.sql.functions import datediff, months_between, last_day

    df = df.select(
        datediff(col('fecha_fin'), col('fecha_ini')).alias('dias'), # saber los días que transcurrieron de una fecha a otra.
        months_between(col('fecha_fin'), col('fecha_ini')).alias('meses'), # saber los meses que transcurrieron de una fecha a otra.
        last_day(col('fecha_fin')).alias('ultimo_dia') # traerá la última fecha de la columna.
    )

- Sumas y restas a fechas (date_add, date_sub)
    ```python
    from pypsrak.sql.functions import date_add, date_sub

    df.select(
        col('name'),
        col('fecha_ini'),
        date_add(col('fecha_ini'), 14).alias('column_sum_days'), # Suma 14 días a la fecha.
        date_sub(col('fecha_ini'), 5).alias('column_sum_days'), # Resta 5 días a la fecha.
    )
    ```

- Extracción de valores de una fecha (year, month, dayofmonth, dayofyear, hour, minute, second)

    ```python
    from pyspark.sql.functions import year, month, dayofmonth, dayofyear, hour, minute, second

    df.select(
        col('fecha_fin'),
        year(col('fecha_fin')),
        month(col('fecha_fin')),
        dayofmonth(col('fecha_fin')),
        dayofyear(col('fecha_fin')),
        hour(col('fecha_fin')),
        minute(col('fecha_fin')),
        second(col('fecha_fin'))
    )
    ```

### Acciones sobre un DataFrame.
```python
df.show(5) # Podemos utilizarlo para visualizar el DF (por defecto montrara 20 registros del DF, pero posible indicarle la cantidad de registros que queremos nos muestre).

df.show(5, truncate=False) # Agregando el parametro truncate=False no limitara la información de las columnas, si no que la mostrará toda.

df.take(1) # Nos muestra la fila o el conjunto de filas que seleccionemos.

df.head(1) # Nos muestra el regiastro de la cabeza solicitado.

df.select(col('column_id')).collect() # Traera todos los valores del DF (Se debe tener cuidado ya que puede generar un amplio consumo de recursos).
```


## Leer consultas SQL con PySpark
- Ejecución de consultas tipo SQL.

- También podemos realizar analisis de datos escribiendo consultas similares a SQL. Para realizar consultas similares a SQL, necesitamos registrar el DataFrame como una Vista Temporal.

    ```python
    # Crear tabla temporal (Pasas el DataFrame que ya se debio haber generado).
    df.createOrReplaceTempView('temp_table')

    # Ejecutar consulta SQL
    spark.sql('SELECT * FROM temp_table WHERE id = 1')

    # Otro ejemplo de seleccionar
    df.select('column_id')
    ```

- Transformaciones.
    ```python
    df.select(
        col('column_likes'),
        col('column_deslikes'),
        (col('column_deslikes') / col('column_likes')).alias('new_name_column')
    )
    ```


## Optimización de Procesos con PySpark.
### Broadcast Join.
Un Broadcast Join es un tipo de unión (join) optimizado en Apache Spark que se utiliza cuando uno de los DataFrames (o tablas) involucrados en la unión es lo suficientemente pequeño como para ser distribuido (o "broadcasted") a todos los nodos del clúster.

En este método, Spark copia el DataFrame más pequeño a la memoria de cada nodo del clúster. Esto elimina la necesidad de transferir datos a través de la red durante la operación de unión, mejorando significativamente el rendimiento en ciertas situaciones.

```python
# ejemplo Join con Broadcast 
df = big_df.join(broadcast(small_df), big_df['id'] == small_df['id'], how="inner")
```


### Almacenamiento en Caché.

```python
df.cache()
df.count()

print('Memory Used : {0}'.format(df.storageLevel.useMemory))
print('Disk Used : {0}'.format(df.storageLevel.useDisk))

# Para utilizar solamente la memoria de la maquina (de lo contrario utilizará la memoria y el disco).
from pyspark.storagelevel import StorageLevel

deptdf.persist(StorageLevel.MEMORY_ONLY)
deptdf.count()
print('Memory Used : {0}'.format(df.storageLevel.useMemory))
print('Disk Used : {0}'.format(df.storageLevel.useDisk))

# Eliminar la memoria caché de los datos
df.unpersist()

# Eliminar todas las tablas almacenadas en caché
slqContext.clearCache()
```
### Valores posibles para almacenamiento
|Nivel de Almacenamiento|Significado|
|-----------------------|-----------|
|MEMORY_ONLY|Almacena RDD como objetos Java deserializados en la JVM. Si el RDD no cabe en la memoria, algunas particiones no se almacenarán en caché y se volveran a calcular sobre lamarcha cada vez que se necesiten. Este es el nivel por defecto.|
|MEMORY_AND_DISK|Almacena RDD como objetos Java deserializados en JVM, Si el RDD no cabe en la memoria, almacena las particiones que no quepan, en el disco y las lee desde allí cuando sea necesario.|
|DISK_ONLY|Almacena las particiones RDD solo en el disco.|
|MEMORY_ONLY_2, MEMORY_AND_DISK_2, etc.|Igual que los niveles anteriores, pero replica cada partición en dos nodos del cluster.|

### Nivel de almacenamiento a elegir, dependiendo la situación.
- Si los RDD caben en la memoria, use "MEMORY_ONLY", ya que es la opción más rápida para el rendimiento de ejecución.
- DISK_ONLY no debe usarse a menos que sus cálculos sean costosos.
- Utilice el alamacenamiento replicado para una mejor tolerancia a fallas si se puede ahorrar la memoria adicional necesaria. Esto evitará que se vuelvan a calcular las particiones perdidas para obtener la mejor disponibilidad.


## Optimización de funciones realizadas por el Usuario.
Podemos utilizar **expr** y **selectExpr**, para generar funciones dentro de pyspark y tenerlo como una evaluación SQL.

```python
from pyspark.sql.functions import expr

cond = """
    CASE
        WHEN column_salary <= 500 THEN 'small_salary'
        WHEN column_salary BETWEEN 501 AND 1000 THEN 'medium_salary'
        WHEN column_salary > 1000 THEN 'high_salary'
        ELSE 'invalid_salary'
    END AS salary_level
"""

df = df.withColumn('salary_level', expr(cond))
df.show()

# traera todas las columnas, más la generada por la condición.
df = df.selectExpr('*', cond)

# hacer la condición conservando solo las columnas involucradas.
df = df.selectExpr(
    'column_id',
    """
    CASE
        WHEN column_salary <= 500 THEN 'small_salary'
        WHEN column_salary BETWEEN 501 AND 1000 THEN 'medium_salary'
        WHEN column_salary > 1000 THEN 'high_salary'
        ELSE 'invalid_salary'
    END AS salary_level
    """
)
```


### Funciones definidas por el Usuario (UDF).
Son funciones que no podemos realizar onc Spark, por lo cual las realizaremos con Python.

```python
def funSalaryLevel(sal):
    level = None

    if(sal <= 500):
        level = 'small_salary'
    elif(sal > 500 & sal < 1000):
        level = 'medium_salary'
    elif(sal > 1000):
        level = 'high_salary'
    else:
        level = 'invalid_salary'
    return level

# Registrar función funSalaryLevel como UDF.
sal_level = udf(funSalaryLevel, StringType())

# Aplicar UDF en pyspark.
df = df.withColumn('salary_level', sal_level('column_salary'))
df.show()
```


## Trabajar valores NULL
- Función para encontrar valores NULL en una columna.
    ```python
    # Filtrar para ver los valores NULL
    df = df.filter(df['column_dept'].isNull())

    # Filtrar para ver los valores NO NULL
    df = df.filter(df['column_dept'].isNotNull())
    ```

- Función para reemplazar los valores nulos.
    ```python
    df = df.fillna('nuevo_valor', ['column_dept'])
    ```

- Función para eliminar las filas con valores nulos.
    ```python
    df = df.dropna() # Eliminara todos los valores nulos.
    df = df.dropna(how = 'all') # Eliminará las filas que contiene todos los valores nulos.
    df = df.dropna(subset = 'column_dept') # Eliminará todas las filas nulas de la columna.
    ```
