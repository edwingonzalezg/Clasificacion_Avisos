"""
Ejemplo de uso del sistema de clasificación de avisos de falla

Este script muestra cómo usar el sistema para procesar y clasificar avisos
de falla extraídos del sistema SAP.
"""

import pandas as pd
from packagename.preprocessing.preprocessing import preprocesamiento
from packagename.classify.classify import clasificador

def ejemplo_clasificacion_avisos():
    """
    Ejemplo básico de cómo usar el sistema de clasificación.
    
    NOTA: Este ejemplo requiere archivos de datos reales del sistema SAP.
    """
    
    print("🚀 Sistema de Clasificación Automática de Avisos de Falla")
    print("=" * 60)
    
    # PASO 1: Cargar datos (normalmente desde archivos Excel exportados de SAP)
    print("\n📂 PASO 1: Cargando datos...")
    print("- df_total: Datos principales de avisos desde SAP")
    print("- df_dic_da: Diccionario corrector para 'Descripción del aviso'")
    print("- df_dic_te: Diccionario corrector para 'Texto explicativo'")
    print("- df_bow: Bolsa de palabras para clasificación")
    
    # En un caso real, cargarías así:
    # df_total = pd.read_excel("qFallas.xlsx")
    # df_dic_da = pd.read_excel("Diccionario_DA.xlsx")
    # df_dic_te = pd.read_excel("Diccionario_TE.xlsx")
    # df_bow = pd.read_excel("BoW_clasificacion_avisos.xlsx")
    
    # PASO 2: Preprocesamiento de texto
    print("\n🔧 PASO 2: Preprocesamiento de texto...")
    print("- Normalización de texto (quitar acentos, minúsculas)")
    print("- Limpieza con expresiones regulares")
    print("- Aplicación de diccionarios correctores")
    print("- Filtrado de palabras irrelevantes ('de', 'la', 'el', 'a')")
    
    # En un caso real, ejecutarías:
    # df_procesado, visualizacion = preprocesamiento(df_total, df_dic_da, df_dic_te)
    
    # PASO 3: Clasificación automática
    print("\n🤖 PASO 3: Clasificación automática...")
    print("- Análisis de longitud de texto (< 40 caracteres = 'Pendiente')")
    print("- Búsqueda de palabras clave en descripción y texto explicativo")
    print("- Aplicación de reglas de negocio según diagrama de flujo")
    print("- Asignación de clasificaciones:")
    print("  • Clasificación: 'Pendiente', 'No aplica', 'Condición', 'Falla'")
    print("  • Proceso gestión: 'Pendiente', 'No aplica', 'Inteligencia artificial', etc.")
    print("  • Tipo falla/SP: 'Pendiente', 'No aplica'")
    
    # En un caso real, ejecutarías:
    # clasificador()  # Usa variable global df_total
    
    # PASO 4: Exportación de resultados
    print("\n📊 PASO 4: Exportación de resultados...")
    print("- Generación de archivo Excel: 'clasificacion.xlsx'")
    print("- Listo para importar en Power BI")
    print("- Reportes disponibles: MTBF, MTTR, Bad Actors")
    
    print("\n✅ Proceso completado exitosamente!")
    print("\n💡 Beneficios obtenidos:")
    print("   • Clasificación automática de cientos de avisos")
    print("   • Reducción de 200+ horas de trabajo manual")
    print("   • Mayor consistencia y precisión en clasificación")
    print("   • Información inmediata para decisiones de mantenimiento")

def mostrar_flujo_trabajo():
    """Muestra el flujo de trabajo completo del sistema."""
    
    print("\n📋 FLUJO DE TRABAJO COMPLETO")
    print("=" * 40)
    
    pasos = [
        "1. 📥 Extraer datos de SAP usando transacción IW49",
        "2. 💾 Guardar archivos Excel en ubicación especificada",
        "3. 🔧 Ejecutar preprocesamiento de texto",
        "4. 🤖 Aplicar algoritmo de clasificación NLP",
        "5. 📊 Generar archivo Excel con clasificaciones",
        "6. 📈 Importar resultados en Power BI",
        "7. 📋 Generar reportes de confiabilidad (MTBF, MTTR, Bad Actors)"
    ]
    
    for paso in pasos:
        print(f"   {paso}")
    
    print(f"\n🎯 Resultado: Avisos clasificados automáticamente y listos para análisis")

if __name__ == "__main__":
    ejemplo_clasificacion_avisos()
    mostrar_flujo_trabajo()