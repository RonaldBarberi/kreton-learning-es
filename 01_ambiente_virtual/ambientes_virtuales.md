# Ambientes virtuales.

### Nota
Si gustas tener está información no solo en manera de lectura si no, un video practico extenso, corto, o simplemente un post más resumido, puedes encontrarlo en las siguientes fuentes.

- TikTok: 
- YouTobe:
- Instragram: 

Eso sería todo, agradezco le pudieses brindar una estrellita a este repositorio, ¡Gracias! 

## Ìndice:
- [¿Qué es un ambiente virtual?](#que-es-un-ambiente-virtual)
- [¿Requisitos para crear un entorno?](#requisitos-para-crear-un-entorno)
- [¿Cómo creo un entorno virtual?](#cómo-creo-un-entorno-virtual)
- [¿Cómo instalo librerias dentro de mi entorno?](#instalación-de-librerías)
- [Créditos](#créditos)

## Sección Noob

### Que es un ambiente virtual

Un ambiente virtual en Python es un entorno aislado a nuestra vesión de Python local, es decir, que es un ambiente donde pueden estar únicamente las dependencias necesarías para un proyecto, lo cual es totalmente útil cuando trabajamos un proyecto en conjunto, ya que con ello evitaremos problemas de versionamiento y tendremos un entorno más acorde con las necesidades del proyecto.

Tengamos en cuenta, que los ambientes virtuales se consideran únicamente para el manejo de las librerías especificas de tú proyecto. Si requieres encapsular todas las dependencias de tú aplicación (desarrollo), utilizar **DOCKER**, esta herramienta fue construida fundamental para estos escenarios, y por si te lo preguntas, sí, dentro de un contenedor de docer, puedes generar un ambiente virtual.

## Sección Junior

### Requisitos para crear un entorno.
1. Conocer la versión de Python que utilizas o validar que la versión para el proyecto se encuentre.
    ```bash
    python --version
    ```

### Cómo creo un entorno virtual.
Pudes crearlo se la siguiente forma:

Pasos generales:
1. Navega al directorio en donde crearás tú erntorno virtual.
    ```bash
    cd directorio/donde/esta/tu/proyecto
    ``` 

Pasos especificos dependiendo el sistema operativo a usar:
- Linux
    ```bash
    # Crear el entorno virtual. (Con la versión especifica, ejem: 3.10.10).
    python3.10 -m venv nombreEntorno

    # Iniciar el entorno virtual.
    source nombreEntorno/bin/activate

    # Validar si está activo el entorno (También se puede validar a simple vista viendo el nombre del entorno entre parentensis).
    which python

    # Salir del entorno virtual.
    deactivate
    ```

- Windows
    ```bash
    # Crear el entorno virtual. (Con la versión especifica, ejem: 3.10.10).
    python3.10 -m venv nombreEntorno

    # Iniciar el entorno virtual.
    nombreEntorno/Scripts/activate

    # Validar si está activo el entorno (También se puede validar a simple vista viendo el nombre del entorno entre parentensis).
    where python

    # Salir del entorno virtual.
    deactivate
    ```
- Mac
    ```bash
    # Crear el entorno virtual. (Con la versión especifica, ejem: 3.10.10).
    python3.10 -m venv nombreEntorno

    # Iniciar el entorno virtual.
    source nombreEntorno/bin/activate

    # Validar si está activo el entorno (También se puede validar a simple vista viendo el nombre del entorno entre parentensis).
    which python

    # Salir del entorno virtual.
    deactivate
    ```

Resultado final.

![alt text](./data/img_entorno_creado.png)

### Instalación de librerías.
En este paso debes contar con el requirements.txt, el cual traera las librerías necesarías así como su versión especifica para que se mantenga exactamente el flujo del proceso.

Ejemplo
```txt
mysql-connector-python==8.1.0
mysqlclient==2.2.4
numpy==1.24.2
openpyxl==3.1.2
PyAutoGUI==0.9.54
PyMySQL==1.1.0
scikit-learn==1.3.2
urllib3==1.26.15
psutil==5.9.6
pyperclip==1.8.2
Pillow==9.5.0
pywin32==306
unidecode==1.3.8
urllib3==1.26.15
sqlalchemy==2.0.27
pandas==2.2.1
tqdm==4.66.5
selenium==4.15.2
requests==2.28.2
ttkthemes==3.2.2
```
Cuando ya tenemos el requirements.txt procedemos con la instalación de las librerías dentro del archivo. Esto se realizá de la siguiente forma:

```bash
# Navegamos a la carpeta en donde se encuentra el archivo requirements.txt 
cd ruta/donde/esta/requirements

# Comando para la instalación de las librerías dentro del archivo.
pip install -r requirements.txt
```

Conclusión

- Junior: Se centra en los pasos básicos para crear y usar un entorno virtual, pero puede carecer de una comprensión profunda y de la capacidad para resolver problemas complejos.

- Senior: Tiene una comprensión integral del concepto, aplica buenas prácticas, resuelve problemas eficientemente, y garantiza la colaboración y reproducibilidad en el equipo.

### Créditos:
- Documentación oficial de Python: https://docs.python.org/3/
- Stack Overflow: https://stackoverflow.com/
- Guias PEP8: https://pep8.org/
