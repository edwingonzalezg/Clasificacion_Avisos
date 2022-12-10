# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

def clasificador():
    
    global df_total
    
    # Validación de texto explicativo
    df_total.loc[df_total['Texto explicativo preprocesado'].str.len() <= 40, 'Clasificación'] = 'Pendiente'
    df_total.loc[df_total['Texto explicativo preprocesado'].str.len() <= 40, 'Proceso gestión'] = 'Pendiente'
    df_total.loc[df_total['Texto explicativo preprocesado'].str.len() <= 40, 'Tipo falla / SP'] = 'Pendiente'

    # Verificamos los valores "Pendientes"
    df_total['Clasificación'].value_counts()

    # Bolsa de palabras
    def filter_and_assign(lookup_column, process):
        df = df_bow.loc[:, ['palabra clave', 'clasificación']][(df_bow['columna de búsqueda'] == lookup_column) & (df_bow['proceso de gestión'] == process)]

        for i in range(len(df)):
            df_total.loc[(df_total[lookup_column].str.contains(df.iloc[i]['palabra clave'])) & (df_total['Clasificación'].isnull()), 'Clasificación'] = df.iloc[i]['clasificación']
            df_total.loc[(df_total[lookup_column].str.contains(df.iloc[i]['palabra clave'])) & (df_total['Proceso gestión'].isnull()), 'Proceso gestión'] = process
            if process != 'Eliminación de defectos' and process != 'Seguridad de procesos':
                df_total.loc[(df_total[lookup_column].str.contains(df.iloc[i]['palabra clave'])) & (df_total['Tipo falla / SP'].isnull()), 'Tipo falla / SP'] = 'No aplica'

    # Vamos siguiendo el paso a paso del diagrama de flujo
    filter_and_assign('Descripción preprocesado', 'No aplica')
    filter_and_assign('Descripción preprocesado', 'Inteligencia artificial')
    filter_and_assign('Texto explicativo preprocesado', 'Seguridad de procesos')
    filter_and_assign('Descripción preprocesado', 'Seguridad de procesos')
    filter_and_assign('Texto explicativo preprocesado', 'Eliminación de defectos')
    filter_and_assign('Descripción preprocesado', 'Eliminación de defectos')

    # Reemplazamos los valores "NaN" de acuerdo al diagrama de flujo
    df_total['Clasificación'] = df_total['Clasificación'].replace(np.nan, 'Condición')
    df_total['Proceso gestión'] = df_total['Proceso gestión'].replace(np.nan, 'Mantenimiento por condición')
    df_total['Tipo falla / SP'] = df_total['Tipo falla / SP'].replace(np.nan, 'No aplica')

    # Visualizamos un resumen de los resultados
    df_final = df_total.loc[:,['Descripción preprocesado', 'Clasificación', 'Proceso gestión', 'Tipo falla / SP']]
    display(df_final)

    # Etiquetas columna de "Clasificación"
    display(df_total["Clasificación"].value_counts())

    # Etiquetas columna de "Proceso gestión"
    display(df_total["Proceso gestión"].value_counts())

    # Etiquetas columna de "Tipo falla / SP"
    display(df_total["Tipo falla / SP"].value_counts())

    # Exportar el archivo a Excel para su utilización
    df_final.to_excel("clasificacion.xlsx")
