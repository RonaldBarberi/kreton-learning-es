# Apache Nifi

Cliente-Web ---> Servidor-Web ---> Integración (Apache Nifi).


### ¿Qué es?
Apache NiFi es una herramienta de integración y automatización de flujos de datos en tiempo real, diseñada para mover, transformar y gestionar datos entre diferentes sistemas de forma sencilla y visual.

### ¿Para qué sirve?
Integración de datos: Conecta múltiples fuentes (bases de datos, APIs, archivos, etc.) y destinos sin necesidad de escribir código.
Procesamiento en tiempo real: Permite transformar, filtrar y enrutar datos en el momento en que se reciben.
Automatización: Facilita la creación de flujos de trabajo automatizados para mover datos de un lugar a otro.
Escalabilidad y monitorización: Es capaz de manejar grandes volúmenes de datos y ofrece herramientas para monitorear los flujos.

### Usos comunes:
Migración de datos entre sistemas.
Ingesta de datos en plataformas de Big Data.
Procesamiento ETL (extraer, transformar y cargar).
Integración en arquitecturas de streaming (como Kafka).
Es ideal para empresas que necesitan gestionar grandes cantidades de datos de forma eficiente y centralizada.


FlowFile = registro de datos
Content Claim = contenido (datos del fichero)

Se interactua con procesadores a través de un flujo de trabajo

---

## Procesadores

### Categorías de los procesos:

1. Ingesta de Datos: Aquellos que traen los datos al flujo.
2. Enrutamiento: Encargado de dirigir los FlowFiles a los diferentes procesadores o flujos de información.
3. Procesadores Bases de Datos: Seleccionar, insertar datos, perepara y/o ejecutar declaraciones SQL desde cualquier base dedatos.
4. Procesadores de interacción con el sistema:  Se utiliza para ejecutar procesos o comando es cualquier sistema operativo (Windows, Linux).
5. Procesadores de Transformación de Datos: Capaces de alterar el contendio de los FlowFiles.
6. Procesadores de Evío de Datos: Estos son los responsables de almacenar y envíar los datos al servidor de destino.
7. Procesadores de Division y Agregación: Se utilizan para dividir y funcionar el contenido existente de un FlowFile

### Estados de los procesadores.
1. Parado: Significa que el procesador **no** está en uso.
2. Ejecutandose: Significa que el procesador está activo y realizando su trabajo.
3. Advertencia: Este estado indica que el procesador tiene una configuración que requiere ser revisada o completada.
4. Deshabilitado: Cuando un procesador se encuentra deshabilitado no puedes iniciado ni configurado.

![alt text](image.png)

Encabezado

- Configure Processor | AttributeRollingWindow 1.21.0
Indica que estás configurando un procesador llamado AttributeRollingWindow en la versión 1.21.0.

- Invalid (Inválido)
Hay un indicador que señala que el procesador no es válido. Esto podría deberse a una configuración incompleta o incorrecta.

Secciones Principales
1. Pestañas Disponibles

   - Settings (Configuración) (pestaña activa en la imagen).
   - Scheduling (Programación).
   - Properties (Propiedades).
   - Relationships (Relaciones).
   - Comments (Comentarios).

2. Configuraciones en la pestaña "Settings"
   - Name (Nombre): AttributeRollingWindow. Es el nombre asignado al procesador.
   - Enabled (Habilitado): Hay una casilla de verificación marcada, lo que indica que el procesador está activado.
   - Id: 1ba506f4-0188-1000-d00c-4d0c19705e63: Es el identificador único del procesador en NiFi.
   - Type (Tipo): AttributeRollingWindow 1.21.0: Muestra el tipo y la versión del procesador.
   - Bundle: org.apache.nifi - nifi-stateful-analysis-nar: Indica el paquete (bundle) del cual proviene este procesador, en este caso, un módulo de análisis con estado de Apache NiFi.
   - Penalty Duration (Duración de penalización): 30 sec: Define cuánto tiempo un flujo de datos será penalizado si ocurre un error. En este caso, es de 30 segundos.
   - Yield Duration (Duración de espera): 1 sec: Si el procesador no puede procesar datos, esperará 1 segundo antes de intentarlo de nuevo.
   - Bulletin Level (Nivel de boletín): WARN: Define el nivel de registros (logs) que generará este procesador. En este caso, WARN significa que se registrarán advertencias y errores.

Botones de Acción
   - CANCEL (Cancelar): Para cerrar la ventana sin aplicar cambios.
   - APPLY (Aplicar): Para guardar los cambios realizados en la configuración del procesador.

---

## Colas

### ¿Qué son?
En Apache NiFi, una cola es una estructura de almacenamiento temporal donde los FlowFiles (unidades de datos en NiFi) esperan antes de ser procesados por el siguiente componente del flujo de datos.

🔹 Concepto de Cola en NiFi
Las colas conectan dos procesadores y permiten gestionar el flujo de datos entre ellos. Un procesador genera datos y los coloca en una cola, mientras que otro procesador los consume para su siguiente transformación o transferencia.

Ejemplo visual en NiFi:
📤 Processor A → 🗃️ Cola → 📥 Processor B

---

Expresion Lenguage