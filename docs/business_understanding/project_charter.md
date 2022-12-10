# Carta del proyecto

## Antecedentes empresariales

El sector minero-energético colombiano es una de las locomotoras definidas por el Gobierno Nacional como el principal motor de desarrollo para el país y busca generar buena parte de las rentas que se necesitan para el funcionamiento del estado. En Colombia, los hidrocarburos aportan el 3,3% del producto interno bruto (PIB), en tanto el petróleo representa el 40% de lo que en Colombia le vende al mundo.

# Quién es el cliente, en qué ámbito empresarial se encuentra el cliente.

Explicaremos brevemente el funcionamiento de la producción de petróleo en Colombia. Lo primero que se debe considerar es que el sector Oil & Gas está dividido en 3 segmentos generales:

1.   **Upstream:** Este sector incluye las tareas de búsqueda de yacimientos potenciales de petróleo crudo y de gas natural, tanto subterráneos como submarinos, la perforación de pozos exploratorios, y posteriormente la perforación y explotación de los pozos que llevan el petróleo crudo o el gas natural hasta la superficie.

2.   **Midstream:** Este sector incluye el transporte, ya sea por tuberías, ferrocarril, barcaza, o camión, el almacenamiento y la comercialización al por mayor de productos crudos o refinados derivados del petróleo. 

3.   **Downstream:** Este sector se refiere a las tareas de refinamiento del petróleo crudo y al procesamiento y purificación del gas natural, así como también la comercialización y distribución de productos hasta los consumidores tales como la gasolina, querosén, gasóleo, fueloil, lubricantes, ceras, asfalto, gas natural y el gas licuado.
 
Actualmente nos encontramos trabajando para el segmento de Midstream donde el transporte juega un papel muy importante ya que permite trasladar el petróleo desde los diferentes yacimientos del país hacia la costa atlántica donde se realiza su exportación.

El cliente es una empresa dedicada al transporte y la logística de hidrocarburos, que lidera el segmento Midstream en la cadena del petróleo de Colombia. Es una de las empresas más grandes del país por cantidad de activos y se encuentra entre las 10 compañías más grandes por ingresos operacionales y utilidades del país. Esta empresa cuenta con cerca de 9.000 kilómetros de oleoductos y poliductos por los que se transporta la mayoría del crudo y los refinados de Colombia.

## ¿Qué problemas empresariales se pretenden resolver?

Para disminuir los costos de mantenimiento y obtener una mayor rentabilidad se requiere buscar una solución para las fallas que se presenten. El primero paso es identificar dichas fallas, sin embargo, no es fácil hacerlo ya que en el CCMS (Gestión de mantenimiento asistido por computadora: SAP) se registran todos los eventos que ocurren dentro de una estación de bombeo de petróleo, como: eventos naturales, condiciones de desgaste, acompañamientos, visitas, fallas, entre otras. Actualmente se registran cerca de 600 avisos en SAP.

Para realizar la clasificación adecuada de los avisos se cuenta con un grupo de personas que invierten más de 200 horas cada "mes", esto genera costos anuales que superan los $100.000.000. Este proceso se realiza manualmente donde los ingenieros deben ingresar a SAP y revisar cada uno de los eventos registrados buscando algunas palabras claves que indican si el aviso corresponde a una falla, una condición, un acompañamiento, un evento natural, etc.

## Alcance
* **¿Qué soluciones de ciencia de datos estamos tratando de construir?**

La solución de datos objeto de este proyecto se basa en el Procesamiento de Lenguaje Natural (NLP) donde el algoritmo ingrese a cada uno de los eventos registrados, busque algunas palabras clave y encuentre patrones para que se realice la clasificación con base en los lineamientos del documento **MED-PD-01_V1 - Procedimiento investigación fallas o averías activos productivos** de propiedad del cliente.

**¿Qué vamos a hacer?**

El algoritmo debe ingresar y validar cada uno de los textos de cada aviso y clasificarlo de acuerdo con la imagen anterior:

* En la columna Clasificación debe colocar una de las siguientes opciones: "Pendiente", "No aplica", "Condición" o "Falla".
* En la columna Proceso de Gestión debe colocar "Pendiente", "No aplica", "Inteligencia artificial", "Eliminación de defectos" o "Seguridad de procesos".
* En la columna Tipo de Falla/SP debe colocar "Pendiente" o "No aplica" y para avisos clasificados como "Eliminación de defectos" o "Seguridad de procesos", dejar este campo en blanco.

**¿Cómo va a ser consumido por el cliente?**

* Por parte del cliente: Los funcionarios del área de analítica de mantenimiento mediante consulta directa de los datos y mediante consumo de los reportes en Power BI de Tiempo Medio entre fallas, (MTBF), Tiempo Medio para Reparar (MTTR), y malos actores (BAD ACTORS).
* Por parte de la empresa: Los ingenieros de confiabilidad que hacen parte del área de sostenimiento.

## Personal

**¿Quiénes están en este proyecto?**

* Empresa a cargo del proyecto:

**Jefe de proyecto**: Edwin González (Jefe del área de sostenimiento)

**Científico(s) de datos**: Leonardo Fabio Montenegro (Ingeniero de datos)

* Cliente:
**Contacto con la empresa**: Diana Mendez (Ingeniero de confiabilidad e integridad)

	
## Métricas
* **Objetivos cualitativos**: Garantizar una alta calidad de la información de fallas de los activos productivos con el fin de aplicar de manera efectiva las técnicas de análisis de información de confiabilidad que nos permitan tomar las mejores decisiones para mejorar la confiabilidad y disponibilidad de los activos del cliente.
* **Métricas cuantificables**: Número de reclamaciones por parte del cliente referentes a avisos de falla o evento de seguridad de procesos mal clasificados.
* **Cuantificación de la utilidad de la mejora de los valores para el escenario del cliente**: Reducir a cero el número de reclamaciones por parte del cliente referentes a avisos de falla o eventos de seguridad de procesos mal clasificados.
* **Valor de referencia (actual) de la métrica**: Número de reclamaciones al mes por parte del cliente referentes a avisos mal clasificados = 2 al mes
* **Medición de la métrica**: # de reclamaciones al mes por parte del cliente referentes a avisos mal clasificados.

## Plan
## Fases (hitos), calendario, breve descripción de lo que haremos en cada fase.

Por ser un proyecto pequeño se va a utilizar un modelo de desarrollo en cascada con las siguientes fases:

**Requisitos**: Durante esta etapa se realizará la identificación de los datos relevantes para realizar la clasificación de las fallas.  Duración 1 semana.

**Diseño**: Durante esta etapa se configurará la disposición de columnas a exportar en Excel mediante la transacción IW49, se creará la bolsa de palabras con la cual se va a realizar la clasificación de las fallas, se desarrollará en lenguaje Python la lógica para realizar el preprocesamiento de la información y se desarrollará en Python la lógica de implementación del clasificador de avisos.  Duración 2 semanas.

**Implementación**: En esta etapa se realiza la puesta en producción del modelo generando el set de datos con las características que requiere el informe en Power BI para poder ser actualizado y visualizado.  Duración 1 semana

**Verificación**: Durante esta etapa se van a realizar de manera aleatoria revisiones manuales a diferentes avisos con el fin de identificar posibles errores en la clasificación de avisos.  Duración 1 semana

**Mantenimiento**: El mantenimiento de la solución se va a realizar bajo demanda cuando se identifiquen palabras a incluir dentro de la bolsa de palabras. 


## Arquitectura

Generar consulta en SAP ERP > Guardar datos en archivo en Excel > Procesar datos en DataFrame de Pandas > Exportar datos procesados a Excel > Procesar y graficar datos en Power BI

## Datos

El módulo PM, también conocido como módulo de mantenimiento de planta tiene como función mejorar el control, gestión y planificación de consumo de materiales, repuestos y servicios de una planta, e integrar al mantenimiento la gestión de los activos.  Los lineamientos en temas de seguridad de la información del Sistema de Gestión de Tecnologías de la Información para el ERP SAP del cliente no permiten una conexión directa a SAP para la extracción de los datos.

## ¿Qué datos esperamos? Datos en bruto en las fuentes de datos del cliente (por ejemplo, archivos on-prem, SQL, Hadoop on-prem, etc.)

* **Movimiento de datos**

Los datos se deben extraer de SAP directamente por la interfaz de usuario por medio de las transacciones configuradas para tal fin.  Las transacciones de consulta permiten exportar los datos a un archivo plano para luego ser procesados con una aplicación externa como Microsoft Excel.

* **Herramientas y recursos de almacenamiento**

 * Microsoft OneDrive
 * Google Drive

* **Cómo se consumirá el servicio.**

A través de Power BI mediante los reportes de Tiempo Medio Entre Fallas (MTBF), Tiempo Medio para Reparar (MTTR) y Malos actores (BAD ACTORS)

## Comunicación

* **Canal de comunicación**

Mediante reuniones sistemáticas semanales de eliminación de defectos entre la empresa y el cliente en las cuales se analizarán las fallas más representativas ocurridas durante la semana.

* **Canal de comunicación**

**Por la empresa**: Edwin González (Jefe del área de sostenimiento)
**Por el cliente**: Diana Mendez (Ingeniero de confiabilidad e integridad)
