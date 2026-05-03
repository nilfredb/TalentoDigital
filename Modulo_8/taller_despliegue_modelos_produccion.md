# Taller 2: Despliegue de Modelos en Producción – Herramientas y Estrategias

## 1. Contexto del despliegue

El caso de negocio elegido es un modelo de IA para clasificar automáticamente solicitudes de clientes en una empresa de servicios. El modelo será utilizado en producción para identificar si una solicitud corresponde a soporte técnico, facturación, reclamos o información general.

El valor esperado es reducir el tiempo de clasificación, mejorar la precisión en la asignación de tickets y disminuir la carga manual del equipo de atención al cliente.

El despliegue sería **en tiempo real**, ya que cada solicitud debe clasificarse tan pronto como llega al sistema.

---

## 2. Desafíos principales

Principales retos del despliegue:

1. **Integración con sistemas existentes**
2. **Seguridad de los datos**
3. **Escalabilidad del servicio**
4. **Mantenimiento y actualización del modelo**

El reto más crítico es la seguridad, porque el sistema manejará información de clientes. Si falla este punto, podría haber pérdida de confianza, problemas legales y exposición de datos sensibles.

---

## 3. Automatización con scripts y APIs

La automatización permite que el despliegue del modelo sea más rápido, repetible y menos propenso a errores. Por ejemplo, se pueden usar scripts para preparar el entorno, actualizar versiones del modelo o reiniciar servicios.

Una **API REST** sería útil para exponer el modelo y permitir que otros sistemas lo consulten. En este caso, el sistema de tickets enviaría el texto de la solicitud a la API y recibiría como respuesta la categoría asignada.

Esto facilitaría la integración con procesos actuales sin modificar completamente la infraestructura existente.

---

## 4. Servidores ligeros: Flask o FastAPI

Exponer un modelo como servicio web significa permitir que otros sistemas puedan enviar datos al modelo y recibir predicciones mediante una URL o endpoint.

Se requiere respuesta rápida en casos como:

- Clasificación de tickets en tiempo real
- Detección de fraude en transacciones
- Recomendaciones personalizadas
- Chatbots de atención al cliente

Una empresa se beneficiaría de un servicio ligero cuando necesita integrar IA de forma rápida, flexible y con bajo costo inicial.

---

## 5. Infraestructura: local vs. servidores

### Máquinas locales

**Ventajas:**
- Menor costo inicial
- Mayor control directo
- Útil para pruebas internas

**Desventajas:**
- Menor escalabilidad
- Mayor riesgo de fallos físicos
- Difícil mantenimiento en producción

### Servidores dedicados

**Ventajas:**
- Mayor estabilidad
- Mejor escalabilidad
- Más adecuados para producción

**Desventajas:**
- Mayor costo
- Requiere administración técnica
- Puede necesitar configuración de seguridad avanzada

**Decisión conceptual:**  
Para este caso, usaría servidores dedicados o nube, ya que el sistema debe estar disponible constantemente y responder en tiempo real. Una máquina local sería útil solo para pruebas iniciales.

---

## 6. Plataformas en la nube

Servicios como Amazon SageMaker, Google AI Platform o Azure ML permiten desplegar, monitorear y actualizar modelos de IA de manera más organizada.

**Ventajas:**
- Escalabilidad automática
- Reducción de tiempos de despliegue
- Herramientas de monitoreo integradas
- Mayor facilidad para gestionar versiones

Preferiría nube cuando el sistema necesita alta disponibilidad, crecimiento rápido y menor carga de mantenimiento técnico interno. También sería útil si la empresa no cuenta con infraestructura propia suficiente.

---

## 7. Contenedores y orquestación

Docker facilita la portabilidad porque permite empaquetar el modelo, sus dependencias y configuraciones en un mismo contenedor. Esto evita problemas como “funciona en mi computadora, pero no en el servidor”.

Kubernetes aporta escalabilidad y resiliencia, ya que puede ejecutar varios contenedores, reiniciarlos si fallan y distribuir la carga entre múltiples instancias.

**Ejemplo:**  
Si aumenta la cantidad de tickets durante una campaña comercial, el sistema podría escalar creando más instancias del servicio de predicción para responder sin retrasos.

---

## 8. Seguridad y monitoreo

Posibles vulnerabilidades:

- Acceso no autorizado a la API
- Exposición de datos sensibles
- Ataques por solicitudes maliciosas
- Uso de modelos desactualizados

El monitoreo continuo permite detectar errores, caídas, aumentos de latencia o degradación del rendimiento del modelo.

**Métricas a monitorear:**
- Latencia promedio de respuesta
- Tasa de errores de la API
- Volumen de solicitudes
- Precisión del modelo en producción

---

## Conclusión

El despliegue de modelos de IA en producción requiere más que entrenar un buen modelo. Es necesario planificar la infraestructura, la seguridad, la integración, el monitoreo y el mantenimiento continuo. Herramientas como APIs, Docker, Kubernetes y plataformas en la nube permiten que los modelos sean más escalables, confiables y útiles para el negocio.
