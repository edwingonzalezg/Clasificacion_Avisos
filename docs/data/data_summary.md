# Informe de datos

Los datos provienen del CMMS **SAP** donde cada tipo de evento ocurrido en las diferentes estaciones de petróleo es registrado, almacenando datos puntales que pueden ser de interes para realizar muchos tipos de análisis.

En este archivo se pueden identificar diferentes columnas que continen información detallada de cada registro o actividad. Este dataset se denomina **`qFallas`** el cual tiene diferentes tipos de datos como:

*   **`datetime64[ns]`** para identificar las fechas de los eventos como el inicio o el fin de la avería.
*   **`int64`** para identificar registros de conteo como el número del aviso o el número que identifica el equipo.   
*   **`float64`** para identificar registros cuantificados como la duración de la parada del equipo, clasificacion, proceso de gestión o el tipo de falla.
*   **`object`** para identificar todos los registros de texto como secuencia de caracteres (string) y corresponden a la gran mayoría de los datos del dataset. Tenemos ejemplos importantes como la descripción, el texto explicativo, la estación, el sistema, ubicción crticidad, etc.

Adiconalmente se cuenta con los datasets de los diccionarios y bolsas de palabras:

*   **`BoW clasificación de avisos`** 
*   **`Diccionario DA`**
*   **`Diccionario TE`**

Los cuales se describiran a continuación.

## Resumen general de los datos 

*   **`qFallas`** archivo con la data extraída de SAP que contiene todos los registros.

Este archivo cuenta con 60 variables tipo **`datetime64[ns]`**, **`int64`**, **`float64`** y **`object`**

![image](https://user-images.githubusercontent.com/119147133/205520784-0739fce8-6364-4577-8043-983807ae45d4.png)

*   **`BoW clasificación de avisos`** archivo que contiene una bolsa de palabras específicas de ingeniería depetróleos.

Este archivo cuenta con 4 variables tipo **`object`** y 180 registros

![image](https://user-images.githubusercontent.com/119147133/205521213-7325a928-1822-418a-a9e1-e51daa9e3a44.png)

*   **`Diccionario DA`** archivo que contiene un diccionario para realizar la corrección de palabras en la columna *descrición del aviso*. 

Este archivo cuenta con una variables tipo **`object`** y 5.537 registros

![image](https://user-images.githubusercontent.com/119147133/205521238-c70da6b2-e070-4222-87ed-a40028f55f0e.png)

*   **`Diccionario TE`** archivo que contiene un diccionario para realizar la corrección de palabras en la columna *texto explicativo*. 

Este archivo cuenta con una variables tipo **`object`** y 248 registros

![image](https://user-images.githubusercontent.com/119147133/205521255-19c941eb-2695-4f2a-a900-402515521c88.png)

## Resumen de la calidad de los datos

La calidad de los datos es deficiente por este motivo debemos realizar el preprocesamiento de la información para que de este manera sepueda implementar un clasificador de variables, lo cual se mostrará más adelante. A continuación algunas estadisticas de las principales variables:

![image](https://user-images.githubusercontent.com/119147133/205522734-04c44523-2c0b-4a1d-8f52-79e065be1ec6.png)

![image](https://user-images.githubusercontent.com/119147133/205522749-27c862b0-3b90-497e-bd9b-ba4f2dcc4240.png)

![image](https://user-images.githubusercontent.com/119147133/205522753-1f07a3ae-f890-44a0-a707-56f6b9ec8e5b.png)

## Variable objetivo

El objetivo de este proyecto es diseñar una solución basa en *Procesamento de Leguaje Natural* **(NPL)** donde el algoritmo ingrese a cada uno de los textos de los eventos registrados, busque algunas palabras clave y encuentre patrones para que finalemente realice una clasificación de la siguiente manera:

![image](https://user-images.githubusercontent.com/119147133/205521661-d669ce31-588e-4e89-965e-967baafa19ab.png)

El algoritmo debe ingresar y validar cada uno de los textos de cada aviso y clasificarlo de acuerdo a la imagen anterior:

*   En la columna **`Clasificación`** debe colocar 0, 1, 2 o 3 para avisos pendientes, no aplican, condiciones o fallas.
*   En la columna **`Proceso de Gestión`** debe colocar 0, 1, 2, 3, 4 o 5 para avisos pendientes, no aplican, mantenimientos por condición, avisos de inteligencia artificial, eliminación de defectos o eventos de seguridad de procesos respectivamente.
*   En la columna **`Tipo de Falla/SP`** debe colocar 0 o 1 para avisos que estén pendientes o avisos que no apliquen.

La clasificación debe realizar en el siguiente orden lógico para lograr obtener una clasificación correcta:

![image](https://user-images.githubusercontent.com/119147133/205521667-4dda5a68-7549-43b9-9ec7-816d6a44f700.png)

Adicionalmente intentaremos realizar una predicción para los avisos los cuales cuentan unicamente con la descrición básica y de esta manera realizar una predicción previa lo cual permitirá anticiparnos a los difernetes eventos que se puedan presentar.

## Variables individuales y clasificación

Se cuenta con bastate información y dentro de este se tienen muchas variables, sin embargo nos interesan solamente 2 variables ***descripción del aviso*** y  ***texto explicativo***.

Nuestro primer objetivo en el preprocesamiento será implementar una función para transformar el texto de los campos ***descripción del aviso*** y ***texto explicativo*** con su respectivo diccionario asociado. Para esto será necesario crear una expresión regurar que reemplazará los tags, dejando solamente letras y elimina palabras como ***'de', 'la', 'el', 'a'.***  

![image](https://user-images.githubusercontent.com/119147133/205523409-6a94d3d8-0f27-4a6d-9ce2-03004e565d22.png)

![image](https://user-images.githubusercontent.com/119147133/205523431-2343a1fe-3a35-4aae-84e5-aa1122f0f641.png)

![image](https://user-images.githubusercontent.com/119147133/205523450-c3e75d88-2f48-4fe7-8fd1-3726dfdfcc55.png)

![image](https://user-images.githubusercontent.com/119147133/205523467-4e0d906c-4032-4ca3-b065-9c7d3a2f85c7.png)

Luego agregaremos dos nuevas columnas con los campos 'Descripción' y 'Texto explicativo' preprocesados.

![image](https://user-images.githubusercontent.com/119147133/205523503-afe4f2f7-e8b5-4d0d-8356-15d671c5ddf3.png)

Obteniendo:

![image](https://user-images.githubusercontent.com/119147133/205523516-9597e0e6-bc4e-464b-b25e-a3925ab27964.png) ![image](https://user-images.githubusercontent.com/119147133/205523528-9b0bf08a-b37e-42c4-8b5a-3315f0988460.png)

## Relación entre las variables explicativas y la variable objetivo

Una de las palabras objetivo es ***falla*** la cual nos indica si un texto corresponde a una falla o no; dicha información es vital para llevar los registros de la empresa de manera adecuada y poder tomar decisiones acertivas sobrelos equipos que presenten fallas. 

A continuación podemos observar la relación de la palbra **falla** en el conteo de caracteres, en el conteo de plabras y en el conteo de oraciones:

![image](https://user-images.githubusercontent.com/119147133/205522757-1adc91df-b7c7-430a-ada9-d344bc546abb.png)

![image](https://user-images.githubusercontent.com/119147133/205522820-1fc82d19-cb16-4178-be46-650f1e2ed6d0.png)

Para los registros que indican las fallas podemos ver que efectivamente las palabras **falla**, **fallar** y **fuga** (que es también una falla) son las que más veces se repiten, lo cual nos indica que existe una fuerte relación de los textos con la variable objetivo.

![image](https://user-images.githubusercontent.com/119147133/205522870-28159c6c-d2c8-4ef0-8e5b-9ea4696d262d.png)

![image](https://user-images.githubusercontent.com/119147133/205522833-f337a1fa-0310-441d-a06e-299b995c3f26.png)

Por otro lado, los registros que indican condiciones, es decir, "NO FALLAS" también tienen las mismas palabras con mayor número de repeticviones (a excepción de **CBM**) lo cual representa un verdadero desafío para poder realizar la calsificación de manera adecuada.

![image](https://user-images.githubusercontent.com/119147133/205522880-78a2cc84-3f68-49b1-a5fa-c302af5d57f8.png)

![image](https://user-images.githubusercontent.com/119147133/205522855-ad3d56a1-9dff-45b2-9db7-99093cfbc498.png)
