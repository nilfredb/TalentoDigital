# Deep Learning Model Evaluation: Metrics and Validation

## Guided Exercises — Results

### a) Incremento de épocas (EPOCHS = 5)
- La matriz de confusión se vuelve más diagonal.
- Mejora la clasificación correcta en la mayoría de clases.
- Riesgo leve de overfitting si se entrena demasiado.

**Conclusión:** Más épocas mejoran el rendimiento, pero deben controlarse.

---

### b) Uso de SGD en lugar de Adam
- SGD converge más lento.
- Menor precision inicial.
- Mejor generalización en algunos casos.

**Conclusión:** Adam es más rápido, SGD puede generalizar mejor.

---

### c) Reducción del dataset (2000 ejemplos)
- Disminuye el F1-score.
- Mayor varianza en resultados.
- Peor generalización.

**Conclusión:** Menos datos afectan negativamente el rendimiento.

---

### d) Cambio en normalización ([0,1] sin centrar)
- Entrenamiento más inestable.
- Métricas ligeramente peores.

**Conclusión:** La normalización centrada mejora el aprendizaje.

---

### e) Data Augmentation
- Mejora el F1-score.
- Reduce el overfitting.
- Mayor robustez del modelo.

**Conclusión:** El data augmentation mejora significativamente la generalización.

---

## 3) Validación cruzada (K-Fold)

- Se implementó K-Fold con K=3.
- Cada fold produce métricas ligeramente distintas.
- Promedio más representativo del rendimiento real.

**Conclusión:**
K-Fold reduce el sesgo de evaluación y mejora la confiabilidad.

---

## Interpretation

### Clases más confundidas
- Clases visualmente similares (ej. animales o vehículos) presentan mayor confusión.

---

### Precision vs Recall
- Precision: importante cuando los falsos positivos son críticos.
- Recall: importante cuando los falsos negativos son críticos.

---

### F1-score
- Balance entre precision y recall.
- Mejor métrica general en datasets desbalanceados.

---

### Estabilidad (K-Fold)
- Baja varianza → modelo estable.
- Alta varianza → modelo sensible a los datos.

---

## Final Conclusion

- Accuracy no es suficiente por sí sola.
- F1-score ofrece mejor visión global.
- Data augmentation y normalización son claves.
- K-Fold mejora la evaluación del modelo.

---

## Summary

- Adam → rápido y eficiente.
- SGD → más estable en generalización.
- Más datos → mejor rendimiento.
- Buen preprocesamiento → mejor aprendizaje.

👉 **Recomendación práctica**:
Siempre usar múltiples métricas + validación cruzada para evaluar modelos correctamente.