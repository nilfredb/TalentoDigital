# Taller: Transfer Learning — Feature Extraction vs Fine-Tuning

## 4) Ejercicios guiados (respuestas)

### a) Congelación selectiva (layer3 + layer4)
- Descongelar **layer4** mejora la adaptación al nuevo dataset.
- Descongelar también **layer3**:
  - Puede mejorar ligeramente la accuracy.
  - Pero aumenta el riesgo de overfitting (especialmente con pocos datos).

✅ **Conclusión**:
- Descongelar más capas aumenta capacidad de aprendizaje.
- Pero también aumenta el riesgo de sobreajuste.
- Layer4 suele ser el mejor compromiso.

---

### b) LR diferenciado (LR_FT = 1e-4)
- Con LR_FT = 3e-4:
  - Entrenamiento más rápido.
  - Puede introducir ruido en capas preentrenadas.
- Con LR_FT = 1e-4:
  - Entrenamiento más estable.
  - Más lento en converger.

✅ **Conclusión**:
Reducir LR en fine-tuning mejora estabilidad, pero ralentiza el aprendizaje.

---

### c) Transferencia negativa (CIFAR-100 reducido a 10 clases)
- Peor rendimiento comparado con CIFAR-10.
- El modelo preentrenado no generaliza tan bien a un dominio diferente.

✅ **Conclusión**:
La transferencia negativa ocurre cuando:
- El dominio de origen ≠ dominio destino.
- Las features aprendidas no son relevantes.

---

### d) Data augmentation
Añadiendo:
- RandomCrop(32, padding=4)
- ColorJitter

Resultados:
- Mejora la generalización.
- Reduce el overfitting.
- Entrenamiento más robusto.

✅ **Conclusión**:
El data augmentation mejora significativamente el rendimiento en validación.

---

### e) Más épocas (EPOCHS = 5 con GPU)
- Feature Extraction:
  - Mejora leve tras más épocas.
  - Se estanca rápido.
- Fine-Tuning:
  - Mejora progresiva.
  - Mayor capacidad de adaptación.

✅ **Conclusión**:
Fine-tuning se beneficia más de entrenamientos largos.

---

## 5) Interpretación rápida

### ¿Cuál enfoque fue mejor?
- **Fine-Tuning (B)** logra mayor accuracy.
- **Feature Extraction (A)** es más rápido pero limitado.

---

### Transferencia negativa
- Aparece cuando el dataset cambia mucho.
- Reduce el rendimiento del modelo preentrenado.

---

### ¿Qué capas conviene descongelar?
- Solo layer4 → mejor balance.
- Más capas → más capacidad pero más overfitting.

---

### LR diferenciado
- LR bajo en capas preentrenadas (layer4).
- LR más alto en la cabeza (fc).

Ejemplo óptimo:
- layer4 → 1e-4
- fc → 1e-3

---

## 6) Conclusión general

### Feature Extraction
✔ Rápido  
✔ Fácil  
❌ Menor precisión  

---

### Fine-Tuning parcial
✔ Mayor precisión  
✔ Mejor adaptación  
❌ Más costoso computacionalmente  

---

## Resumen final

- Si tienes poco tiempo o recursos → **Feature Extraction**
- Si buscas mejor rendimiento → **Fine-Tuning**
- Siempre usar:
  - LR diferenciado
  - Data augmentation
  - Descongelación progresiva

👉 **Recomendación práctica**:
1. Empieza con Feature Extraction.
2. Luego aplica Fine-Tuning si necesitas mejorar resultados.