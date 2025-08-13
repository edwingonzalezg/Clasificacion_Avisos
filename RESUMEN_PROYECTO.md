# ¿De qué se trata este proyecto?

## Resumen ejecutivo

Este proyecto desarrolla una **herramienta de inteligencia artificial** para automatizar la clasificación de avisos de falla en una empresa petrolera colombiana.

## El problema

Una empresa petrolera líder en Colombia (con 9,000 km de oleoductos) tiene un problema costoso:

- **600 avisos mensuales** registrados en SAP sobre eventos en estaciones de bombeo
- **200+ horas mensuales** gastadas en clasificación manual
- **$100+ millones anuales** en costos de clasificación
- **Errores humanos** que generan reclamaciones del cliente

## La solución

**Algoritmo de Procesamiento de Lenguaje Natural (NLP)** que:

1. **Lee automáticamente** el texto de cada aviso
2. **Identifica palabras clave** específicas del sector petrolero
3. **Clasifica automáticamente** cada aviso en categorías:
   - Si es una falla real o solo una condición
   - Qué tipo de proceso de gestión requiere
   - Si necesita intervención de seguridad

## Cómo funciona

```
📄 Aviso en SAP → 🤖 Algoritmo NLP → 📊 Clasificación automática → 📈 Reportes Power BI
```

**Ejemplo práctico:**
- **Entrada**: "Fuga en válvula principal estación bombeo"
- **Salida**: Clasificación="Falla", Proceso="Eliminación de defectos"

## Beneficios

✅ **Ahorro de tiempo**: De 200 horas manuales a procesamiento automático  
✅ **Reducción de costos**: Elimina $100+ millones anuales en clasificación manual  
✅ **Mejor precisión**: Reduce errores de clasificación a cero  
✅ **Decisiones más rápidas**: Información inmediata para mantenimiento  

## Tecnologías utilizadas

- **Python** para el desarrollo del algoritmo
- **Pandas** para procesamiento de datos
- **NLP** con bolsas de palabras especializadas
- **SAP** como fuente de datos
- **Power BI** para visualización

## Impacto empresarial

Este proyecto transforma un proceso manual, costoso y propenso a errores en una solución automatizada que mejora la eficiencia operacional y reduce significativamente los costos de mantenimiento en la industria petrolera colombiana.