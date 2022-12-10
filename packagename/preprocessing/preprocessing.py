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
import re
import numpy as np
from unidecode import unidecode

def preprocesamiento():
    global df_total
    # Convertimos los DataFrames a diccionarios
    dict_da = df_dic_da.to_dict()
    dict_te = df_dic_te.to_dict()

    # Expresión regular
    regex = r"\w+-?\d+|\d+-?\w+|[^a-z ]| de | la | el | a "

    # Función de transformación "Descripción del Aviso"
    def transform_da(text):
        text = unidecode(text)
        text = text.lower()
        text = re.sub(re.compile(regex), " ", text)
        text = re.sub(re.compile(r" +"), " ", text)
        text = text.strip()
        text = text.split()
        text = [token for token in text if len(token) > 1]
        text = [token.replace(token,dict_da['Corrector'].get(token, token)) for token in text]
        return " ".join(text)

    # Función de transformación "Texto Explicativo"
    def transform_te(text):
        text = unidecode(text)
        text = text.lower()
        text = re.sub(re.compile(regex), " ", text)
        text = re.sub(re.compile(r" +"), " ", text)
        text = text.strip()
        text = text.split()
        text = [token for token in text if len(token) > 1]
        text = [token.replace(token,dict_te['Corrector'].get(token, token)) for token in text]
        return " ".join(text)

    # Agregar columnas Nuevas
    df_total['Descripción preprocesado'] = df_total['Descripción'].apply(transform_da)
    df_total['Texto explicativo preprocesado'] = df_total['Texto explicativo'].apply(transform_te)

    # Visualizamos el resultado de "Descripción preprocesado"
    display(pd.DataFrame(df_total['Descripción preprocesado']))

    # Visualizamos el resultado de "Texto explicativo preprocesado"
    display(pd.DataFrame(df_total['Texto explicativo preprocesado']))

    # Creación Columnas
    df_total = df_total.assign(Clasificación = np.nan)
    df_total = df_total.assign(Proceso_gestión = np.nan)
    df_total = df_total.assign(Tipo_falla_SP = np.nan)

    # Renombramiento Columnas
    df_total.rename({'Proceso_gestión':'Proceso gestión', 'Tipo_falla_SP':'Tipo falla / SP'}, axis=1, inplace=True)

    # Generamos la información con las características del DataFrame
    display(df_total.info())

    # Visualizamos el tamañao del nuevo DataFrame
    display(df_total.shape)
