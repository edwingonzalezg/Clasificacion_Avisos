# Infraestructura

Para desarrollar un proyecto de ciencia de datos es importante tener una buena infraestructura, que incluya tanto los datos como las herramientas que se utilizarán para trabajar con ella.

## Configuración y gestión de Docker/kubernetes.

Debido a que este tema aún no lo hemos abordado en el desarrollo del diplomado, dejaremos abierta la opción de utilizar Docker si nos facilita el trabajo de despliegue.

## Configuración basada en el servidor.

Para desarrollar este proyecto de ciencia de datos, es necesario seleccionar los recursos mínimos del sistema que se van a requerir para ejecutar las herramientas y librerías que se van a utilizar durante su desarrollo.

Teniendo en cuenta que los requisitos mínimos dependen de factores como el tamaño y la complejidad de los datos, las herramientas y librerías a utilizar y el nivel de rendimiento que se requiere, inicialmente contar un sistema que tenga los siguientes requerimientos:

* 4 Gb de memoria RAM
*	Procesador de cuatro núcleos para ejecutar las herramientas y librerías necesarias
*	5 Gb de espacio en disco duro
*	GPU con 8 Gb de memoria.

Una vez seleccionados los recursos mínimos del sistema, se va a enumerar a continuación los requerimientos a nivel de software para configurar el servidor de desarrollo.  Para ello se va a utilizar lo siguiente:

*	Subsistema de Linux para Windows denominado WSL 
*	Sistema operativo Linux con la distribución Debian

## Configuración del entorno.

Para este proyecto, utilizaremos:
**GIT** para realizar el control del código.  Lo configuraremos como se muestra a continuación:

1.	Instalaremos GIT en la distribución Debian de Linux mediante el comando **`sudo apt install git`**
2.	Realizamos la configuración inicial agregando el nombre de usuario y el email con los comandos **`git config --global user.name "<<Nombre>>`** y **`git config --global user.email "<<Email>>`**.
3.	Configuramos el comportamiento de los saltos de línea de acuerdo a nuestro sistema operativo utilizando el comando **`git config --global core.autocrlf input`**
4.	Una vez instalado GIT, utilizamos el comando **`git init`** para inicializar el nuevo repositorio en el directorio destinado para tal fin.
5.	Utilizamos el comando **`git add`** para ir agregando los archivos que deseamos incluir en el repositorio.
6.	Después de haber agregado todos los archivos que deseamos incluir en el repositorio, utilizamos el comando **`git commit <<Mensaje con los cambios realizados>>`** para llevar una correcta trazabilidad de los cambios.
7.	Para almacenar y compartir el repositorio en GitHub, utilizamos el comando **`git remote add <<URL del sitio>>`** para agregar el repositorio remoto al repositorio local y luego, utilizando el comando **`git push <<Nombre del repositorio>>`**, enviaremos los cambios del repositorio local al repositorio remoto
POETRY para gestionar las dependencias y paquetes necesarios.  Para configurar el entorno, vamos a seguir los siguientes pasos:
  
1.	Lo instalaremos utilizando el comando **`pip install poetry`**
2.	Utilizaremos el comando **`poetry init`** para inicializar el nuevo proyecto en el directorio que usaremos.  En este el comando nos solicitará agregar algunos detalles del proyecto como el nombre y la versión y se creará un archivo que contendrá la configuración del proyecto.
3.	Utilizando el comando **`poetry add`**, iremos agregando una a una las librerías que necesitaremos incluir en el proyecto.  Dentro de estas librerías se encuentran **nltk, re, pandas, numpy, seaborn, matplotlib, collections y sklearn**.
4.	Una vez agregadas todas las librerías necesarias del proyecto, utilizaremos el comando **`poetry install`** para instalar todas las dependencias al entorno Poetry.


## Pipelines de ejecución.

El fuerte de este proyecto es la clasificación de avisos mediante la implementación de bolsas de palabras.  Cuando contemos con datos suficientes vamos realizar predicciones sobre los datos y utilizaremos  **mlflow** para gestionar y rastrear el ciclo de vida de los modelos de aprendizaje.
