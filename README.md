# Clasificación Automática de Avisos de Falla

> **¿Quieres una explicación rápida?** Lee el [**Resumen del Proyecto**](RESUMEN_PROYECTO.md) 📄

## 📋 ¿De qué se trata este proyecto?

Este proyecto desarrolla una **solución de Procesamiento de Lenguaje Natural (NLP)** para automatizar la clasificación de avisos de falla en una empresa petrolera colombiana del segmento Midstream (transporte de hidrocarburos).

### 🎯 Problema que resuelve

**Contexto empresarial:**
- El cliente es una de las 10 empresas más grandes de Colombia por ingresos
- Opera cerca de 9,000 kilómetros de oleoductos y poliductos
- Registra aproximadamente 600 avisos mensuales en su sistema SAP sobre eventos en estaciones de bombeo

**Problema actual:**
- La clasificación manual de avisos consume **más de 200 horas mensuales**
- Costos anuales superiores a **$100,000,000**
- Proceso propenso a errores humanos (2 reclamaciones mensuales por clasificaciones incorrectas)

### 🚀 Solución propuesta

**Algoritmo de NLP** que:
1. Analiza automáticamente el texto de cada aviso (descripción y texto explicativo)
2. Busca palabras clave y patrones específicos del dominio petrolero
3. Clasifica cada aviso en categorías predefinidas:
   - **Clasificación**: "Pendiente", "No aplica", "Condición", "Falla"
   - **Proceso de gestión**: "Pendiente", "No aplica", "Inteligencia artificial", "Eliminación de defectos", "Seguridad de procesos"
   - **Tipo de falla/SP**: "Pendiente", "No aplica"

### 🔧 Arquitectura técnica

```
SAP ERP → Excel → Pandas DataFrame → Algoritmo NLP → Excel → Power BI
```

**Componentes principales:**
- **Preprocesamiento**: Limpieza y normalización de texto usando diccionarios especializados
- **Clasificación**: Implementación de bolsas de palabras (Bag of Words) con reglas de negocio
- **Exportación**: Generación de reportes para Power BI (MTBF, MTTR, Bad Actors)

### 📊 Impacto esperado

- **Reducir a cero** las reclamaciones por avisos mal clasificados
- **Automatizar** 200+ horas mensuales de trabajo manual
- **Mejorar** la calidad y consistencia de la clasificación
- **Acelerar** la toma de decisiones de mantenimiento

---

## 📁 Estructura del proyecto

```
├── docs/                          # Documentación completa
│   ├── business_understanding/    # Charter del proyecto y contexto empresarial
│   ├── data/                     # Definición y análisis de datos
│   └── infraestructure/          # Documentación técnica
├── packagename/                   # Código fuente principal
│   ├── preprocessing/            # Limpieza y normalización de texto
│   ├── classify/                 # Algoritmo de clasificación
│   ├── database/                 # Gestión de datos
│   ├── models/                   # Modelos de ML
│   ├── training/                 # Entrenamiento de modelos
│   ├── evaluation/               # Evaluación de rendimiento
│   └── visualization/            # Generación de reportes
└── README.md                     # Este archivo
```

## 🚀 Uso del sistema

### Ejemplo práctico
Ejecuta el script de demostración para ver cómo funciona el sistema:

```bash
python ejemplo_uso.py
```

### Flujo de trabajo completo
1. **Extracción de datos**: Exportar avisos desde SAP usando transacción IW49
2. **Preprocesamiento**: Ejecutar módulo de limpieza de texto
3. **Clasificación**: Aplicar algoritmo de NLP para categorizar avisos
4. **Exportación**: Generar archivo Excel para Power BI

### Uso programático
```python
from packagename.preprocessing.preprocessing import preprocesamiento
from packagename.classify.classify import clasificador

# Cargar datos
df_total = pd.read_excel("qFallas.xlsx")
df_dic_da = pd.read_excel("Diccionario_DA.xlsx")
df_dic_te = pd.read_excel("Diccionario_TE.xlsx")

# Preprocesar texto
df_procesado, viz_data = preprocesamiento(df_total, df_dic_da, df_dic_te)

# Clasificar avisos
clasificador()  # Usa variable global df_total

# Resultado: archivo 'clasificacion.xlsx' listo para Power BI
```

## 📚 Información académica

**Curso**: Machine Learning and Data Science Avanzado - Módulo 3

**Entregables**:
- ✅ Entregable 1: Business Understanding and Data Acquisition (27-nov-2022)
- ✅ Entregable 2: Preprocesamiento, EDA y Extracción de Características (4-dic-2022)
- ✅ Entregable 3: Implementación y Evaluación

**Integrantes:**
- Edwin Yecid González Gómez
- Leonardo Fabio Montenegro Torres

---

Para más detalles, consulte la [documentación completa](docs/) del proyecto.
