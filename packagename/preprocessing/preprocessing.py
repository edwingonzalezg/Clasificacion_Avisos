
import re
import pandas as pd
import numpy as np
from unidecode import unidecode
from typing import Dict, Tuple, Optional
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextPreprocessor:
    """Clase para preprocesamiento de texto de avisos de falla."""
    
    def __init__(self):
        # Compilar regex una sola vez para mejor rendimiento
        self.regex_pattern = re.compile(r"\w+-?\d+|\d+-?\w+|[^a-z ]| de | la | el | a ")
        self.whitespace_pattern = re.compile(r" +")
        
    def _clean_text(self, text: str, corrector_dict: Dict[str, str]) -> str:
        """
        Limpia y normaliza texto usando diccionario corrector.
        
        Args:
            text: Texto a procesar
            corrector_dict: Diccionario para corrección de palabras
            
        Returns:
            Texto procesado y limpio
        """
        if pd.isna(text) or not isinstance(text, str):
            return ""
            
        try:
            # Normalizar texto
            text = unidecode(text).lower()
            
            # Aplicar expresiones regulares
            text = self.regex_pattern.sub(" ", text)
            text = self.whitespace_pattern.sub(" ", text)
            text = text.strip()
            
            # Tokenizar y filtrar
            tokens = [token for token in text.split() if len(token) > 1]
            
            # Aplicar corrector
            tokens = [corrector_dict.get(token, token) for token in tokens]
            
            return " ".join(tokens)
            
        except Exception as e:
            logger.error(f"Error procesando texto: {e}")
            return ""
    
    def preprocess_dataframe(
        self, 
        df: pd.DataFrame,
        dict_da: Dict[str, str],
        dict_te: Dict[str, str],
        verbose: bool = True
    ) -> pd.DataFrame:
        """
        Preprocesa DataFrame completo con avisos.
        
        Args:
            df: DataFrame con datos originales
            dict_da: Diccionario corrector para descripción
            dict_te: Diccionario corrector para texto explicativo
            verbose: Si mostrar información de progreso
            
        Returns:
            DataFrame con columnas preprocesadas
        """
        if df.empty:
            logger.warning("DataFrame está vacío")
            return df.copy()
            
        df_processed = df.copy()
        
        try:
            # Validar columnas requeridas
            required_cols = ['Descripción', 'Texto explicativo']
            missing_cols = [col for col in required_cols if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Columnas faltantes: {missing_cols}")
            
            # Procesar descripción
            if verbose:
                logger.info("Procesando descripción del aviso...")
            df_processed['Descripción preprocesado'] = df['Descripción'].apply(
                lambda x: self._clean_text(x, dict_da)
            )
            
            # Procesar texto explicativo
            if verbose:
                logger.info("Procesando texto explicativo...")
            df_processed['Texto explicativo preprocesado'] = df['Texto explicativo'].apply(
                lambda x: self._clean_text(x, dict_te)
            )
            
            # Agregar columnas para clasificación
            df_processed = df_processed.assign(
                Clasificación=np.nan,
                **{'Proceso gestión': np.nan, 'Tipo falla / SP': np.nan}
            )
            
            if verbose:
                logger.info(f"Preprocesamiento completado. Shape: {df_processed.shape}")
                
            return df_processed
            
        except Exception as e:
            logger.error(f"Error en preprocesamiento: {e}")
            raise

def preprocesamiento(
    df_total: pd.DataFrame,
    df_dic_da: pd.DataFrame,
    df_dic_te: pd.DataFrame,
    verbose: bool = True
) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """
    Función principal de preprocesamiento.
    
    Args:
        df_total: DataFrame principal con avisos
        df_dic_da: DataFrame con diccionario para descripción
        df_dic_te: DataFrame con diccionario para texto explicativo
        verbose: Si mostrar información de progreso
        
    Returns:
        Tupla con DataFrame procesado y diccionario de resultados para visualización
    """
    try:
        # Validar entrada
        if any(df.empty for df in [df_total, df_dic_da, df_dic_te]):
            raise ValueError("Uno o más DataFrames están vacíos")
        
        # Convertir diccionarios
        dict_da = df_dic_da.to_dict().get('Corrector', {})
        dict_te = df_dic_te.to_dict().get('Corrector', {})
        
        if not dict_da or not dict_te:
            logger.warning("Diccionarios correctores están vacíos")
        
        # Crear preprocessor
        preprocessor = TextPreprocessor()
        
        # Procesar datos
        df_processed = preprocessor.preprocess_dataframe(
            df_total, dict_da, dict_te, verbose
        )
        
        # Preparar resultados para visualización
        visualization_data = {
            'descripcion_preprocesado': df_processed[['Descripción preprocesado']],
            'texto_preprocesado': df_processed[['Texto explicativo preprocesado']],
            'info': df_processed.info(),
            'shape': df_processed.shape
        }
        
        return df_processed, visualization_data
        
    except Exception as e:
        logger.error(f"Error en función principal: {e}")
        raise

# Función de compatibilidad con código existente
def preprocesamiento_legacy():
    """
    Función legacy para mantener compatibilidad.
    DEPRECATED: Usar preprocesamiento() en su lugar.
    """
    logger.warning("Usando función legacy. Considere migrar a la nueva API.")
    # Aquí iría la lógica original si es necesario mantener compatibilidad
    pass
