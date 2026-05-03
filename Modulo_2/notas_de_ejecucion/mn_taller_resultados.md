# 🧠 Taller (con Python): Redes Generativas Adversarias (GANs)

## 📌 Prerrequisitos
- Python 3.9+ instalado  
- Conocimientos básicos de tensores, redes neuronales y backpropagation  
- Familiaridad mínima con PyTorch  
- Computador con CPU (opcional GPU) y 3–4 GB RAM libres  

## ⏱️ Duración
30 minutos  

## 🎯 Objetivo
Construir, entrenar y evaluar una mini-GAN en PyTorch sobre MNIST, observando la interacción entre Generador y Discriminador y analizando su comportamiento.

---

## 3️⃣ Ejercicios guiados (resueltos)

### a) Cambio de `Z_DIM`

- Con `Z_DIM = 16`:  
  Se observa menor diversidad en las imágenes generadas. El generador tiene menos capacidad para representar variabilidad en los datos.

- Con `Z_DIM = 128`:  
  Aumenta la diversidad de las muestras, ya que el espacio latente es más amplio. Sin embargo, también puede hacer el entrenamiento más inestable si no se ajustan otros parámetros.

👉 **Conclusión:**  
Un `Z_DIM` mayor mejora la diversidad, pero requiere mayor estabilidad en el entrenamiento.

---

### b) Sustitución de `LeakyReLU` por `ReLU`

- Con `ReLU`:  
  Se observa menor estabilidad durante el entrenamiento. Algunas neuronas dejan de activarse (problema de “dead neurons”), lo que afecta la capacidad del modelo.

- Con `LeakyReLU`:  
  El entrenamiento es más estable y consistente, ya que evita que las neuronas queden completamente inactivas.

👉 **Conclusión:**  
`LeakyReLU` es preferible en GANs por su estabilidad.

---

### c) Ajuste de `LR`

- Con `LR = 1e-3`:  
  El entrenamiento se vuelve inestable. El discriminador aprende demasiado rápido y el generador no logra mejorar, provocando colapso de modo.

- Con `LR = 5e-5`:  
  El entrenamiento es más estable, pero más lento. El generador mejora gradualmente.

👉 **Conclusión:**  
Un learning rate intermedio (como `2e-4`) ofrece mejor equilibrio entre estabilidad y velocidad.

---

### d) Incremento de `EPOCHS`

- Con más épocas (`EPOCHS = 5`):  
  Las imágenes generadas mejoran en calidad progresivamente.

- Riesgo:  
  Si se entrena demasiado, puede aparecer colapso de modo o sobreajuste.

👉 **Conclusión:**  
Más entrenamiento mejora resultados, pero requiere monitoreo constante.

---

### e) Uso de DCGAN

- Con MLP:  
  Las imágenes son más borrosas y menos estructuradas.

- Con DCGAN:  
  Las imágenes tienen mejor calidad visual, mayor coherencia espacial y mejor representación de patrones.

👉 **Conclusión:**  
Las arquitecturas convolucionales son superiores para datos de imágenes.

---

## 4️⃣ Señales de colapso de modo

Durante el entrenamiento se pueden identificar:

- Imágenes generadas muy similares entre sí  
- Baja pérdida del generador sin mejora visual  
- Discriminador dominante (alta precisión constante)  
- Oscilaciones fuertes en pérdidas sin progreso real  

👉 **Interpretación:**  
El generador deja de explorar nuevas soluciones y se queda atrapado en patrones repetitivos.

---

## 5️⃣ Reflexión final

1. **Mejor combinación encontrada:**  
   - `LR = 2e-4`  
   - `Z_DIM = 64`  
   - `LeakyReLU`  
   Esta combinación ofrece buen equilibrio entre estabilidad y diversidad.

2. **Impacto del LR en la dinámica G/D:**  
   - LR alto: el discriminador domina rápidamente  
   - LR bajo: entrenamiento estable pero lento  
   - LR equilibrado: ambos modelos aprenden de forma competitiva  

3. **Mejoras para datasets complejos (CIFAR-10):**
   - Uso de DCGAN o arquitecturas más profundas  
   - Batch Normalization  
   - Regularización  
   - Mayor número de épocas  
   - Uso de GPU  
   - Ajuste fino de hiperparámetros  

---

## 🧾 Conclusión general

Las GANs permiten generar datos realistas mediante una competencia entre dos redes neuronales. Sin embargo, su entrenamiento es delicado y requiere un balance cuidadoso entre el generador y el discriminador. Factores como la arquitectura, la tasa de aprendizaje y el tamaño del espacio latente influyen directamente en la calidad de los resultados. El uso de arquitecturas convolucionales y parámetros adecuados permite mejorar significativamente la estabilidad y la diversidad de las muestras generadas.

---

## 🚀 Bonus

Para mejorar este proyecto:

- Implementar DCGAN completa  
- Añadir métricas como FID  
- Guardar checkpoints del modelo  
- Visualizar evolución del entrenamiento  