# 🧠 Taller: Evaluación y Métricas en PLN

## 🔍 7) Experimentos y reflexión

### a) Clase minoritaria

Al reducir los ejemplos de una clase:

- El modelo tiene menos datos para aprender ese patrón.
- El **F1 de esa clase disminuye significativamente**.
- Puede aumentar el sesgo hacia clases mayoritarias.

**Conclusión:**  
El desbalance de clases afecta negativamente el rendimiento del modelo, por lo que es importante evaluar métricas por clase y no solo accuracy.

---

### b) Ajuste de umbrales (probabilidades)

Al modificar el umbral de decisión:

- **Umbral bajo:**
  - Aumenta el recall
  - Disminuye la precisión

- **Umbral alto:**
  - Aumenta la precisión
  - Disminuye el recall

**Conclusión:**  
El umbral debe ajustarse según el costo de errores en el problema.

---

### c) Métrica prioritaria según el caso

- Si el problema penaliza **falsos negativos**:
  - Priorizar **recall**
  - Ejemplo: detección de enfermedades

- Si penaliza **falsos positivos**:
  - Priorizar **precisión**
  - Ejemplo: detección de spam

**Conclusión:**  
No existe una métrica universal; depende del contexto.

---

### d) ROUGE vs BLEU

- **ROUGE:**
  - Mide coincidencia con referencia (recall)
  - Más usado en resumen automático

- **BLEU:**
  - Mide precisión de n-gramas
  - Más usado en traducción automática

**Observación:**
- Un texto puede tener alto ROUGE/BLEU pero:
  - Ser incoherente
  - Tener errores semánticos

**Conclusión:**  
Estas métricas no garantizan calidad real, solo similitud textual.

---

### e) Curva ROC

- Permite visualizar el rendimiento del modelo en distintos umbrales.
- Mide la relación entre:
  - Tasa de verdaderos positivos (TPR)
  - Tasa de falsos positivos (FPR)

- **AUC (Área bajo la curva):**
  - 1.0 = perfecto
  - 0.5 = aleatorio

**Conclusión:**  
La curva ROC es útil para comparar modelos y seleccionar umbrales óptimos.

---

## 🧪 Intrínseca vs Extrínseca

### 📌 Evaluación intrínseca

- Basada en métricas internas:
  - Accuracy
  - F1
  - ROUGE
  - BLEU

- Mide calidad técnica del modelo.

---

### 📌 Evaluación extrínseca

- Basada en impacto real:
  - Tasa de casos resueltos
  - Tiempo de respuesta
  - Satisfacción del usuario

- Mide utilidad en producción.

---

### ✅ Conclusión

Una métrica intrínseca alta no garantiza impacto real.  
Por eso, es necesario combinar ambas evaluaciones para tomar decisiones correctas.

---

## 🎯 Conclusión general

Las métricas en PLN permiten evaluar modelos desde diferentes perspectivas. Mientras que las métricas intrínsecas ayudan a medir el rendimiento técnico, las métricas extrínsecas reflejan el impacto real en aplicaciones prácticas. La elección de métricas debe alinearse con los objetivos del sistema y el contexto de uso.
