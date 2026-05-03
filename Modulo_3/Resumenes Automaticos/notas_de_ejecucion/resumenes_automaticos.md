# 🧠 Taller: Resúmenes Automáticos — Extractivo vs Abstractivo

## 📄 Texto de referencia

La inteligencia artificial está transformando diversos sectores como la salud y las finanzas mediante el análisis de datos. Permite mejorar diagnósticos médicos y detectar fraudes en tiempo real. Sin embargo, plantea desafíos como la privacidad, el sesgo y el impacto en el empleo. Su desarrollo futuro dependerá de una regulación responsable.

---

## 🔍 7) Experimentos y reflexión

### a) Cambio de `num_sent` en el resumen extractivo

Al modificar la cantidad de oraciones:

- **num_sent = 4**
  - El resumen es más corto y directo.
  - Puede omitir ideas importantes del texto original.
  - Útil para resúmenes rápidos.

- **num_sent = 8**
  - El resumen es más completo.
  - Puede incluir información redundante.
  - Mayor fidelidad al texto original.

**Conclusión:**  
Existe un equilibrio entre brevedad y cobertura de información.

---

### b) Ajuste de `max_length` y `min_length` en el resumen abstractivo

- **max_length bajo (120):**
  - Resumen más corto.
  - Menos contexto y detalle.

- **max_length alto (180–220):**
  - Más información.
  - Mayor fluidez y coherencia.

- **min_length:**
  - Evita resúmenes demasiado breves.
  - Asegura un mínimo de contenido.

**Conclusión:**  
Estos parámetros influyen directamente en la **longitud, fluidez y calidad** del resumen generado.

---

### c) Uso de estrategia map-reduce (dividir el texto)

**Ventajas:**
- Permite procesar textos largos.
- Evita límites de tokens del modelo.
- Mejora el rendimiento.

**Desventajas:**
- Puede perder coherencia global.
- Requiere un segundo resumen para consolidar.

**Conclusión:**  
Es útil para textos extensos, pero debe aplicarse con cuidado.

---

### d) Comparación con ROUGE

Resultados esperados:

- **Resumen extractivo:**
  - Mayor puntuación ROUGE.
  - Más coincidencia con el texto original.

- **Resumen abstractivo:**
  - Menor puntuación ROUGE.
  - Mayor naturalidad y legibilidad.

**Conclusión:**  
ROUGE favorece el enfoque extractivo porque mide coincidencias textuales, no calidad semántica.

---

### e) Casos de uso: extractivo vs abstractivo

#### 📌 Resumen extractivo
Se recomienda en:
- Informes legales
- Documentación técnica
- Auditorías
- Casos donde no se debe alterar el contenido

#### 📌 Resumen abstractivo
Se recomienda en:
- Reportes ejecutivos
- Noticias
- Presentaciones
- Contenido orientado a usuarios finales

---

## ✅ Conclusión general

La elección entre resumen extractivo y abstractivo depende del contexto. El enfoque extractivo es más adecuado cuando se requiere mantener la fidelidad al texto original, mientras que el abstractivo es ideal para generar contenido más natural y comprensible. Aunque el extractivo suele obtener mejores métricas ROUGE, el abstractivo ofrece mayor legibilidad y coherencia.
