# Taller 3: MLOps – Estrategias para la Operacionalización y Monitoreo

## 1. Definición de MLOps

MLOps es el conjunto de prácticas que permite llevar modelos de machine learning desde desarrollo hasta producción de forma sostenible, automatizada y monitoreada.

Es importante porque evita que los modelos queden como prototipos sin uso real en el negocio.

**Beneficios:**
- Mejora continua del modelo
- Mayor confiabilidad y estabilidad

---

## 2. Ciclo de vida de ML

Etapas:
- Preparación de datos  
- Entrenamiento  
- Validación  
- Despliegue  
- Monitoreo  

**Etapa crítica:** preparación de datos  
Si los datos son incorrectos, el modelo fallará.

---

## 3. DevOps vs MLOps

- DevOps: enfocado en software  
- MLOps: incluye datos y modelos  

MLOps es necesario porque los modelos cambian con el tiempo (deriva de datos).

---

## 4. Herramientas

- MLflow: gestión de experimentos y modelos  
- Kubeflow: pipelines y despliegue  

**Elección:** MLflow por simplicidad y control de versiones.

---

## 5. Arquitectura

Escalable: puede crecer con más datos  
Reproducible: resultados consistentes  

Sin reproducibilidad:
- Resultados inconsistentes
- Difícil debugging

---

## 6. Pipelines

Un pipeline es un flujo automatizado de datos y modelos.

Ejemplo:
Datos → Limpieza → Entrenamiento → Evaluación → Despliegue

---

## 7. Estrategias de despliegue

- Batch: procesamiento por lotes  
- Tiempo real: respuestas inmediatas  

**Elección:** tiempo real para atención al cliente.

---

## 8. Automatización

Automatizar:
- Entrenamiento
- Evaluación
- Despliegue

Reduce errores y acelera procesos.

---

## 9. Versionado

Importante para:
- Controlar cambios
- Reproducir resultados

Sin versionado:
- Pérdida de control
- Errores difíciles de rastrear

---

## 10. Monitoreo

Métricas:
- Precisión  
- Latencia  
- Deriva de datos  

Reentrenar cuando:
- Baja precisión
- Cambian los datos

---

## Conclusión

MLOps permite mantener modelos útiles y confiables en producción. Las prácticas más críticas son el monitoreo continuo y el versionado, ya que garantizan que el modelo se mantenga actualizado y controlado en el tiempo.
