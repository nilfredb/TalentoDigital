# 🧠 Taller: Redes Neuronales Recurrentes (RNN) y LSTM

## 📌 Prerrequisitos
- Conocimientos básicos de redes neuronales feedforward.
- Familiaridad con el concepto de gradiente y retropropagación.
- Comprensión general de problemas de secuencia (series de tiempo o NLP).

## ⏱️ Duración
30 minutos

## 🎯 Objetivo
Al finalizar este taller, el estudiante comprenderá el funcionamiento de las Redes Neuronales Recurrentes (RNN) y las Long Short-Term Memory (LSTM), identificando sus diferencias clave y aplicando ejemplos conceptuales en problemas de secuencia.

---

## 1. 🔄 Redes Feedforward vs Datos Secuenciales

Las redes neuronales tradicionales (feedforward) procesan cada entrada de forma independiente.  
Esto es un problema cuando el **orden importa**.

### Ejemplos:
- Predicción de palabras:  
  *"El clima de hoy es ___"*
- Series de tiempo: temperaturas, precios, etc.

👉 Estas redes **no tienen memoria**, por lo que no capturan contexto.

---

## 2. 🔁 ¿Qué es una RNN?

Las **Redes Neuronales Recurrentes (RNN)** introducen **memoria temporal**.

Cada paso utiliza:
- La entrada actual
- La información del paso anterior

### Idea clave:
> La salida de un paso se convierte en entrada del siguiente.

Esto permite modelar secuencias como:
- Texto
- Audio
- Series temporales

---

## 3. ⚠️ Problema del Gradiente

### 🔻 Desvanecimiento del gradiente
- El gradiente se vuelve muy pequeño
- La red olvida información lejana

### 🔺 Explosión del gradiente
- El gradiente crece demasiado
- Entrenamiento inestable

👉 Resultado:  
Las RNN tradicionales tienen dificultades con **dependencias a largo plazo**.

---

## 4. 🧩 ¿Qué es una LSTM?

Las **LSTM (Long Short-Term Memory)** son una mejora de las RNN.

👉 Permiten decidir:
- Qué recordar
- Qué olvidar
- Qué usar en la salida

### 🔐 Componentes principales (puertas)

#### 🚪 Puerta de olvido
Descarta información innecesaria.

#### 🚪 Puerta de entrada
Guarda nueva información relevante.

#### 🚪 Puerta de salida
Controla qué se usa para la salida.

---

### 🧠 Analogía

Como tomar apuntes:
- Borras lo irrelevante
- Guardas lo importante
- Usas lo necesario en el momento

---

## 5. 🔄 Flujo de una celda LSTM

1. Llega la entrada actual
2. Se decide qué olvidar
3. Se decide qué guardar
4. Se actualiza la memoria
5. Se genera la salida

👉 Hay dos estados:
- Estado de celda (memoria larga)
- Estado oculto (salida inmediata)

---

## 6. ✍️ Ejemplo práctico

Frase:

> **"El clima de hoy es ___"**

### La LSTM debería recordar:
- "clima" → contexto meteorológico
- "hoy" → tiempo presente

### Debería ignorar:
- Información irrelevante previa

### Posibles predicciones:
- soleado
- lluvioso
- frío
- agradable

---

## 7. 🌍 Aplicaciones reales

### 📈 Finanzas
Predicción de precios y tendencias

### 🌐 Traducción automática
Interpretación de contexto en frases

### 🎤 Asistentes de voz
Reconocimiento de lenguaje hablado

### ⌨️ Autocompletado
Predicción de texto

### 📊 Series temporales
Clima, tráfico, sensores

---

## 8. 🧾 Reflexión final

Las RNN introdujeron el concepto de memoria en redes neuronales, pero presentan limitaciones importantes debido al desvanecimiento y explosión del gradiente. Las LSTM solucionan este problema mediante un sistema de puertas que regula el flujo de información, permitiendo capturar dependencias a largo plazo. Gracias a esto, son ampliamente utilizadas en tareas como procesamiento de lenguaje natural, predicción de series temporales y sistemas inteligentes.

---

## 📊 Comparación RNN vs LSTM

| Característica | RNN | LSTM |
|------|-----|------|
| Memoria | Limitada | Robusta |
| Dependencias largas | Difícil | Eficiente |
| Gradiente | Problemas comunes | Mejor manejo |
| Complejidad | Baja | Mayor |
| Uso | Secuencias simples | Secuencias complejas |

---

## 🚀 Bonus (opcional)

Puedes complementar este taller con:
- Diagramas de LSTM
- Ejemplos en PyTorch o TensorFlow
- Visualizaciones de secuencias

---