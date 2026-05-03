# Taller 1: De la teoría a la práctica – Implementación efectiva de modelos de IA

## 1. Problema de negocio

Las empresas enfrentan retrasos y errores en la atención al cliente debido al alto volumen de solicitudes manuales. Esto afecta la satisfacción del cliente y aumenta los costos operativos.

Declaración:
**Necesitamos automatizar la clasificación y respuesta de solicitudes para reducir tiempos de atención porque el volumen actual supera la capacidad humana.**

✔ La IA agrega valor al manejar grandes volúmenes de datos mejor que reglas simples.

---

## 2. Objetivos y métricas

**Objetivo principal:**
Reducir el tiempo de respuesta en un 40% en 3 meses.

**Objetivos secundarios:**
- Aumentar la satisfacción del cliente en un 20%
- Reducir costos operativos en un 15%

**Métricas de negocio:**
- Tiempo promedio de respuesta
- Tasa de resolución

**Métricas técnicas:**
- Precisión
- Recall

**Baseline:** 60% precisión  
**Target:** 85% precisión  

---

## 3. Restricciones y riesgos

**Restricciones:**
- Datos incompletos
- Presupuesto limitado
- Tiempo corto

**Riesgos:**
- Sesgo en datos (Alto)
- Baja calidad (Medio)

**Mitigación:**
- Limpieza de datos
- Validación constante

---

## 4. Stakeholders

- Patrocinador: Dirección
- Dueño del proceso: Operaciones
- Usuario final: Agentes
- Soporte técnico: IT

**RACI:**
- Responsable: IT
- Aprobador: Dirección
- Consultado: Operaciones
- Informado: Usuarios

---

## 5. Estrategia de datos

**Fuentes:**
- Base de tickets
- Correos
- Chat

**Tipo:**
- Texto (no estructurado)

**Variables:**
- Tipo de solicitud
- Tiempo de respuesta
- Prioridad
- Cliente

**Partición:**
- 70% entrenamiento
- 15% validación
- 15% prueba

---

## 6. Hipótesis

- El modelo puede clasificar solicitudes con precisión > 80%
- Reduce el tiempo de respuesta en 30%

---

## 7. Selección de modelo

**Opciones:**
- Regresión logística (interpretabilidad)
- Redes neuronales (rendimiento)

**Elección:** modelo de lenguaje básico  
**Plan B:** modelo más simple

---

## 8. Evaluación

- Validación cruzada
- Evitar fuga de datos
- Evaluación de sesgos

---

## 9. Despliegue

- API en tiempo real
- Integración con sistema de tickets

---

## 10. Monitoreo

- Precisión en producción
- Deriva de datos
- Alertas automáticas

**Reentrenamiento:** cada 3 meses

---

## 11. Ética y cumplimiento

- Protección de datos personales
- Transparencia en decisiones
- Supervisión humana

---

## Conclusión

Este caso demuestra cómo la IA puede mejorar procesos operativos de forma eficiente, siempre que se controle la calidad de datos, se monitoree el sistema y se mantenga un enfoque ético en su implementación.
