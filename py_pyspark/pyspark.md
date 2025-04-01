# PySpark

## Lista funciones de PySpark.
|Función|Uso|
|-------|---|
| [Esencial Para Uso](#esencial) | Generar instalación, e importar la librería para poderla utilizar. |
| [Config](#config) | Configuraciones para la creación de la sesión de Spark. |
| [Read HIVE](#crear-dataframe-en-base-a-hive) | Crear un DataFrame en base a una tabla HIVE. |
| [To HIVE](#guardar-el-dataframe-como-tabla-hive) | Exportar un DataFrame en HIVE. |
| [Read TXT](#crear-el-dataframe-a-partir-de-un-archivo-txt) | Crear un DataFrame en base a un archivo TXT. |
| [Read CSV](#crear-el-dataframe-a-partir-de-un-archivo-csv) | Crear un DataFrame en base a un archivo CSV. |
| [To CSV](#crear-el-DataFrame-a-partir-de-un-archivo-csv) | Exportan un DataFrame en un archivo CSV. |
| [Read Excel](#crear-el-dataframe-a-partir-de-un-archivo-excel) | Crear un DataFrame en base a un archivo Excel. |
| [To Excel](#exportar-un-dataframe-a-un-archivo-excel) | Exportan un DataFrame en un archivo Excel. |
| [Read JDBC](#crear-el-dataframe-a-partir-de-un-motor-de-base-de-datos) | Crear un DataFrame en base a una Base de Datos. |

---

### Esencial
1. JDK: Es necesario contar con Java, se debe descargar e instalar desde Oracle. Descarga la versión correspondiente para tú sistema operativo, para Windows se recomienda 'x64 Installer'
   - Link: https://www.oracle.com/java/technologies/downloads/

2. Hadoop: Es necesario contar con los drivers necesarios Binarios para su correcta ejecución. Descarga la versión más reciente del siguiente repositorio.
   - Link: https://github.com/steveloughran/winutils

3. JAR: El .jar a descargar dependerá del motor de base de datos que utilices.
   - Link SQL Server: https://learn.microsoft.com/es-es/sql/connect/spark/connector?view=sql-server-ver16
   - Link Postgresql: https://jdbc.postgresql.org/download/?utm_source=chatgpt.com
   - Link MySQL: https://dev.mysql.com/downloads/connector/j/
   - Link Oracle: https://www.oracle.com/co/database/technologies/appdev/jdbc-downloads.html

4. Automatico: Driver para creación de DataFrame en base a archivos Excel, una vez instalado no es necesario importarlo.
    ```python
    # Instalar la librería necesaria.
    pip install spark-excel

    spark = SparkSession.builder \
        .appName('MiApp') \
        # Debe agregarse está configuración para su correcta ejecución.
        .config('spark.jars.packages', 'com.crealytics:spark-excel_2.12:0.13.7') \
        .getOrCreate()
    ```
    Manual: Si requieres un control más especifico sobre las versiones, se recomienda descargar el .jar y anexalo en la ruta.
    - Link: https://mvnrepository.com/artifact/com.crealytics/spark-excel_2.12
    ```python
    spark = SparkSession.builder \
        .appName('MiApp') \
        .config('spark.jars', 'ruta/al/spark-excel_2.12-0.13.7.jar') \
        .getOrCreate()
    ```

Se recomienda generar en tu proyecto la carpeta Tools, y allí generar cada carpeta.
```
mi_proyect
 - tools
   - jdk  --> versión de Java con Oracle.
   - hadoop  --> los archivos binarios.
   - jdbc  --> los .jar correspondientes a tú proyecto.
    - excel (Driver del excel en caso de ser descargado manualmente).
```

---

### Config

```python
from pyspark import SparkConf
from pyspark.sql import SparkSession

# Metodo 1
spark = SparkSession.builder \
    .appName('MiApp') \
    .master('local[*]') \
    .config('spark.executor.memory', '2g') \
    .config('spark.sql.shuffle.partitions', '8')
    .getOrCreate()

# Metodo 2 SparkConf
confg = SparkConf() \
   .setMaster('local[*]') \
   .setAppName("MiApp") \
   .set('spark.executor.memory', '2g') \
   .set('spark.sql.shuffle.partitions', '8')

spark = SparkSession.builder \
    .config(conf=confg) \
    .getOrCreate()
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| spark.app.name | (vacío) | Nombre de la aplicación Spark. | .set('spark.app.name', 'MiApp') |
| spark.master | * | Define el master: local[*], yarn, mesos, k8s, etc. | .setMaster('local[*]') |
| spark.submit.deployMode | client | client o cluster. | .set('spark.submit.deployMode', 'client') |
| spark.ui.port | 4040 | Puerto de la UI de Spark. | .set('spark.ui.port', '4041') |
| spark.executor.memory | 1g | Cantidad de memoria para cada executor (Ej: 2g). | .set('spark.executor.memory', '2g') |
| spark.executor.cores | 1 | Núcleos por executor. | .set('spark.executor.cores', '4') |
| spark.executor.instances |  | Número de executors. | .set('spark.executor.instances', '3') |
| spark.driver.memory | 1g | Memoria para el driver. | .set('spark.driver.memory', '2g') |
| spark.driver.cores | 1 | Núcleos para el driver. | .set('spark.driver.cores', '2') |
| spark.dynamicAllocation.enabled | false | Habilita asignación dinámica de recursos (true / false). | .set('spark.dynamicAllocation.enabled', 'true') |
| spark.sql.shuffle.partitions | 200 | Número de particiones por defecto para shuffles. | .set('spark.sql.shuffle.partitions', '8') |
| spark.default.parallelism |  | Paralelismo por defecto. | .set('spark.default.parallelism', '16') |
| spark.serializer | org.apache.spark.serializer.JavaSerializer | Serializador. Recomendado: KryoSerializer. | .set('spark.serializer', 'org.apache.spark.serializer.KryoSerializer') |
| spark.kryo.registrationRequired | false | Si es true, requiere registro explícito de clases. | .set('spark.kryo.registrationRequired', 'true') |
| spark.storage.memoryFraction | 0.6 | Fracción de memoria para almacenamiento (0.6 por defecto). | .set('spark.storage.memoryFraction', '0.7') |
| spark.memory.fraction | 0.6 | Fracción de memoria ejecutora utilizada para almacenamiento. | .set('spark.memory.fraction', '0.7') |
| spark.authenticate | false | Habilita autenticación. | .set('spark.authenticate', 'true') |
| spark.authenticate.secret |  | Secreto compartido para autenticación. | .set('spark.authenticate.secret', 'miSecreto123') |
| spark.ssl.enabled | false | Habilita SSL. | .set('spark.ssl.enabled', 'true') |
| spark.sql.catalogImplementation | in-memory | Motor de catálogo (hive o in-memory). | .set('spark.sql.catalogImplementation', 'hive') |
| spark.sql.warehouse.dir | ./spark-warehouse | Directorio del almacén de datos. | .set('spark.sql.warehouse.dir', '/user/hive/warehouse') |
| spark.sql.autoBroadcastJoinThreshold | 10485760 | Tamaño máximo de un DataFrame para broadcast join. | .set('spark.sql.autoBroadcastJoinThreshold', '52428800') |
| spark.eventLog.enabled | false | Habilita el registro de eventos. | .set('spark.eventLog.enabled', 'true') |
| spark.eventLog.dir |  | Directorio para guardar logs de eventos. | .set('spark.eventLog.dir', '/tmp/spark-events') |
| spark.yarn.queue | default | Cola de YARN donde enviar la aplicación. | .set('spark.yarn.queue', 'production') |
| spark.yarn.am.memor | 512m | Memoria para el ApplicationMaster en YARN. | .set('spark.yarn.am.memory', '1g') |
| spark.rdd.compress | false | Habilita compresión de RDDs. | .set('spark.rdd.compress', 'true') |
| spark.broadcast.compress | true | Habilita compresión de variables broadcast. | .set('spark.broadcast.compress', 'true') |
| spark.sql.inMemoryColumnarStorage.compressed | true | Comprime almacenamiento en memoria. | .set('spark.sql.inMemoryColumnarStorage.compressed', 'true') |
| spark.hadoop.* |  | Cualquier configuración específica de Hadoop. | .set('spark.hadoop.fs.defaultFS', 'hdfs://localhost:9000') |

---

### Crear DataFrame en base a Hive.
Recuerda tene e lDriver correspondiente para poder realizar está función (hive-site.xml).
```python
# Leer una consulta SQL
df = spark.sql('SELECT * FROM bbdd_name.tb_name')

# Cargar una tabla directamente.
df = spark.table('bbdd_name'.'tb_name')
```

---

### Guardar el DataFrame como tabla HIVE.
```python
df.write.saveASTable('bbdd_name.tb_name')

# append, error (otros modos para poderlo guardar)
df.write.saveASTable('bbdd_name.tb_name', mode='overwrite')

# guardarlo como una tabla externa HIVE
df.write.saveASTable('bbdd_name.tb_name', path=<ruta/de/tabla/externa>)
```

---

### Crear el DataFrame a partir de un archivo TXT.
```python
df = spark.read \
    .format('text') \
    .option('wholetext', 'false')  # Si true, lee todo el archivo como un solo registro
    .option('lineSep', '\n')  # Separador de líneas
    .option('encoding', 'UTF-8')  # Codificación del archivo
    .option('compression', 'none')  # Tipo de compresión (none, bzip2, gzip, lz4, snappy y deflate)
    .option('pathGlobFilter', '*.txt')  # Filtro de nombres de archivo
    .option('recursiveFileLookup', 'false')  # Buscar archivos en subdirectorios
    .option('modifiedBefore', None)  # Filtrar archivos modificados antes de timestamp
    .option('modifiedAfter', None)  # Filtrar archivos modificados después de timestamp
    .option('locale', 'en-US')  # Configuración regional
    .option('mode', 'PERMISSIVE')  # Modo de lectura (PERMISSIVE, DROPMALFORMED, FAILFAST)
    .option('multiLine', 'false')  # Soporte para registros multilínea
    .option('charToEscapeQuoteEscaping', '\\')  # Carácter para escapar citaciones
    .option('enforceSchema', 'true')  # Aplicar esquema estrictamente
    .option('samplingRatio', '1.0')  # Proporción de muestreo
    .option('ignoreMissingFiles', 'false')  # Ignorar archivos faltantes
    .option('maxColumns', '20480')  # Número máximo de columnas
    .option('maxCharsPerColumn', '-1')  # Caracteres máximos por columna
    .option('columnNameOfCorruptRecord', '_corrupt_record')  # Columna para registros corruptos
    .load('ruta/archivo.txt')
```

### Crear el DataFrame a partir de un archivo CSV.
```python
df = spark.read \
    .format('csv') \
    .option('header', 'false')  # Por defecto no asume encabezados
    .option('delimiter', ',')  # Separador por defecto es coma
    .option('quote', '\'')  # Carácter de citación
    .option('escape', '\\')  # Carácter de escape
    .option('escapeQuotes', 'true')  # Escapa caracteres de citación
    .option('quoteAll', 'false')  # No cita todos los campos
    .option('multiLine', 'false')  # No permite registros multilínea
    .option('inferSchema', 'false')  # No infiere tipos de datos
    .option('enforceSchema', 'true')  # Aplica el esquema estrictamente
    .option('samplingRatio', '1.0')  # Ratio para inferSchema
    .option('nullValue', null)  # Cómo interpretar valores nulos
    .option('nanValue', 'NaN')  # Valor para NaN
    .option('positiveInf', 'Inf')  # Valor para infinito positivo
    .option('negativeInf', '-Inf')  # Valor para infinito negativo
    .option('dateFormat', 'yyyy-MM-dd')  # Formato de fecha
    .option('timestampFormat', 'yyyy-MM-dd'T'HH:mm:ss.SSSXXX')  # Formato timestamp
    .option('maxColumns', '20480')  # Máximo número de columnas
    .option('maxCharsPerColumn', '-1')  # Sin límite de caracteres por columna
    .option('mode', 'PERMISSIVE')  # Modo de análisis
    .option('columnNameOfCorruptRecord', '_corrupt_record')  # Columna para registros corruptos
    .option('encoding', 'UTF-8')  # Codificación por defecto
    .option('locale', 'en-US')  # Configuración regional
    .option('lineSep', '\n')  # Separador de líneas
    .option('pathGlobFilter', '*.csv')  # Filtro de archivos
    .option('recursiveFileLookup', 'false')  # No busca archivos recursivamente
    .option('modifiedBefore', null)  # Filtro por fecha de modificación
    .option('modifiedAfter', null)  # Filtro por fecha de modificación
    .option('unescapedQuoteHandling', 'STOP_AT_DELIMITER')  # Manejo de citas sin escape
    .load('ruta/archivo.csv')
```



---

### Guardar el DataFrame a partir de un archivo CSV.
```python
df.write \
    .format('csv') \
    .option('header', 'false')  # Por defecto no incluye encabezados
    .option('delimiter', ',')  # Separador por defecto es coma
    .option('quote', '\'')  # Carácter de citación por defecto
    .option('escape', '\\')  # Carácter de escape por defecto
    .option('escapeQuotes', 'true')  # Escapa caracteres de citación
    .option('quoteAll', 'false')  # No cita todos los campos
    .option('nullValue', null)  # Representación de valores nulos
    .option('emptyValue', '')  # Valor para campos vacíos
    .option('dateFormat', 'yyyy-MM-dd')  # Formato de fecha
    .option('timestampFormat', 'yyyy-MM-dd'T'HH:mm:ss.SSSXXX')  # Formato timestamp
    .option('compression', 'none')  # Sin compresión por defecto
    .option('encoding', 'UTF-8')  # Codificación por defecto
    .option('ignoreLeadingWhiteSpace', 'true')  # Ignora espacios al inicio
    .option('ignoreTrailingWhiteSpace', 'true')  # Ignora espacios al final
    .option('charToEscapeQuoteEscaping', '\\')  # Carácter para escapar citas
    .option('lineSep', '\n')  # Separador de líneas
    .option('maxColumns', '20480')  # Máximo número de columnas
    .option('maxCharsPerColumn', '-1')  # Sin límite de caracteres por columna
    .mode('error')  # Modo de escritura por defecto
    .save('ruta/archivo.csv')

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

---

### Crear el DataFrame a partir de un archivo Excel
Para la creación de DataFrame en base a un archivo Excel se complica un poco, por el hecho de que está función no viene integrada con PySpark, pero se
puede instalar un driver que nos permitira realiazr estás acciones (Esta descarga se encuentra en el punto 4 de [Esencial Para Uso](#esencial)). Una vez configurado
correctamente puedes proceder de la siguiente forma:

```python
df = spark.read
    .format('com.crealytics.spark.excel') \
    .option('dataAddress', 'A1')
    .option('header', 'true')
    .option('treatEmptyValuesAsNulls', 'true')
    .option('setErrorCellsToFallbackValues', 'fasle')
    .option('usePlainNumberFormat', 'false')
    .option('inferSchema', 'false')
    .option('addColorColumns', 'false')
    .option('timestampFormat', 'yyyy-mm-dd hh:mm:ss[.fffffffff]')
    .option('dateFormat', 'yyyy-MM-dd')
    .option('maxRowsInMemory', None)
    .option('maxByteArraySize', None)
    .option('tempFileThreshold', None)
    .option('excerptSize', 10)
    .option('workbookPassword', None)
    .schema(myCustomSchema)
    .load('Worktime.xlsx')
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| .format() | 'com.crealytics.spark.excel' | Este valor es obligatorio e indica el driver que especifica que se hará la lectura a un archivo Excel. | .format("com.crealytics.spark.excel") |
| .option('dataAddress', '') | 'A1' | Indicar el rango de celdas en donde se encuentra la data para construir el DF. | .option('dataAddress', "'Hoja 1'!B3:C35") |
| .option('header', '') | 'true' | Indica si debe tomar la primera fila como los encabezados de las columnas. | .option('header', 'true') |
| .option('treatEmptyValuesAsNulls', '') | 'true' | Se usa para tratar las celdas vacías en los datos como valores nulos (null) | .option('treatEmptyValuesAsNulls', 'false') |
| .option('setErrorCellsToFallbackValues', '') | 'false' | Indica si los errores dentro de los registros deben dejarse como NULL o el error explicito. | .option('setErrorCellsToFallbackValues', 'true') |
| .option('usePlainNumberFormat', '') | 'false' | Se utiliza para leer los valore númericos de manera 'plana', sin formatos y demás que estén dentro del archivo. | .option('usePlainNumberFormat', 'false') |
| .option('inferSchema', '') | 'false' | Se usa para que psyspark analice los datos de cada columna y asigne automaticamente los tipos de datos más apropiados, en vez de asignarlo todo como un String. | .option('inferSchema', 'false') |
| .option('addColorColumns', '') | 'fasle' | Esta opción permite agregar columnas adicionales al DataFrame para capturar la información de color de las celdas del archivo. | .option('addColorColumns', 'fasle') |
| .option('timestampFormat', '') | 'yyyy-mm-dd hh:mm:ss[.fffffffff]' | Se utiliza para asignar un formato especifico a las columnas TimeStamp | .option('timestampFormat', 'MM-dd-yyyy HH:mm:ss') |
| .option('dateFormat', '') | 'yyyy-MM-dd' | Se utiliza para asignar un formato especifico a las columnas Date | .option('dateFormat', 'yyyyMMdd') |
| .option('maxRowsInMemory', None) | None | Indicara le monto de registos que irá procesando paulatinamente como un estilo 'chunkzise'. | .option('maxRowsInMemory', 20) |
| .option('maxByteArraySize', None) | None | Se utiliza para definir el tamaño máximo, en bytes, de los arreglos de datos (byte arrays) que se pueden manejar en ciertas operaciones de lectura, escritura o procesamiento | .option('maxByteArraySize', 2147483647) |
| .option('tempFileThreshold', None) | None | Define el umbral de tamaño de archivo para que, cuando los datos procesados superen dicho tamaño, Spark los escriba temporalmente en archivos de disco en lugar de mantenerlos en memoria. | .option('tempFileThreshold', '128MB') |
| .option('excerptSize', 10) | 10 | Esta opción controla cuántos bytes de datos se leen a la vez o cuántos se mantienen en memoria cuando se trabaja con grandes volúmenes de datos o datos complejos, como archivos de texto, logs, o bases de datos. | .option('excerptSize', 10) |
| .option('workbookPassword', None) | None | Se utiliza para cuando el archivo contiene clave, brindarla y poder acceder. | .option('workbookPassword', 'pass') |
|.schema(myCustomSchema) | Either inferred schema | Se utiliza para definir un esquema personalizado al leer o escribir datos, particularmente cuando se trabaja con archivos, bases de datos u otras fuentes de datos estructurados. | .schema(myCustomSchema) |

---

### Exportar un DataFrame a un archivo Excel.

```python
df.write \
    .format('com.crealytics.spark.excel') \
    .option('header', 'false')
    .option('dataAddress', "'Sheet1'!A1")
    .option('dateFormat', 'yyyy-mm-dd')
    .option('timestampFormat', 'yyyy-mm-dd hh:mm:ss')
    .option('workbookPassword', null)
    .option('sheetPassword', null)
    .option('useDefaultNumberFormat', 'true')
    .option('numberFormat', null)
    .option('columnNameFormula', 'false')
    .option('keepUndefinedRows', 'false')
    .option('keepNullRows', 'true')
    .option('usePlainNumberFormat', 'false')
    .option('writeMode', 'OVERWRITE')
    .option('preHeaderRows', '0')
    .option('postHeaderRows', '0')
    .option('autoSize', 'false')
    .option('schema_change_policy', 'ERROR')
    .option('maxRowsInMemory', '10000')
    .option('compression', 'NONE')
    .mode('error')
    .save('ruta/archivo.xlsx')
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| .format() | 'com.crealytics.spark.excel' | Este valor es obligatorio e indica el driver que especifica que se exportara en un archivo Excel. | .format('com.crealytics.spark.excel") |
| .option('header', 'flase') | flase | Indica si debe incluir los encabezados en el exporte. | .option('header', 'true') |
| .option('dataAddress', 'A1') | 'A1' | Indica en que fila y columna se exportará la información. | .option('dataAddress', "'NombreHoja'!A1") |
| .option('dateFormat', 'yyyy-MM-dd') | 'yyyy-mm-dd' | Indica el formato en el que se exportará las columnas tipo Date. | .option('dateFormat', 'yyyy-MM-dd') |
| .option('timestampFormat', 'yyyy-MM-dd HH:mm:ss') | 'yyyy-MM-dd HH:mm:ss' | Indica el formato en el que se exportará las columnas tipo TimeStamp. | .option('timestampFormat', 'yyyy-MM-dd HH:mm:ss') |
| .option('workbookPassword', null) | null | Se utiliza para que el archivo exportado tenga una clave asignada. | .option('workbookPassword', 'tupassword') |
| .option('sheetPassword', null) | null | Se utiliza para que en el archivo exportado la hoja tenga una clave asignada. | .option('sheetPassword', 'tupassword') |
| .option('useDefaultNumberFormat', 'true') | true | Si utilizar el formarto de números por defecto o uno especial. | .option('useDefaultNumberFormat', 'true') |
| .option('numberFormat', null) | null | Indicar el formato especifico para las columnas númericas. | .option('numberFormat', '#,##0.00') |
| .option('columnNameFormula', 'false') | false | No permite que hayan formulas en los nombres. | .option('columnNameFormula', 'true') |
| .option('keepUndefinedRows', 'false') | false | No mantiene filas indefinidas. | .option('keepUndefinedRows', 'true') |
| .option('keepNullRows', 'false') | false | Indica si conservas las filas que estén vacías. | .option('keepNullRows', 'true') |
| .option('usePlainNumberFormat', 'false') | false | Indica si utlizar un formato plano para los números o dejar el que ya tienen. | .option('usePlainNumberFormat', 'true') |
| .option('writeMode', 'OVERWRITE') | OVERWRITE | Establece el metodo de escritura si reescribir (overwrite) o anexar (append) | .option('writeMode', 'APPEND') |
| .option('preHeaderRows', '0') | '0' | Indica la cantidad de filas que ahbrán antes del encabezado. | .option('preHeaderRows', '2') |
| .option("postHeaderRows", '0')  | '0' | Indica la cantidad de filas que ahbrán después del encabezado. | .option("postHeaderRows", "0")  |
| .option("autoSize", "false") | false | Indica si deseamos ajustar el tamaño de las celdas al contenido o dejarlo con el tamaño por defecto | .option("autoSize", "true") |
| .option('schema_change_policy', 'ERROR') | 'ERROR' | Indica que hacer si ve cambios en el esquema de los tipos de datos. | .option('schema_change_policy', 'ERROR') |
| .option('maxRowsInMemory', '10000') | '10000' | Indica la cantidad de filas maxima que habrá en memoria. | .option('maxRowsInMemory', '10000') |
| .option('compression', 'NONE') | 'NONE' | Indica si dejeamos exportar el archivo comprimido en gzip. | .option('compression', 'GZIP') |
| .mode('overwrite') | 'error' | Indica el moto en que pyspark hará la escritura y exporte del archivo (overwrite/append/ignore/error) | .mode('overwrite') |
| .save('ruta/archivo.xlsx') | Obligatorio | Recibe la ruta ne donde alojara el archivo Excel. | .save('ruta/archivo.xlsx') |

---

### Crear el DataFrame a partir de un motor de Base de Datos.

```python
df = spark.read \
    .format('jdbc') \
    .option('url', 'jdbc:mysql://host:port/database')  # URL de conexión JDBC, cambia el tipo de base de datos y datos según sea necesario \
    .option('dbtable', 'nombre_de_la_tabla')  # Especifica la tabla o consulta (puede ser una subquery entre paréntesis) \
    .option('user', 'usuario')  # Usuario de la base de datos \
    .option('password', 'contraseña')  # Contraseña del usuario \
    .option('driver', 'com.mysql.cj.jdbc.Driver')  # Controlador JDBC, cambia según el motor de base de datos \
    .option('fetchsize', '1000')  # Tamaño de lote al recuperar filas \
    .option('partitionColumn', 'columna_particion')  # Columna utilizada para particionar los datos \
    .option('lowerBound', 'valor_inferior')  # Límite inferior para la partición \
    .option('upperBound', 'valor_superior')  # Límite superior para la partición \
    .option('numPartitions', '10')  # Número de particiones (hilos para paralelismo) \
    .option('customSchema', 'columna1 INT, columna2 STRING')  # Esquema personalizado (opcional) \
    .option('queryTimeout', '30')  # Tiempo de espera para consultas (segundos) \
    .option('batchsize', '5000')  # Tamaño del lote para operaciones de escritura \
    .option('isolationLevel', 'NONE')  # Nivel de aislamiento de la transacción \
    .option('pushDownPredicate', 'true')  # Permite empujar filtros a la base de datos \
    .option('sessionInitStatement', 'SET search_path TO schema')  # Comando de inicialización de sesión SQL \
    .load()
```

---
