# Modelos de Lenguaje Avanzados con Transformers

## Introducción

Los modelos de lenguaje avanzados son sistemas basados en arquitecturas de Deep Learning, especialmente Transformers, capaces de comprender, analizar y generar texto en lenguaje natural. Estos modelos se utilizan en múltiples aplicaciones como análisis de sentimiento, chatbots, búsqueda semántica y clasificación de texto.

En este taller se utilizó un modelo preentrenado (DistilBERT) junto con un dataset de IMDb para explorar su funcionamiento en tareas de clasificación.

---

## 1) Preparación del entorno

Se creó un entorno virtual y se instalaron las librerías necesarias:

```bash
pip install transformers datasets torch
```

Librerías utilizadas:

- transformers → modelos preentrenados
- datasets → carga de datasets
- torch → manejo de tensores y ejecución del modelo

---

## 2) Carga del modelo y tokenizador

Se utilizó el modelo:

- distilbert-base-uncased

Este es un modelo más ligero que BERT, ideal para pruebas rápidas.

El tokenizador convierte el texto en números (tokens) que el modelo puede procesar.

---

## 3) Preparación del dataset

Se utilizó el dataset IMDb (subconjunto de 2000 ejemplos):

- 0 → sentimiento negativo
- 1 → sentimiento positivo

Esto permite trabajar rápido sin necesidad de muchos recursos.

---

## 4) Tokenización y DataLoader

El texto fue transformado en:

- input_ids
- attention_mask

Se aplicó padding y truncation para mantener tamaños consistentes.

---

## 5) Definición del modelo

Se utilizó un modelo de clasificación basado en DistilBERT con dos salidas:

- positivo
- negativo

Este enfoque aprovecha el aprendizaje previo del modelo (transfer learning).

---

## 6) Entrenamiento

Durante el entrenamiento:

- Se calculó la pérdida (loss)
- Se generaron logits (predicciones sin normalizar)
- El modelo comenzó a ajustar sus pesos

Incluso con pocas iteraciones, el modelo logra resultados aceptables gracias al preentrenamiento.

---

## 7) Evaluación

Se evaluó el modelo usando accuracy:

- Accuracy = predicciones correctas / total

El modelo logra buen rendimiento incluso con pocos datos.

---

## 8) Embeddings de texto

Los embeddings representan el significado del texto en forma numérica.

Ejemplo:

- "This movie was amazing"
- "I loved this film"

→ embeddings similares

- "This movie was terrible"

→ embedding diferente

Aplicaciones:

- búsqueda semántica
- sistemas de recomendación
- detección de similitud

---

## 9) Aplicaciones reales

- Chatbots
- Análisis de sentimiento
- Clasificación automática de textos
- Motores de búsqueda inteligentes

---

## 10) Reflexión

Estos modelos son muy potentes porque permiten reutilizar conocimiento previo. Sin embargo, presentan desafíos:

- consumo de recursos
- sesgos en los datos
- falta de interpretabilidad

Es importante utilizarlos como apoyo y no como sustituto total del juicio humano.

---

## Conclusión

Los modelos de lenguaje avanzados son herramientas clave en la IA moderna. Permiten resolver múltiples tareas con alta precisión y poco entrenamiento adicional. Su uso responsable es fundamental para maximizar sus beneficios y minimizar riesgos.
