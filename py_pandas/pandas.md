# Pandas

## Lista funciones de Pandas.
|Función|Uso|
|-------|---|
| [Esencial Para Uso](#esencial) | Generar instalación, e importar la librería para poderla utilizar. |
| [DataFrame](#dataframe) | Generar un DataFrame en base a un diccionario almanecando en una variable. |
| [Series](#series) | Se utiliza para crear una Serie en Pandas, que es una estructura de datos unidimensional similar a una columna de una tabla o un arreglo unidimensional con etiquetas (índices). |
| [read_csv](#read_csv) | Leer archivos CSV y generar un DataFrame en base a ellos. |
| [to_csv](#to_csv) | Exportar un DataFrame en un archivo CSV. |
| [read_excel](#read_excel)  | Leer archivos XLSX y generar un DataFrame en base a ellos. |
| [to_excel](#to_excel) | Exportar DataFrame en archivo XLSX. |
| [read_sql](#read_sql) | Leer una consulta SQL y en base a ella generar un DataFrame. |
| [to_sql](#to_sql) | Insertará el DataFrame construido en una tabla SQL. |
| [read_json](#read_json) | Leer y generar un DataFrame en base aa un json. |
| [to_json](#to_json) | Exportar un DataFrame en json. |
| [read_html](#read_html) | Generar un DataFrame en base a una tabla (table) HTML |
| [to_html](#to_html) |  Exportar DataFrame en archivos con formato HTML. |
| [read_parquet](#read_parquet) | Leer archivos en formato Parquet y cargarlos en un DataFrame. |
| [to_parquet](#to_parquet) | Exportar DataFrame en archivos con formato Parquet. |
| [read_feather](#read_feather) | Leer archivos en formato Feather y cargarlos en un DataFrame. |
| [to_feather](#to_feather) | Exportar DataFrame en archivos con formato Feather. |
| [read_orc](#read_orc) | Leer archivos en formato ORC y cargarlos en un DataFrame. |
| [read_sas](#read_sas) | Leer archivos en formato SAS y cargarlos en un DataFrame. |
| [read_stata](#read_stata) | Leer archivos en formato Stata (.dta) y cargarlos en un DataFrame. |
| [read_pickle](#read_pickle) | Leer archivos en formato pickle y cargarlos en un DataFrame. |
| [to_pickle](#to_pickle) | Exportar DataFrame en archivos con formato pickle. |
| [read_table](#) | Leer archivos de texto (por ejemplo, archivos .txt) que contienen datos tabulares, donde las columnas están separadas por delimitadores como tabuladores, comas, espacios y cargarlos en un DataFrame. |
| [read_clipboard](#read_clipboard) | Leer datos directamente desde el portapapeles del sistema operativo y cargarlos en un DataFrame. |
| [concat](#concat) |  |
| [merge](#merge) |  |
| [merge_asof](#merge_asof) |  |
| [merge_ordered](#merge_ordered) |  |
| [pivot_table](#pivot_table) |  |
| [pivot](#pivot) |  |
| [crosstab](#crosstab) |  |
| [cut](#cut) |  |
| [qcut](#qcut) |  |
| [melt](#melt) |  |
| [get_dummies](#get_dummies) |  |
| [factorize](#factorize) |  |
| [unique](#unique) |  |
| [value_counts](#value_counts) |  |
| [head](#head) |  |
| [tail](#tail) |  |
| [iloc](#iloc) |  |
| [loc](#loc) |  |
| [at](#at) |  |
| [iat](#iat) |  |
| [columns](#columns) |  |
| [index](#index) |  |
| [describe](#describe) |  |
| [mean](#mean) |  |
| [median](#median) |  |
| [mode](#mode) |  |
| [sum](#sum) |  |
| [prod](#prod) |  |
| [min](#min) |  |
| [max](#max) |  |
| [count](#count) |  |
| [std](#std) |  |
| [var](#var) |  |
| [corr](#corr) |  |
| [cov](#cov) |  |
| [sort_values](#sort_values) | Organizar un DataFrme 'Oder By'. |
| [sort_index](#sort_index) |  |
| [drop](#drop) |  |
| [dropna](#dropna) |  |
| [fillna](#fillna) |  |
| [rename](#rename) |  |
| [set_index](#set_index) |  |
| [reset_index](#) |  |
| [apply](#apply) |  |
| [applymap](#applymap) |  |
| [groupby](#groupby) |  |
| [agg](#agg) |  |
| [merge](#merge) |  |
| [join](#join) |  |
| [pivot](#pivot) |  |
| [melt](#melt) |  |
| [isnull](#isnull) |  |
| [notnull](#notnull) |  |
| [duplicated](#duplicated) |  |
| [drop_duplicates](#drop_duplicates) |  |
| [replace](#replace) |  |
| [add](#add) |  |
| [sub](#sub) |  |
| [mul](#mul) |  |
| [div](#div) |  |
| [round](#round) |  |
| [abs](#abs) |  |
| [clip](#clip) |  |
| [map](#map) |  |
| [apply](#apply) |  |
| [astype](#astype) |  |
| [str.*](#str.*) |  |
| [dt.*](#dt.*) |  |
| [rolling](#expanding) |  |
| [ewm](#ewm) |  |
| [resample](#resample) |  |
| [interpolate](#interpolate) |  |
| [interpolate](#interpolate) |  |
| [query](#query) | Para filtrar los DataFrame conforme a la necesidad. |

## Esencial
1. Para generar la instalación de la libreria de Pandas se debe ejecutar el siguiente comando:
    ```bash
    pip install pandas

    pip install openpyxl
    ```
2. Para importar la librería en el script con el fin de utilizarla.
    ```python
    import pandas as pd
    ```

## DataFrame
```python
df = pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| data | None | Este parametro es fundamental, en el se asigna la variable que contiene la información para generar el DataFrame. | pd.DataFrame(data=None) |
| index | None | Se puede asignar las columna(s) que se utilizarán como índice. | pd.DataFrame(data=None, index=None) |
| columns | None | Parametro para indicar las columnas específicas para cargar. | pd.DataFrame(data=None, index=None, columns=None) |
| dtype | None | Se brinda un diccionario, para indicar desde la lectura el tipo de datos de las columnas (ejemplo: {'col1': str, 'col2': int}). | pd.DataFrame(data=None, index=None, columns=None, dtype=None) |
| copy | False | Si es True, fuerza una copia de los datos, incluso si data es un DataFrame. Por defecto es False. | pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False) |

## Series
```python
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| data | None | Este parametro es fundamental, en el se asigna la variable que contiene la información para generar el DataFrame. | pd.DataFrame(data=None) |
| index | None | Se puede asignar las columna(s) que se utilizarán como índice. | pd.DataFrame(data=None, index=None) |
| dtype | None | Se brinda un diccionario, para indicar desde la lectura el tipo de datos de las columnas (ejemplo: {'col1': str, 'col2': int}). | pd.DataFrame(data=None, index=None, dtype=None) |
| name | None | Nombre de la Serie. Este valor no afecta los datos. | pandas.Series(data=None, index=None, dtype=None, name=None) |
| copy | False | Si es True, fuerza una copia de los datos, incluso si data es un DataFrame. Por defecto es False. | pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False) |
| fastpath | False | Usado internamente para optimización. No se utiliza en la mayoría de los casos de uso habituales. | pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False) |

## read_csv

```python
df = pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, 
                index_col=None, usecols=None, dtype=None, engine=None, converters=None, 
                true_values=None, false_values=None, skipinitialspace=False, skiprows=None, 
                skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, 
                verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, 
                keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, 
                chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, 
                quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, 
                encoding=None, encoding_errors='strict', dialect=None, on_bad_lines=None, 
                delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, 
                storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| filepath_or_buffer | Obligatorio / 'archivo.csv' | Este parametro es fundamental, en el se asigna la ruta del archivo CSV que se leerá. | pd.read_csv(filepath_or_buffer) |
| sep | ',' | Este parametro recibe el delimitador que tiene el archivo CSV, si no se recibe este parametro, asignara una coma por defecto. | pd.read_csv(filepath_or_buffer, sep=';') |
| delimiter | None | Este parametro recibe el delimitador que tiene el archivo CSV, si no se recibe este parametro, asignara una coma por defecto (Es un espejo de sep, pero más antigua al ser espejo de las funciones csv de Python). | pd.read_csv(filepath_or_buffer, delimiter=';') |
| header | 'infer' | Este parmetro indica en que fila se encuentra el encabezado de las columnas. Infer intentara adivinar en donde se ecnuentra, pero por lo general se indica el número de fila. | pd.read_csv(filepath_or_buffer, header=0) |
| names | None | Lista de nombres de columnas, para asignarlos (si el archivo no tiene encabezados). | pd.read_csv(filepath_or_buffer, names=lista_nombres_columnas) |
| index_col | None | Se puede asignar las columna(s) que se utilizarán como índice. | pd.read_csv(filepath_or_buffer, index_col=lista_columnas) |
| usecols | None | Parametro para indicar las columnas específicas para cargar. | pd.read_csv(filepath_or_buffer, usecols=lista_columnas) |
| dtype | None | Se brinda un diccionario, para indicar desde la lectura el tipo de datos de las columnas (ejemplo: {'col1': str, 'col2': int}). | pd.read_csv(filepath_or_buffer, dtype=diccionario_tipo_datos) |
| engine | None | Indicar el motor de backend que utilizará para la lectura del archivo. (engine='c' o engine='python'), el 'c' viene por defecto. | pd.read_csv(filepath_or_buffer, engine='python') |
| converters | None | Permite especificar una función personalizada para convertir columnas de un archivo CSV durante la lectura. ejem: dicConverters = {columna: funcion} | pd.read_csv(filepath_or_buffer, converters=dicConverters) |
| true_values | None | Se utiliza para especificar un conjunto de valores que deben ser interpretados como True cuando pandas lee el archivo CSV. | pd.read_csv(filepath_or_buffer, true_values=lista_columnas) |
| false_values | None | Se utiliza para especificar un conjunto de valores que deben ser interpretados como False cuando pandas lee el archivo CSV. | pd.read_csv(filepath_or_buffer, false_values=lista_columnas) |
| skipinitialspace | False | Se utiliza para indicar si se deben ignorar los espacios en blanco al principio de los campos del archivo CSV. (True, False) | pd.read_csv(filepath_or_buffer, skipinitialspace=Fasle) |
| skiprows | None | Se utiliza para omitir las filas iniciales del archivo CSV durante su lectura. | pd.read_csv(filepath_or_buffer, skiprows=100) |
| skipfooter | 0 | Se utiliza para omitir las filas finales de un archivo CSV durante su lectura. | pd.read_csv(filepath_or_buffer, skipfooter=100) |
| nrows | None | Se utiliza para limitar el número de filas que pandas leerá de un archivo CSV. | pd.read_csv(filepath_or_buffer, nrows=1000) |
| na_values | None | Se utiliza para especificar qué valores deben ser interpretados como NaN (Not a Number), es decir, como valores faltantes o nulos en el DataFrame. | pd.read_csv(filepath_or_buffer, na_values=['NA', 'n/a']) |
| keep_default_na | True | Se utiliza para controlar si se deben mantener los valores predeterminados de pandas como NaN (valores faltantes) al leer un archivo CSV. | pd.read_csv(filepath_or_buffer, keep_default_na=True) |
| na_filter | True | Se utiliza para activar o desactivar la detección de valores faltantes (NaN) en el archivo CSV. | pd.read_csv(filepath_or_buffer, na_filter=True) |
| verbose | False | Se utiliza para controlar la cantidad de información detallada que se muestra durante la lectura del archivo CSV. (True or False) | pd.read_csv(filepath_or_buffer, verbose=True) |
| skip_blank_lines | True | Se utiliza para controlar si se deben ignorar las líneas en blanco (es decir, las filas vacías) al leer un archivo CSV. (True or False) | pd.read_csv(filepath_or_buffer, skip_blank_lines=True) |
| parse_dates | False | Se utiliza para convertir columnas que contienen fechas en tipos de datos de fecha y hora (como datetime64). (bool, list, dict, or None) | pd.read_csv(filepath_or_buffer, parse_dates=lista_columnas) |
| infer_datetime_format | False | Se utiliza para mejorar la eficiencia al analizar columnas de fecha. Cuando se establece en True, pandas intentará inferir automáticamente el formato de las fechas en las columnas que se procesen. Esto puede hacer que la conversión de fechas sea más rápida, especialmente si las fechas siguen un formato consistente en todo el archivo. (True or False) | pd.read_csv(filepath_or_buffer, infer_datetime_format=True) |
| keep_date_col | False | Se utiliza para mantener la columna original que contiene las fechas después de que se haya realizado la conversión de las fechas en formato datetime. (True or False) | pd.read_csv(filepath_or_buffer, keep_date_col=False) |
| date_parser | None | Permite especificar una función personalizada para convertir las cadenas de texto que representan fechas en un formato datetime específico. | pd.read_csv(filepath_or_buffer, date_parser=funTransformColumnsDates) |
| dayfirst | False | Se utiliza para indicar si el día debe ser interpretado como la parte inicial de la fecha (en lugar del mes) cuando pandas está parseando una columna con fechas. (True or False) | pd.read_csv(filepath_or_buffer, dayfirst=False) |
| cache_dates | True | Se utiliza para mejorar el rendimiento al leer archivos CSV que contienen columnas de fechas. Si se establece en True, pandas almacenará en caché las fechas que ya ha procesado, lo que puede hacer que la carga de los datos sea más rápida, especialmente si hay muchas fechas repetidas o si el archivo es grande. (True or False) | pd.read_csv(filepath_or_buffer, cache_dates=True) |
| iterator | False | Permite leer archivos CSV de manera iterativa, lo que es útil cuando se están trabajando con archivos de gran tamaño que no se pueden cargar completamente en memoria. Al establecer iterator=True, pandas devuelve un iterador que se puede usar para leer el archivo en partes (o "chunks"). (True or False) | pd.read_csv(filepath_or_buffer, iterator=True) |
| chunksize | None | Especifica el número de filas que pandas debe leer en cada fragmento (o "chunk") al leer un archivo CSV. | pd.read_csv(filepath_or_buffer, chunksize=1000) |
| compression | 'infer' | Se utiliza para especificar el tipo de compresión del archivo CSV que estás leyendo. Este parámetro permite leer archivos CSV comprimidos de forma directa, sin necesidad de descomprimirlos previamente en el sistema de archivos. ('infer'  |  'gzip'  |  'bz2'  |  'zip'  |  'xz'  |  'lzma'  |  None) | pd.read_csv(filepath_or_buffer, compression='gzip') |
| thousands | None | Se utiliza para especificar el carácter que se usa para representar los separadores de miles en un archivo CSV. | pd.read_csv(filepath_or_buffer, thousands=',') |
| decimal | '.' | Se utiliza para especificar el carácter que se usa como separador decimal en los números dentro de un archivo CSV. | pd.read_csv(filepath_or_buffer, decimal=',') |
| lineterminator | None | Se utiliza para especificar el carácter o la secuencia de caracteres que se utilizará para terminar las líneas en el archivo CSV. | pd.read_csv(filepath_or_buffer, lineterminator='\r\n') |
| quotechar | ' " ' | Se utiliza para especificar el carácter que se debe usar para citar (envolver) los campos de texto en un archivo CSV. Este parámetro es útil cuando los datos en el archivo CSV contienen comas, saltos de línea u otros caracteres especiales dentro de los campos de texto, y necesitas que esos campos sean tratados como una unidad. | pd.read_csv(filepath_or_buffer, quotechar='"') |
| quoting | 0 | Se utiliza para controlar cuándo los campos de texto deben ser citados en el archivo CSV, es decir, cuándo se deben utilizar comillas alrededor de los campos. (csv.QUOTE_MINIMAL (valor 0): Solo se citan los campos que contienen el delimitador de campo (por ejemplo, una coma) o caracteres especiales (como saltos de línea). csv.QUOTE_ALL (valor 1): Todos los campos de texto se citan, independientemente de su contenido. csv.QUOTE_NONNUMERIC (valor 2): Solo se citan los campos que contienen texto no numérico. csv.QUOTE_NONE (valor 3): No se utilizan comillas para ningún campo, incluso si contienen caracteres especiales.) | pd.read_csv(filepath_or_buffer, quoting=csv.QUOTE_MINIMAL) |
| doublequote | True | Se utiliza para especificar cómo se deben manejar las comillas dobles dentro de los campos citados en un archivo CSV. | pd.read_csv(filepath_or_buffer, doublequote=True) |
| escapechar | None | Se utiliza para especificar un carácter de escape dentro de los campos de texto en un archivo CSV. | pd.read_csv(filepath_or_buffer, escapechar='\\') |
| comment | None | Se utiliza para identificar los comentarios en un archivo CSV. | pd.read_csv(filepath_or_buffer, comment='#') |
| encoding | None | Se utiliza para especificar la codificación de caracteres del archivo CSV que se va a leer. | pd.read_csv(filepath_or_buffer, encoding='utf-8') |
| encoding_errors | 'strict' | Se utiliza para manejar los errores de codificación cuando se lee un archivo CSV con una codificación específica. | pd.read_csv(filepath_or_buffer, encoding_errors='ignore') |
| dialect | None | Se utiliza para especificar un conjunto predefinido de reglas que definen el formato de los archivos CSV, como los delimitadores, las comillas y otros aspectos de la estructura del archivo. | pd.read_csv(filepath_or_buffer, dialect='excel') |
| on_bad_lines | None | Se utiliza para manejar las líneas mal formateadas o incorrectas dentro de un archivo CSV. ('error' (valor predeterminado): Genera un error si se encuentra una línea mal formada y detiene el proceso de lectura. 'warn': Muestra una advertencia pero sigue leyendo el archivo. Las líneas mal formadas se omiten, pero se indica el problema. 'skip': Omite las líneas mal formadas sin generar advertencias ni errores. Simplemente se saltan y se sigue procesando el archivo.) | pd.read_csv(filepath_or_buffer, on_bad_lines='skip') |
| delim_whitespace | False | Se utiliza para indicar si los espacios en blanco (espacios y tabulaciones) deben considerarse como delimitadores en lugar de un solo carácter delimitador, como una coma o tabulación. | pd.read_csv(filepath_or_buffer, delim_whitespace=True) |
| low_memory | True | Controla cómo pandas maneja la lectura de archivos CSV grandes que no caben completamente en memoria. (True (predeterminado): Utiliza un enfoque optimizado para leer grandes archivos CSV, procesando los datos por fragmentos en lugar de cargar el archivo completo en memoria a la vez. Esto reduce el uso de memoria, pero puede hacer que pandas intente inferir los tipos de datos en varias pasadas, lo que puede generar advertencias sobre la conversión de tipos. False: Lee el archivo de una vez, cargando todos los datos en memoria antes de procesarlos. Esto puede consumir más memoria, pero a menudo es más rápido si el archivo cabe en la memoria) | pd.read_csv(filepath_or_buffer, low_memory=True) |
| memory_map | False | Se utiliza para mejorar la eficiencia en la lectura de archivos CSV grandes, al permitir que pandas utilice un mapa de memoria en lugar de cargar todo el archivo en la memoria directamente. | memory_map=True |
| float_precision | None | Se utiliza para especificar cómo se deben manejar los números de punto flotante al leer un archivo CSV ('none', 'high', 'round_trip') | pd.read_csv(filepath_or_buffer, float_precision='high') |
| storage_options | None | Se utiliza para proporcionar opciones adicionales de configuración para acceder a archivos almacenados en ubicaciones remotas o en sistemas de almacenamiento específicos, como Amazon S3, Google Cloud Storage, o incluso en sistemas de archivos locales. | pd.read_csv(filepath_or_buffer, storage_options=dicConectAws) |

## to_csv

```python
df.to_csv(path_or_buffer, sep=',', na_rep='', float_format=None, columns=None, 
                        header=True, index=True, index_label=None, mode='w', encoding=None, 
                        compression='infer', quoting=None, quotechar='"', line_terminator=None, 
                        chunksize=None, date_format=None, doublequote=True, escapechar=None, 
                        decimal='.', errors='strict', storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso | 
| ----- | ------- | ------- | ----------- | 
| path_or_buffer | Obligatorio / 'archivo.csv' | Este parametro es fundamental, en el se asigna la ruta del archivo CSV que se leerá. | df.to_csv(path_or_buffer) | 
| sep | ',' | Este parametro recibe el delimitador que tiene el archivo CSV, si no se recibe este parametro, asignara una coma por defecto. | df.to_csv(path_or_buffer, sep=';') | 
| na_rep | '' | Se utiliza para especificar qué valor debe reemplazar los valores NaN (Not a Number) o None cuando se exporta un DataFrame a un archivo CSV. | df.to_csv(path_or_buffer, na_rep='NULL') | 
| float_format | None | Se utiliza para especificar el formato de los números de punto flotante (floats) cuando se exporta un DataFrame a un archivo CSV. | df.to_csv(path_or_buffer, float_format='%.2f') | 
| columns | None | Se utiliza para especificar un subconjunto de columnas que deseas exportar al archivo CSV. | df.to_csv(path_or_buffer, columns=None) |
| header | True | Este parmetro indica en que fila se encuentra el encabezado de las columnas. Infer intentara adivinar en donde se ecnuentra, pero por lo general se indica el número de fila. | df.to_csv(path_or_buffer, header=True) |
| index | True | Controla si se deben escribir o no los índices del DataFrame en el archivo CSV resultante. | df.to_csv(path_or_buffer, index=True) |
| index_label | None | Permite especificar un nombre para la columna que representa el índice cuando se guarda el DataFrame en un archivo CSV. | df.to_csv(path_or_buffer, index_label=None) |
| mode | 'w' | Define el modo de apertura del archivo. 'w' para sobrescribir y 'a' para agregar. | df.to_csv(path_or_buffer, mode='a') |
| encoding | None | Define la codificación de caracteres del archivo. Usualmente 'utf-8' o 'latin1'. | df.to_csv(path_or_buffer, encoding='utf-8') |
| compression | 'infer' | Especifica el tipo de compresión a aplicar al archivo. Los valores posibles incluyen 'gzip', 'bz2', 'zip', entre otros. | df.to_csv(path_or_buffer, compression='gzip') |
| quoting | None | Controla el comportamiento de las comillas en los valores exportados. | df.to_csv(path_or_buffer, quoting=csv.QUOTE_MINIMAL) |
| quotechar | '"' | Define el carácter utilizado para las comillas en los valores exportados. | df.to_csv(path_or_buffer, quotechar='"') |
| line_terminator | None | Define el carácter que se utilizará para terminar las líneas en el archivo CSV. | df.to_csv(path_or_buffer, line_terminator='\n') |
| chunksize | None | Si se define, el DataFrame se escribirá en fragmentos de este tamaño. Esto es útil para escribir grandes archivos CSV sin agotar la memoria. | df.to_csv(path_or_buffer, chunksize=1000) |
| date_format | None | Permite definir un formato para las fechas en el DataFrame antes de exportarlas. | df.to_csv(path_or_buffer, date_format='%Y-%m-%d') |
| doublequote | True | Si es True, se utilizan dos comillas para escapar una comilla en un valor. | df.to_csv(path_or_buffer, doublequote=True) |
| escapechar | None | Especifica un carácter de escape para los caracteres especiales. | df.to_csv(path_or_buffer, escapechar='\\') |
| decimal | '.' | Define el carácter a utilizar para separar los decimales en números. | df.to_csv(path_or_buffer, decimal=',') |
| errors | 'strict' | Controla cómo manejar los errores de codificación. Los valores posibles son 'strict', 'ignore', y 'replace'. | df.to_csv(path_or_buffer, errors='ignore') |
| storage_options | None | Permite especificar opciones de almacenamiento adicionales, como la configuración para acceder a archivos en almacenamiento remoto. | df.to_csv(path_or_buffer, | storage_options={'key': 'value'}) |


## read_excel

```python
df = pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, 
                  squeeze=None, dtype=None, engine=None, converters=None, 
                  true_values=None, false_values=None, skiprows=None, nrows=None, 
                  na_values=None, keep_default_na=True, na_filter=True, verbose=False, 
                  parse_dates=False, date_parser=None, thousands=None, decimal='.', 
                  comment=None, skipfooter=0, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| io |  Obligatorio | Este parametro es fundamental, en el se asigna la ruta del archivo XLSX que se leerá. | pd.read_excel(io) |
| sheet_name | 0 | Se utiliza para especificar la hoja que se leerá. Puede ser el índice de la hoja o el nombre de la hoja. | pd.read_excel(io, sheet_name=0) |
| header | 0 | Define en qué fila están los nombres de las columnas. | pd.read_excel(io, header=0) |
| names | None | Permite especificar una lista de nombres de columnas en caso de que se desee reemplazar los nombres originales del archivo Excel. | pd.read_excel(io, names=None) |
| index_col | None | Especifica qué columna usar como índice del DataFrame. | pd.read_excel(io, index_col=None) |
| usecols | None | Se utiliza para seleccionar un subconjunto de columnas a leer del archivo Excel. | pd.read_excel(io, usecols=None) |
| squeeze | None | Si se establece en True, se devuelve una serie si el DataFrame tiene una sola columna. | pd.read_excel(io, squeeze=None) |
| dtype | None | Permite especificar el tipo de datos que deben tener las columnas. | pd.read_excel(io, dtype=None) |
| engine | None | Permite especificar el motor que se utilizará para leer el archivo Excel. | pd.read_excel(io, engine=None) |
| converters | None | Se utiliza para aplicar una función de conversión a columnas específicas durante la lectura. | pd.read_excel(io, converters=None) |
| true_values | None | Permite especificar qué valores deben ser considerados como True. | pd.read_excel(io, true_values=None) |
| false_values | None | Permite especificar qué valores deben ser considerados como False. | pd.read_excel(io, false_values=None) |
| skiprows | None | Permite saltar filas al leer el archivo Excel. | pd.read_excel(io, skiprows=None) |
| nrows | None | Se utiliza para leer un número específico de filas del archivo Excel. | pd.read_excel(io, nrows=None) |
| na_values | None | Permite especificar qué valores deben ser tratados como NaN. | pd.read_excel(io, na_values=None) |
| keep_default_na | True | Controla si los valores NA por defecto deben ser considerados como NaN. | pd.read_excel(io, keep_default_na=True) |
| na_filter | True | Controla si se debe filtrar los valores NaN mientras se lee el archivo Excel. | pd.read_excel(io, na_filter=True) |
| verbose | False | Si se establece en True, se muestra información adicional durante el proceso de lectura. | pd.read_excel(io, verbose=False) |
| parse_dates | False | Controla si se deben analizar las fechas y convertirlas a tipo datetime. | pd.read_excel(io, parse_dates=False) |
| date_parser | None | Permite especificar una función personalizada para analizar las fechas. | pd.read_excel(io, date_parser=None) |
| thousands | None | Se utiliza para definir el carácter que se usará como separador de miles. | pd.read_excel(io, thousand=None) |
| decimal | '.' | Define el carácter a utilizar para separar los decimales en los números. | pd.read_excel(io, decimal='.') |
| comment | None | Permite especificar un carácter que marque el inicio de los comentarios en las filas del archivo Excel. | pd.read_excel(io, comment=None) |
| skipfooter | 0 | Permite especificar cuántas filas deben ser omitidas al final del archivo Excel. | pd.read_excel(io, skipfooter=None) |
| storage_options | None | Permite especificar opciones de almacenamiento adicionales, como la configuración para acceder a archivos en almacenamiento remoto. | pd.read_excel(io, storage_options=None) |


## to_excel

```python
df.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, 
                      header=True, index=True, index_label=None, startrow=0, startcol=0, 
                      engine=None, merge_cells=True, encoding=None, inf_rep='inf', 
                      xlsxwriter_options=None, date_format=None, datetime_format=None)

```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| excel_writer | Obligatorio |  Este parametro es fundamental, en el se asigna la ruta del archivo XLSX que se leerá. | df.to_excel(excel_writer) |
| sheet_name | 'Sheet1' | Define el nombre de la hoja en el archivo Excel donde se escribirán los datos. | df.to_excel(excel_writer, sheet_name='Sheet1') |
| na_rep | '' | Permite especificar qué valor debe reemplazar los valores NaN o None cuando se exporta un DataFrame a un archivo Excel. | df.to_excel(excel_writer, na_rep='') |
| float_format | None | Se utiliza para especificar el formato de los números de punto flotante cuando se exporta un DataFrame a un archivo Excel. | df.to_excel(excel_writer, float_format=None) |
| columns | None | Permite especificar un subconjunto de columnas que deseas exportar al archivo Excel. | df.to_excel(excel_writer, columns=None) |
| header | True | Este parámetro controla si se debe escribir o no la fila de encabezado. Si es True, se incluye. | df.to_excel(excel_writer, header=True) |
| index | True | Controla si se deben escribir o no los índices del DataFrame en el archivo Excel. | df.to_excel(excel_writer, index=True) |
| index_label | None | Permite especificar un nombre para la columna que representa el índice cuando se guarda el DataFrame en un archivo Excel. | df.to_excel(excel_writer, index_label=None) |
| startrow | 0 | Especifica la fila de inicio para escribir los datos en el archivo Excel. | df.to_excel(excel_writer, startrow=0) |
| startcol | 0 | Especifica la columna de inicio para escribir los datos en el archivo Excel. | df.to_excel(excel_writer, startcol=0) |
| engine | None | Permite especificar el motor que se utilizará para escribir el archivo Excel (por ejemplo, xlsxwriter, openpyxl). | df.to_excel(excel_writer, engine=None) |
| merge_cells | True | Controla si se deben combinar las celdas en el archivo Excel al escribir el DataFrame. | df.to_excel(excel_writer, merge_cells=True) |
| encoding | None | Permite especificar el tipo de codificación para el archivo de salida (por ejemplo, 'utf-8'). | df.to_excel(excel_writer, encoding=None) |
| inf_rep | 'inf' | Especifica el valor que debe reemplazar los valores infinitos cuando se exporta el DataFrame. | df.to_excel(excel_writer, inf_rep='inf) |
| xlsxwriter_options | None | Permite pasar opciones adicionales al motor xlsxwriter (si es utilizado). | df.to_excel(excel_writer, xlsxwriter_options=None) |
| date_format | None | Permite especificar el formato de fecha a utilizar cuando se exporta el DataFrame a Excel. | df.to_excel(excel_writer, date_format=None) |
| datetime_format | None | 	Permite especificar el formato de fecha y hora a utilizar cuando se exporta el DataFrame a Excel. | df.to_excel(excel_writer, datetime_format=None) |


## read_sql
```python
df = pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, 
            columns=None, chunksize=None, dtype=None, sqlalchemy_schema=None, 
            conn=None, schema=None, **kwargs)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| sql | Obligatorio | Este parámetro es fundamental, en él se asigna la consulta SQL que se ejecutará en la base de datos. | pandas.read_sql(sql, con) |
| con | Obligatorio | Se utiliza para pasar la conexión a la base de datos que se utilizará para ejecutar la consulta SQL. | pandas.read_sql(sql, con) |
| index_col | None | Permite especificar una columna que debe ser utilizada como índice en el DataFrame resultante. | pandas.read_sql(sql, con, index_col=None) |
| coerce_float | True | Si se establece como True, intenta convertir los valores no numéricos en columnas numéricas a valores float. | pandas.read_sql(sql, con, coerce_float=True) |
| params | None | Permite pasar parámetros adicionales para la consulta SQL, generalmente cuando se utiliza una consulta parametrizada. | pandas.read_sql(sql, con, params=None) |
| parse_dates | None | Permite especificar qué columnas deben ser convertidas a formato de fecha durante la lectura. | pandas.read_sql(sql, con, parse_dates=None) |
| columns | None | Permite seleccionar un subconjunto de columnas que se desean leer de la base de datos. | pandas.read_sql(sql, con, columns=None) |
| chunksize | None | Si se establece, la función leerá el archivo en fragmentos del tamaño especificado, devolviendo un iterador. | pandas.read_sql(sql, con, chunksize=None) |
| dtype | None | Permite especificar el tipo de datos de las columnas a leer en el DataFrame resultante. | pandas.read_sql(sql, con, dtype=None) |
| sqlalchemy_schema | None | Permite especificar el esquema de SQLAlchemy que debe utilizarse para la consulta SQL. | pandas.read_sql(sql, con, sqlalchemy_schema=None) |
| conn | None | Se utiliza para pasar un objeto de conexión a la base de datos. | pandas.read_sql(sql, con, conn=None) |
| schema | None | Permite especificar el esquema en el que se encuentra la tabla o vista a consultar. | pandas.read_sql(sql, con, schema=None) |
| **kwargs |  | Permite pasar argumentos adicionales para personalizar el comportamiento de la función según sea necesario. | pandas.read_sql(sql, con, **kwargs) |


## to_sql

```python
df.to_sql(name, con, schema=None, if_exists='fail', index=True, 
                    index_label=None, chunksize=None, dtype=None, method=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| name | Obligatorio | Nombre de la tabla en la base de datos donde se almacenarán los datos del DataFrame. | df.to_sql(name='table_name', con=con) |
| con | Obligatorio | Objeto de conexión a la base de datos (puede ser una conexión de SQLAlchemy, sqlite3 u otras). | df.to_sql(name='table_name', con=con) |
| schema | None | Especifica el esquema de la base de datos donde se guardará la tabla. | df.to_sql(name='table_name', con=con, schema='schema_name') |
| if_exists | 'fail' | Controla el comportamiento si la tabla ya existe. Opciones: 'fail' (lanza un error), 'replace' (reemplaza la tabla) o 'append' (agrega los datos). | df.to_sql(name='table_name', con=con, if_exists='replace') |
| index | True | Controla si se escribe o no el índice del DataFrame en la tabla de la base de datos. | df.to_sql(name='table_name', con=con, index=False) |
| index_label | None | Especifica un nombre para la columna del índice en la tabla de la base de datos. | df.to_sql(name='table_name', con=con, index_label='id') |
| chunksize | None | Si se establece, divide los datos en fragmentos del tamaño especificado para escribirlos en la tabla en varias transacciones. | df.to_sql(name='table_name', con=con, chunksize=1000) |
| dtype | None | Permite especificar los tipos de datos de las columnas en la tabla de la base de datos, como un diccionario {columna: tipo}. | df.to_sql(name='table_name', con=con, dtype={'col1': Integer, 'col2': String}) |
| method | None | Permite especificar el método de inserción de datos, como 'multi' para optimizar la velocidad de escritura con múltiples valores. | df.to_sql(name='table_name', con=con, method='multi') |


## read_json

```python
df = pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=True, 
             convert_axes=None, convert_dates=True, keep_default_dates=True, 
             precise_float=False, date_unit=None, encoding='utf-8', 
             lines=False, chunksize=None, compression='infer', 
             nrows=None, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path_or_buf | None | Ruta o buffer desde el cual se leerá el archivo JSON. Puede ser una cadena, un objeto de archivo o un buffer. | pandas.read_json(path_or_buf=None) |
| orient | None | Especifica la orientación del JSON. Opciones: 'split', 'records', 'index', 'columns', 'values', 'table'. | pandas.read_json(path_or_buf, orient=None) |
| typ | 'frame' | Especifica el tipo de datos devueltos. Opciones: 'frame' (DataFrame) o 'series'. | pandas.read_json(path_or_buf, typ='frame') |
| dtype | True | Controla si se infiere automáticamente el tipo de datos de las columnas. | pandas.read_json(path_or_buf, dtype=True) |
| convert_axes | None | Indica si los ejes deben ser convertidos al tipo inferido automáticamente. | pandas.read_json(path_or_buf, convert_axes=None) |
| convert_dates | True | Convierte automáticamente cadenas que parezcan fechas a objetos datetime. | pandas.read_json(path_or_buf, convert_dates=True) |
| keep_default_dates | True | Si se establece en False, desactiva el comportamiento predeterminado de conversión automática de fechas. | pandas.read_json(path_or_buf, keep_default_dates=True) |
| precise_float | False | Si se establece en True, usa una conversión precisa para datos de punto flotante. | pandas.read_json(path_or_buf, precise_float=False) |
| date_unit | None | Unidad para interpretar las marcas de tiempo, como 'ms', 's'. | pandas.read_json(path_or_buf, date_unit=None) |
| encoding | 'utf-8' | Codificación del archivo JSON. | pandas.read_json(path_or_buf, encoding='utf-8') |
| lines | False | Si se establece en True, trata cada línea del archivo como un registro JSON separado. | pandas.read_json(path_or_buf, lines=False) |
| chunksize | None | Si se establece, devuelve un iterador con fragmentos del tamaño especificado. | pandas.read_json(path_or_buf, chunksize=None) |
| compression | 'infer' | Especifica el tipo de compresión del archivo JSON. Opciones: 'gzip', 'bz2', 'zip', 'xz', o 'infer' para deducirlo automáticamente. | pandas.read_json(path_or_buf, compression='infer') |
| nrows | None | Número máximo de filas a leer. | pandas.read_json(path_or_buf, nrows=None) |
| storage_options | None | Diccionario de opciones adicionales para el almacenamiento remoto, como autenticación en sistemas basados en URL. | pandas.read_json(path_or_buf, storage_options=None) |


## to_json

```python
df.to_json(path_or_buf=None, orient=None, date_format=None, 
                     double_precision=10, force_ascii=True, date_unit='ms', 
                     default_handler=None, lines=False, compression='infer', 
                     index=True, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path_or_buf | None | Ruta o buffer donde se guardará el archivo JSON. Si es None, el resultado se devuelve como una cadena JSON. | df.to_json(path_or_buf=None) |
| orient | None | Especifica el formato del JSON. Opciones: 'split', 'records', 'index', 'columns', 'values', 'table'. | df.to_json(path_or_buf, orient=None) |
| date_format | None | Formato de fecha para las columnas de tipo datetime. Opciones: 'epoch' o 'iso'. | df.to_json(path_or_buf, date_format=None) |
| double_precision | 10 | Precisión para los valores de punto flotante. | df.to_json(path_or_buf, double_precision=10) |
| force_ascii | True | Si se establece en True, todos los caracteres no ASCII se escapan en Unicode. | df.to_json(path_or_buf, force_ascii=True) |
| date_unit | 'ms' | Unidad de tiempo para las marcas temporales, como 's' (segundos), 'ms' (milisegundos), 'us' (microsegundos), 'ns' (nanosegundos). | df.to_json(path_or_buf, date_unit='ms') |
| default_handler | None | Función que convierte valores no serializables a objetos serializables. | df.to_json(path_or_buf, default_handler=None) |
| lines | False | Si es True, escribe una línea por registro en formato JSON, ideal para archivos grandes. | df.to_json(path_or_buf, lines=False) |
| compression | 'infer' | Especifica el tipo de compresión del archivo. Opciones: 'gzip', 'bz2', 'zip', 'xz', o 'infer'. | df.to_json(path_or_buf, compression='infer') |
| index | True | Si es True, incluye el índice del DataFrame en el archivo JSON. | df.to_json(path_or_buf, index=True) |
| storage_options | None | Diccionario con opciones adicionales para sistemas de almacenamiento remoto, como autenticación basada en URL. | df.to_json(path_or_buf, storage_options=None) |


## read_html

```python
df = pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, 
             skiprows=None, attrs=None, parse_dates=False, thousands=None, 
             encoding=None, decimal='.', converters=None, na_values=None, 
             keep_default_na=True, displayed_only=True, extract_links=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| io | Obligatorio | Ruta o contenido del archivo HTML que contiene las tablas. Puede ser una URL, archivo o cadena HTML. | df = pandas.read_html(io) |
| match | '.+' | Expresión regular para filtrar las tablas en el HTML según el contenido. | df = pandas.read_html(io, match='.+') |
| flavor | None | Especifica el motor para analizar las tablas. Opciones: 'bs4' (BeautifulSoup) o 'html5lib'. | df = pandas.read_html(io, flavor=None) |
| header | None | Fila o filas para usar como encabezados de las columnas. Si es None, se utiliza la primera fila. | df = pandas.read_html(io, header=None) |
| index_col | None | Columna o columnas que se utilizarán como índice del DataFrame. | df = pandas.read_html(io, index_col=None) |
| skiprows | None | Número de filas o lista de índices a omitir antes de procesar la tabla. | df = pandas.read_html(io, skiprows=None) |
| attrs | None | Filtro de atributos HTML para seleccionar tablas específicas (e.g., por clase o id). | df = pandas.read_html(io, attrs={'class': 'mi-tabla'}) |
| parse_dates | False | Si es True, intenta analizar columnas como fechas. | df = pandas.read_html(io, parse_dates=False) |
| thousands | None | Caracter que separa los miles (e.g., ',' o '.'). | df = pandas.read_html(io, thousands=None) |
| encoding | None | Codificación del archivo HTML. Útil para caracteres especiales. | df = pandas.read_html(io, encoding=None) |
| decimal | '.' | Caracter que representa el separador decimal. | df = pandas.read_html(io, decimal='.') |
| converters | None | Diccionario de funciones para convertir valores en columnas específicas. | df = pandas.read_html(io, converters=None) |
| na_values | None | Valores a considerar como NaN en las tablas. | df = pandas.read_html(io, na_values=None) |
| keep_default_na | True | Si es True, utiliza los valores predeterminados como NaN. Si es False, solo considera los valores especificados en na_values. | df = pandas.read_html(io, keep_default_na=True) |
| displayed_only | True | Si es True, solo considera las tablas visibles en el HTML. Si es False, también procesa tablas ocultas. | df = pandas.read_html(io, displayed_only=True) |
| extract_links | None | Especifica si se deben extraer enlaces HTML de las tablas. Opciones: 'all', 'body', 'header' o None. | df = pandas.read_html(io, extract_links=None) |


## to_html

```python
df = pandas.to_html(buf=None, columns=None, col_space=None, header=True, 
                     index=True, na_rep='NaN', formatters=None, float_format=None, 
                     sparsify=None, index_names=True, justify=None, max_rows=None, 
                     max_cols=None, show_dimensions=False, decimal='.', 
                     border=None, table_id=None, render_links=False, 
                     classes=None, escape=True, notebook=False)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| buf | None | Archivo, buffer o None. Si es None, se devuelve como cadena HTML. | df.to_html(buf='output.html') |
| columns | None | Lista de columnas a incluir en el HTML. Si es None, se incluyen todas. | df.to_html(columns=['col1', 'col2']) |
| col_space | None | Espacio (en pixeles) para cada columna. | df.to_html(col_space=50) |
| header | True | Si es True, incluye los nombres de las columnas como encabezados. | df.to_html(header=False) |
| index | True | Si es True, incluye el índice del DataFrame en la salida. | df.to_html(index=False) |
| na_rep | 'NaN' | Representación de valores faltantes en el HTML. | df.to_html(na_rep='') |
| formatters | None | Diccionario de funciones para formatear columnas específicas. | df.to_html(formatters={'col1': lambda x: f'{x:.2f}'}) |
| float_format | None | Formato para valores de punto flotante. | df.to_html(float_format='%.2f') |
| sparsify | None | Si es True, combina celdas en el índice para mejorar la presentación visual. | df.to_html(sparsify=True) |
| index_names | True | Si es True, incluye los nombres de los índices en la salida. | df.to_html(index_names=False) |
| justify | None | Alineación de texto: 'left', 'right', 'center'. | df.to_html(justify='center') |
| max_rows | None | Número máximo de filas a incluir. Si es None, se incluyen todas. | df.to_html(max_rows=10) |
| max_cols | None | Número máximo de columnas a incluir. Si es None, se incluyen todas. | df.to_html(max_cols=5) |
| show_dimensions | False | Si es True, muestra las dimensiones del DataFrame como comentario al final del HTML. | df.to_html(show_dimensions=True) |
| decimal | '.' | Separador decimal para valores numéricos. | df.to_html(decimal=',') |
| border | None | Espesor del borde de la tabla en pixeles. | df.to_html(border=1) |
| table_id | None | Valor del atributo id para la tabla HTML generada. | df.to_html(table_id='mi_tabla') |
| render_links | False | Si es True, convierte los valores de texto que parecen URLs en enlaces HTML. | df.to_html(render_links=True) |
| classes | None | Clase(s) CSS para la tabla. Puede ser una cadena o lista de cadenas. | df.to_html(classes='mi-clase') |
| escape | True | Si es True, escapa caracteres HTML especiales en los datos (e.g., <, >). | df.to_html(escape=False) |
| notebook | False | Si es True, utiliza el formato de estilo de cuaderno (notebook) en Jupyter. | df.to_html(notebook=True) |


## read_parquet

```python
pd.read_parquet(path, engine='auto', columns=None, use_nullable_dtypes=None, 
                filters=None, engine_options=None, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta al archivo Parquet o a un objeto con el archivo (e.g., URL, archivo local). | pd.read_parquet('data.parquet')
| engine | 'auto' | Motor utilizado para leer el archivo. Puede ser auto, 'pyarrow' o 'fastparquet'. | pd.read_parquet('data.parquet', engine='pyarrow')
| columns | None | Lista de columnas a leer. Si es None, se leen todas las columnas. | pd.read_parquet('data.parquet', columns=['col1', 'col2'])
| use_nullable_dtypes | None | Si es True, usa tipos de datos nulos. | pd.read_parquet('data.parquet', use_nullable_dtypes=True)
| filters | None | Filtros para leer solo un subconjunto de los datos. Debe ser una lista de tuplas, donde cada tupla representa un filtro. | pd.read_parquet('data.parquet', filters=[('col1', '=', 10)])
| engine_options | None | Opciones adicionales para el motor utilizado. | pd.read_parquet('data.parquet', engine_options={'use_legacy_dataset': True})
| storage_options | None | Opciones para especificar parámetros de almacenamiento (por ejemplo, para leer desde S3). | pd.read_parquet('s3://bucket/data.parquet', storage_options={'key': 'value'})


## to_parquet

```python
df.to_parquet(path, engine='auto', compression='snappy', 
                        index=True, partition_cols=None, 
                        ignore_index=False, 
                        filepath_or_buffer=None, 
                        partition_on=None, 
                        storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta al archivo Parquet donde se guardarán los datos. Puede ser un archivo local o un objeto con el archivo (e.g., URL). | df.to_parquet('data.parquet')
| engine | 'auto' | Motor utilizado para escribir el archivo. Puede ser auto, 'pyarrow' o 'fastparquet'. | df.to_parquet('data.parquet', engine='pyarrow')
| compression | 'snappy' | Método de compresión a utilizar. Puede ser snappy, gzip, brotli, lz4, o zstd. | df.to_parquet('data.parquet', compression='gzip')
| index | True | Si es True, incluye la columna del índice del DataFrame. | df.to_parquet('data.parquet', index=False)
| partition_cols | None | Lista de columnas sobre las cuales particionar el archivo Parquet. | df.to_parquet('data.parquet', partition_cols=['col1'])
| ignore_index | False | Si es True, no incluye el índice al escribir el archivo. | df.to_parquet('data.parquet', ignore_index=True)
| filepath_or_buffer | None	 | Puede especificar el archivo donde escribir el DataFrame (también puede ser una URL). | df.to_parquet('data.parquet', filepath_or_buffer='path')
| partition_on | None | Columnas sobre las cuales particionar el archivo, útil para almacenar en sistemas como S3. | df.to_parquet('s3://bucket/data.parquet', partition_on=['col1'])
| storage_options | None | Opciones para especificar parámetros de almacenamiento (por ejemplo, para escribir en S3). | df.to_parquet('s3://bucket/data.parquet', storage_options={'key': 'value'})


## read_feather

```python
df = pandas.read_feather(path, columns=None, use_nullable_dtypes=None, 
                storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta al archivo Feather que se leerá. Puede ser una ruta local o un objeto como una URL. | df = pandas.read_feather('data.feather') |
| columns | None | Lista de columnas a leer desde el archivo. Si no se especifica, se leen todas las columnas. | df = pandas.read_feather('data.feather', columns=['col1', 'col2']) |
| use_nullable_dtypes | None | Si es True, usa tipos de datos nulos de pandas para columnas con datos nulos. | df = pandas.read_feather('data.feather', use_nullable_dtypes=True) |
| storage_options | None | Opciones para especificar parámetros de almacenamiento (como para leer desde sistemas como S3). | df = pandas.read_feather('s3://bucket/data.feather', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## to_feather

```python
df.to_feather(path, index=True, compression=None, 
                        use_nullable_dtypes=None, 
                        storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta donde se guardará el archivo Feather. Puede ser una ruta local o un objeto como una URL. | df.to_feather('data.feather') |
| index | True | Si es True, incluye el índice del DataFrame en el archivo. Si es False, no se incluye. | df.to_feather('data.feather', index=False) |
| compression | None | Método de compresión a usar, por ejemplo 'snappy', 'gzip', etc. Si no se especifica, no se aplica compresión. | df.to_feather('data.feather', compression='snappy') |
| use_nullable_dtypes | None | Si es True, usa tipos de datos nulos de pandas para columnas con datos nulos. | df.to_feather('data.feather', use_nullable_dtypes=True) |
| storage_options | None | Opciones para especificar parámetros de almacenamiento (como para escribir en sistemas como S3). | df.to_feather('s3://bucket/data.feather', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## read_orc

```python
df = pandas.read_orc(path, columns=None, engine='pyarrow', 
            use_nullable_dtypes=None, 
            storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta del archivo ORC a leer. Puede ser una ruta local o un objeto como una URL. | df = pandas.read_orc('data.orc') |
| columns |  | None | Lista de columnas que se desea leer del archivo ORC. Si se deja como None, se leen todas las columnas. | df = pandas.read_orc('data.orc', columns=['col1', 'col2']) |
| engine | 'pyarrow' | Motor a usar para leer el archivo ORC. Puede ser 'pyarrow' o 'cudf'. | df = pandas.read_orc('data.orc', engine='pyarrow') |
| use_nullable_dtypes | None | Si es True, usa tipos de datos nulos de pandas para columnas con valores nulos. | df = pandas.read_orc('data.orc', use_nullable_dtypes=True) |
| storage_options | None | Opciones adicionales para especificar parámetros de almacenamiento (como para leer desde un sistema en la nube). | df = pandas.read_orc('s3://bucket/data.orc', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## read_sas

```python
df = pandas.read_sas(filepath_or_buffer, format='sas7bdat', encoding=None, index=None, 
            chunksize=None, iterator=False, compression='infer', 
            usecols=None, skiprows=None, skipfooter=0, 
            storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| filepath_or_buffer | Obligatorio | Ruta del archivo SAS a leer, puede ser un archivo local o una URL. | df = pandas.read_sas('data.sas7bdat') |
| format | 'sas7bdat' | El formato del archivo SAS a leer. Los valores posibles son 'sas7bdat' y 'xport'. | df = pandas.read_sas('data.sas7bdat', format='sas7bdat') |
| encoding | None | Codificación del archivo SAS. Si se deja como None, se usa la codificación predeterminada. | df = pandas.read_sas('data.sas7bdat', encoding='utf-8') |
| index | None | Si se proporciona, indica cuál columna usar como índice al leer los datos. | df = pandas.read_sas('data.sas7bdat', index='column_name') |
| chunksize | None | Tamaño de los bloques de datos a leer. Si se proporciona, devuelve un iterador. | df = pandas.read_sas('data.sas7bdat', chunksize=1000) |
| iterator | False | Si se establece en True, devuelve un iterador para leer el archivo en bloques. | df = pandas.read_sas('data.sas7bdat', iterator=True) |
| | compression | 'infer' | Tipo de compresión. Puede ser 'infer', 'gzip', 'bz2', 'zip', 'xz', o None. | df = pandas.read_sas('data.sas7bdat', compression='gzip') |
| usecols | None | Lista de columnas a leer. Si no se proporciona, se leen todas las columnas. | df = pandas.read_sas('data.sas7bdat', usecols=['col1', 'col2']) |
| skiprows | None | Número de filas a saltar al inicio del archivo. | df = pandas.read_sas('data.sas7bdat', skiprows=5) |
| skipfooter | 0 | Número de filas a omitir al final del archivo. | df = pandas.read_sas('data.sas7bdat', skipfooter=2) |
| storage_options | None | Opciones de almacenamiento, como credenciales para leer desde un sistema en la nube. | df = pandas.read_sas('s3://bucket/data.sas7bdat', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## read_stata

```python
df = pandas.read_stata(filepath_or_buffer, convert_dates=True, convert_categoricals=True, 
              index_col=None, convert_missing=True, encoding=None, 
              chunksize=None, iterator=False, usecols=None, 
              skiprows=None, skipfooter=0, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| filepath_or_buffer | Obligatorio	Ruta del archivo STATA a leer. Puede ser un archivo local o una URL. | df = pandas.read_stata('data.dta') |
| convert_dates | True | Si es True, convierte las columnas con fechas en objetos datetime. | df = pandas.read_stata('data.dta', convert_dates=False) |
| convert_categoricals | True | Si es True, convierte las variables categóricas a tipo category de pandas. | df = pandas.read_stata('data.dta', convert_categoricals=False) |
| index_col | None | Si se proporciona, utiliza esta columna como índice. | df = pandas.read_stata('data.dta', index_col='id') |
| convert_missing | True | Si es True, convierte los valores de "missing" (nulos) en valores NaN en pandas. | df = pandas.read_stata('data.dta', convert_missing=False) |
| encoding | None | Codificación del archivo STATA. Si se deja como None, se usa la codificación predeterminada. | df = pandas.read_stata('data.dta', encoding='utf-8') |
| chunksize | None | Tamaño de los bloques de datos a leer. Si se proporciona, devuelve un iterador. | df = pandas.read_stata('data.dta', chunksize=1000) |
| iterator | False | Si se establece en True, devuelve un iterador para leer el archivo en bloques. | df = pandas.read_stata('data.dta', iterator=True) |
| usecols | None | Lista de columnas a leer. Si no se proporciona, se leen todas las columnas. | df = pandas.read_stata('data.dta', usecols=['col1', 'col2']) |
| skiprows | None | Número de filas a saltar al inicio del archivo. | df = pandas.read_stata('data.dta', skiprows=5) |
| skipfooter | 0 | Número de filas a omitir al final del archivo. | df = pandas.read_stata('data.dta', skipfooter=2) |
| storage_options | None | Opciones de almacenamiento, como credenciales para leer desde un sistema en la nube. | df = pandas.read_stata('s3://bucket/data.dta', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## read_pickle

```python
df = pandas.read_pickle(filepath_or_buffer, compression='infer', 
               storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| filepath_or_buffer | Obligatorio | Ruta del archivo pickle a leer. Puede ser un archivo local o una URL. | df = pandas.read_pickle('data.pkl') |
| compression | 'infer' | Método de compresión, puede ser 'infer', 'gzip', 'bz2', 'zip', 'xz', 'lzma', o None. 'infer' infiere automáticamente el tipo de compresión a partir de la extensión del archivo. | df = pandas.read_pickle('data.pkl', compression='gzip') |
| storage_options | None | Opciones de almacenamiento, como credenciales para leer desde un sistema en la nube. | df = pandas.read_pickle('s3://bucket/data.pkl', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## to_pickle

```python
df.to_pickle(path, compression='infer', 
                       protocol=4, 
                       storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| path | Obligatorio | Ruta donde se guardará el archivo pickle. Puede ser un archivo local o una URL. | df.to_pickle('data.pkl') |
| compression | 'infer' | Método de compresión, puede ser 'infer', 'gzip', 'bz2', 'zip', 'xz', 'lzma', o None. 'infer' infiere automáticamente el tipo de compresión a partir de la extensión del archivo. | df.to_pickle('data.pkl', compression='gzip') |
| protocol | 4 | Nivel de protocolo de pickle, que controla la versión de serialización del objeto. Un valor más alto puede mejorar la eficiencia. El valor predeterminado es 4. | df.to_pickle('data.pkl', protocol=5) |
| storage_options | None | Opciones de almacenamiento, como credenciales para guardar el archivo en un sistema en la nube. | df.to_pickle('s3://bucket/data.pkl', storage_options={'key': 'my-access-key', 'secret': 'my-secret'}) |


## read_table

```python
df = pandas.read_table(filepath_or_buffer, sep='\t', delimiter=None, header='infer', 
              names=None, index_col=None, usecols=None, engine='python', 
              skiprows=None, skipfooter=0, na_values=None, 
              parse_dates=False, date_parser=None, thousands=None, 
              decimal='.', comment=None, encoding=None, 
              encoding_errors='strict', dtype=None, 
              converters=None, true_values=None, false_values=None, 
              skipinitialspace=False, nrows=None, 
              na_filter=True, verbose=False, 
              delimiter='none', 
              storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| filepath_or_buffer | Obligatorio | Ruta al archivo a leer. Puede ser una ruta de archivo local, una URL, o un objeto similar a un archivo. | df = pandas.read_table('data.txt') |
| sep | '\t' | Separador de campos (por defecto, tabulación \t para archivos TSV). | df = pandas.read_table('data.txt', sep=',') |
| delimiter | None | Un delimitador alternativo para sep. No se utiliza si sep está especificado. | df = pandas.read_table('data.txt', delimiter=';') |
| header | 'infer' | Fila a usar como nombres de columnas. 'infer' intenta detectar automáticamente la fila de encabezado. | df = pandas.read_table('data.txt', header=0) |
| names | None | Lista de nombres de columnas si no se encuentran en el archivo o si deseas reemplazarlos. | df = pandas.read_table('data.txt', names=['A', 'B']) |
| index_col | None | Columna(s) para usar como índice (por defecto no se usa ningún índice). | df = pandas.read_table('data.txt', index_col=0) |
| usecols | None | Lista de columnas a leer. Si no se especifica, se leen todas las columnas. | df = pandas.read_table('data.txt', usecols=[0, 2]) |
| engine | 'python' | Motor para el procesamiento, puede ser 'python' o 'c' (C parser, más rápido). | df = pandas.read_table('data.txt', engine='c') |
| skiprows | None | Número de filas a saltar al principio del archivo. | df = pandas.read_table('data.txt', skiprows=1) |
| skipfooter | 0 | Número de filas a saltar al final del archivo. | df = pandas.read_table('data.txt', skipfooter=1) |
| na_values | None | Valores adicionales que se deben tratar como NaN. | df = pandas.read_table('data.txt', na_values=['NA']) |
| parse_dates | False | Si se debe intentar convertir las columnas de fecha a objetos de tipo datetime. | df = pandas.read_table('data.txt', parse_dates=True) |
| date_parser | None | Función de análisis de fechas personalizada. | df = pandas.read_table('data.txt', date_parser=my_parser) |
| thousands | None | El carácter a utilizar como separador de miles. | df = pandas.read_table('data.txt', thousands=',') |
| decimal | '.' | El carácter a usar como separador decimal (por defecto es el punto .). | df = pandas.read_table('data.txt', decimal=',') |
| comment | None | Carácter que indica el inicio de un comentario en una fila. | df = pandas.read_table('data.txt', comment='#') |
| encoding | None | Codificación del archivo, como 'utf-8', 'latin1', etc. | df = pandas.read_table('data.txt', encoding='utf-8') |
| encoding_errors | 'strict' | Estrategia para manejar errores de codificación. | df = pandas.read_table('data.txt', encoding_errors='ignore') |
| dtype | None | Tipo de datos para las columnas. | df = pandas.read_table('data.txt', dtype={'col1': float}) |
| converters | None | Diccionario de funciones para convertir las columnas. | df = pandas.read_table('data.txt', converters={'col1': my_converter}) |
| true_values | None | Valores que se deben interpretar como True al leer el archivo. | df = pandas.read_table('data.txt', true_values=['yes']) |
| false_values | None | Valores que se deben interpretar como False al leer el archivo. | df = pandas.read_table('data.txt', false_values=['no']) |
| skipinitialspace | False | Si se deben ignorar los espacios iniciales después del delimitador. | df = pandas.read_table('data.txt', skipinitialspace=True) |
| nrows | None | Número máximo de filas a leer. | df = pandas.read_table('data.txt', nrows=100) |
| na_filter | True | Si se deben buscar valores NaN en las columnas del archivo. | df = pandas.read_table('data.txt', na_filter=False) |
| verbose | False | Si se deben mostrar mensajes adicionales sobre el análisis del archivo. | df = pandas.read_table('data.txt', verbose=True) |
| delimiter | 'none' | Este parámetro es redundante, ya que se establece sep para el delimitador principal. | df = pandas.read_table('data.txt', delimiter=';') |
| storage_options | None | Opciones de almacenamiento, como credenciales para acceder a archivos en la nube. | df = pandas.read_table('s3://bucket/data.txt', storage_options={'key': 'my-access-key'}) |


## read_clipboard

```python
df = pandas.read_clipboard(sep=None, header='infer', names=None, 
                  index_col=None, usecols=None, engine='python', 
                  skiprows=None, skipfooter=0, na_values=None, 
                  parse_dates=False, date_parser=None, thousands=None, 
                  decimal='.', comment=None, encoding=None, 
                  encoding_errors='strict', dtype=None, 
                  converters=None, true_values=None, false_values=None, 
                  skipinitialspace=False, nrows=None, 
                  na_filter=True, verbose=False, 
                  storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| sep | None | Separador de columnas. Si no se especifica, se detecta automáticamente. | df = pandas.read_clipboard(sep=';') |
| header | 'infer' | Fila que se utiliza como los nombres de las columnas. 'infer' intenta detectar automáticamente la fila de encabezado. | df = pandas.read_clipboard(header=0) |
| names | None | Lista de nombres de columnas si no se encuentran en el portapapeles o si deseas reemplazarlos. | df = pandas.read_clipboard(names=['A', 'B']) |
| index_col | None | Columna(s) que se utilizarán como índice. Si no se especifica, se usa un índice por defecto. | df = pandas.read_clipboard(index_col=0) |
| usecols | None | Lista de columnas a leer. Si no se especifica, se leen todas las columnas. | df = pandas.read_clipboard(usecols=[0, 1]) |
| engine | 'python' | Motor para procesar el contenido (puede ser 'python' o 'c' para el motor en C, más rápido). | df = pandas.read_clipboard(engine='python') |
| skiprows | None | Número de filas a saltar desde el principio del contenido del portapapeles. | df = pandas.read_clipboard(skiprows=2) |
| skipfooter | 0 | Número de filas a saltar desde el final del contenido del portapapeles. | df = pandas.read_clipboard(skipfooter=1) |
| na_values | None | Valores adicionales a tratar como NaN. | df = pandas.read_clipboard(na_values=['NA']) |
| parse_dates | False | Si se deben analizar las columnas de fecha como objetos datetime. | df = pandas.read_clipboard(parse_dates=True) |
| date_parser | None | Función personalizada para analizar fechas. | df = pandas.read_clipboard(date_parser=my_parser) |
| thousands | None | Carácter que se utiliza como separador de miles. | df = pandas.read_clipboard(thousands=',') |
| decimal | '.' | Carácter que se utiliza como separador decimal. | df = pandas.read_clipboard(decimal=',') |
| comment | None | Carácter que indica el inicio de un comentario. | df = pandas.read_clipboard(comment='#') |
| encoding | None | Codificación del texto en el portapapeles (por ejemplo, 'utf-8'). | df = pandas.read_clipboard(encoding='utf-8') |
| encoding_errors | 'strict' | Estrategia para manejar errores de codificación, como 'ignore' o 'replace'. | df = pandas.read_clipboard(encoding_errors='ignore') |
| dtype | None | Tipo de datos para las columnas. | df = pandas.read_clipboard(dtype={'col1': float}) |
| converters | None | Diccionario de funciones para convertir las columnas. | df = pandas.read_clipboard(converters={'col1': my_converter}) |
| true_values | None | Valores que se deben interpretar como True al leer los datos. | df = pandas.read_clipboard(true_values=['yes']) |
| false_values | None | Valores que se deben interpretar como False al leer los datos. | df = pandas.read_clipboard(false_values=['no']) |
| skipinitialspace | False | Si se deben ignorar los espacios iniciales después de los delimitadores. | df = pandas.read_clipboard(skipinitialspace=True) |
| nrows | None | Número máximo de filas a leer. | df = pandas.read_clipboard(nrows=100) |
| na_filter | True | Si se deben detectar valores NaN. | df = pandas.read_clipboard(na_filter=False) |
| verbose | False | Si se deben mostrar mensajes adicionales sobre el análisis del archivo. | df = pandas.read_clipboard(verbose=True) |
| storage_options | None | Opciones adicionales para el almacenamiento, como credenciales para acceder a archivos en la nube. | df = pandas.read_clipboard(storage_options={'key': 'my-access-key'}) |

### miin
```python
print(df["A"].min())  # Mínimo de la columna "A"
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |

### max
```python
print(df["A"].max())  # Máximo de la columna "A"
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |

### sort_values

```python
df = df.sort_values(by="fecha_ini_log", ascending=True)  # ascendente

df_sorted = df.sort_values(by="fecha_ini_log", ascending=False) # descendente

df_sorted = df.sort_values(by=["fecha_ini_log", "interval_start"], ascending=[True, False]) # varias columnas
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |

### query

```python
df_filtrado = df.query("interval_start == '00:00:00'")

df_filtrado = df.query("interval_start == '00:00:00' and date_start == '2024-01-01'")

df_filtrado = df.query("interval_start == '00:00:00' or interval_start == '01:00:00'")

```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
