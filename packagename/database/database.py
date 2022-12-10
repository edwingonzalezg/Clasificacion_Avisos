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
def cargar_datos():
    df_total = pd.read_excel('qFallas.xlsx')
    df_bow = pd.read_excel('BoW clasificación de avisos.xlsx')
    df_dic_da = pd.read_excel('Diccionario DA.xlsx', index_col='Palabra')
    df_dic_te = pd.read_excel('Diccionario TE.xlsx', index_col='Palabra')
    
    display(df_total)
    display(df_bow)
    display(df_dic_da)
    display(df_dic_te)
