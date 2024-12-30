# Pandas

## Lista funciones de Pandas
|Función|Uso|
|-------|---|
| [DataFrame](#DataFrame) | Generar un DataFrame. |
| [Series](#Series) | Se utiliza para crear una Serie en Pandas, que es una estructura de datos unidimensional similar a una columna de una tabla o un arreglo unidimensional con etiquetas (índices) |
| [read_csv](#read_csv) | Leer archivos CSV y generar un DataFrame en base a ellos. |
| [to_csv](#to_csv) | Exportar un DataFrame en un archivo CSV. |
| [read_excel](#read_excel)  | Leer archivos XLSX y generar un DataFrame en base a ellos. |
| [to_excel](#to_excel) |  |
| [read_sql](#read_sql) |  |
| [to_sql](#to_sql) |  |
| [read_json](#read_json) |  |
| [to_json](#to_json) |  |
| [read_html](#read_html) |  |
| [read_parquet](#read_parquet) |  |
| [to_parquet](#to_parquet) |  |
| [read_feather](#read_feather) |  |
| [to_feather](#to_feather) |  |
| [read_orc](#read_orc) |  |
| [read_sas](#read_sas) |  |
| [read_stata](#read_stata) |  |
| [read_pickle](#read_pickle) |  |
| [to_pickle](#to_pickle) |  |
| [read_table](#) |  |
| [to_html](#to_html) |  |
| [read_clipboard](#read_clipboard) |  |
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
| [sort_values](#sort_values) |  |
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
| [](#) |  |

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
| path_or_buffer | Obligatorio / 'archivo.csv' | Este parametro es fundamental, en el se asigna la ruta del archivo CSV que se leerá. | pd.read_csv(path_or_buffer) | 
| sep | ',' | Este parametro recibe el delimitador que tiene el archivo CSV, si no se recibe este parametro, asignara una coma por defecto. | pd.read_csv(path_or_buffer, sep=';') | 
| na_rep | '' | Se utiliza para especificar qué valor debe reemplazar los valores NaN (Not a Number) o None cuando se exporta un DataFrame a un archivo CSV. | pd.read_csv(path_or_buffer, na_rep='NULL') | 
| float_format | None | Se utiliza para especificar el formato de los números de punto flotante (floats) cuando se exporta un DataFrame a un archivo CSV. | pd.read_csv(path_or_buffer, float_format='%.2f') | 
| columns | None | Se utiliza para especificar un subconjunto de columnas que deseas exportar al archivo CSV. |
| header | True |
| index | True |
| index_label | None |
| mode | 'w' |
| encoding | None |
| compression | 'infer' |
| quoting | None |
| quotechar | '"' |
| line_terminator | None |
| chunksize | None |
| date_format | None |
| doublequote | True |
| escapechar | None |
| decimal | '.' |
| errors | 'strict' |
| storage_options | None |

## read_excel

```python
pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, 
                  squeeze=None, dtype=None, engine=None, converters=None, 
                  true_values=None, false_values=None, skiprows=None, nrows=None, 
                  na_values=None, keep_default_na=True, na_filter=True, verbose=False, 
                  parse_dates=False, date_parser=None, thousands=None, decimal='.', 
                  comment=None, skipfooter=0, storage_options=None)
```

| Clave | Default | Función | Ejemplo Uso |
| ----- | ------- | ------- | ----------- |
| io |  Obligatorio / 'archivo.csv' | Este parametro es fundamental, en el se asigna la ruta del archivo CSV que se leerá. | pd.read_excel(io) |
| sheet_name | 0 |  | pd.read_excel(io, sheet_name=0) |
| header | 0 |  | pd.read_excel(io, header=0) |
| names | None |  | pd.read_excel(io, names=None) |
| index_col | None |  | pd.read_excel(io, index_col=None) |
| usecols | None |  | pd.read_excel(io, usecols=None) |
| squeeze | None |  | pd.read_excel(io, squeeze=None) |
| dtype | None |  | pd.read_excel(io, dtype=None) |
| engine | None |  | pd.read_excel(io, engine=None) |
| converters | None |  | pd.read_excel(io, converters=None) |
| true_values | None |  | pd.read_excel(io, true_values=None) |
| false_values | None |  | pd.read_excel(io, false_values=None) |
| skiprows | None |  | pd.read_excel(io, skiprows=None) |
| nrows | None |  | pd.read_excel(io, nrows=None) |
| na_values | None |  | pd.read_excel(io, na_values=None) |
| keep_default_na | True |  | pd.read_excel(io, keep_default_na=True) |
| na_filter | True |  | pd.read_excel(io, na_filter=True) |
| verbose | False |  | pd.read_excel(io, verbose=False) |
| parse_dates | False |  | pd.read_excel(io, parse_dates=False) |
| date_parser | None |  | pd.read_excel(io, date_parser=None) |
| thousands | None |  | pd.read_excel(io, thousand=None) |
| decimal | '.' |  | pd.read_excel(io, decimal='.') |
| comment | None |  | pd.read_excel(io, comment=None) |
| skipfooter | 0 |  | pd.read_excel(io, skipfooter=None) |
| storage_options | None |  | pd.read_excel(io, storage_options=None) |
|  |  |  |  |