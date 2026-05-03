# Taller: Comparación Adam vs RMSProp

## 4) Ejercicios guiados (respuestas)

### a) Sensibilidad al LR
Al probar diferentes tasas de aprendizaje (lr=5e-4 y lr=5e-3):

- **Adam**:
  - Con lr=5e-4: entrenamiento más estable, pero más lento.
  - Con lr=5e-3: puede volverse inestable, pero aún converge en algunos casos.
- **RMSProp**:
  - Con lr=5e-4: estable pero más lento que Adam.
  - Con lr=5e-3: mayor inestabilidad, pérdidas oscilantes.

✅ **Conclusión**: Adam es más robusto a cambios en el learning rate y converge más rápido en general.

---

### b) Momentos en Adam
Probando betas:

- (0.9, 0.95):
  - Menor memoria del gradiente pasado.
  - Más adaptativo, pero más ruido.
- (0.5, 0.999):
  - Mucho peso al pasado.
  - Entrenamiento más lento pero más estable.

✅ **Conclusión**: 
- Betas estándar (0.9, 0.999) ofrecen el mejor balance.
- Reducir beta2 aumenta sensibilidad al ruido.

---

### c) Decaimiento de peso (weight_decay)
- Con weight_decay=1e-4:
  - Mejora ligera en validación.
  - Reduce overfitting.
- Con weight_decay=0:
  - Mayor ajuste al entrenamiento.
  - Peor generalización.

✅ **Conclusión**: 
El weight decay mejora la generalización al penalizar pesos grandes.

---

### d) Alpha en RMSProp
- alpha=0.95:
  - Más reactivo a cambios recientes.
  - Más ruido en el entrenamiento.
- alpha=0.999:
  - Más suavizado.
  - Menos ruido, pero más lento.

✅ **Conclusión**:
Alpha controla el "promedio móvil":
- Bajo → más adaptativo.
- Alto → más estable.

---

### e) Clip de gradiente
- Con clip:
  - Entrenamiento estable.
  - Evita explosión de gradientes.
- Sin clip:
  - Posibles oscilaciones grandes.
  - Pérdidas inestables.

✅ **Conclusión**:
El gradient clipping mejora significativamente la estabilidad.

---

## 5) Interpretación rápida

### Convergencia
- Adam alcanza el mínimo más rápido.
- RMSProp tarda más en estabilizarse.

### Estabilidad
- Adam: más estable en general.
- RMSProp: puede tener más fluctuaciones.

### Robustez al LR
- Adam tolera mejor cambios en LR.
- RMSProp es más sensible.

### Generalización
- Ambos pueden generalizar bien.
- Adam suele obtener mejor val_acc en menos tiempo.

### Tiempo
- Adam suele ser ligeramente más rápido en convergencia efectiva.

---

## 6) Conclusión general

- **Adam**:
  - Más rápido
  - Más robusto
  - Mejor elección por defecto

- **RMSProp**:
  - Útil en problemas específicos (ej. secuencias)
  - Más sensible a hiperparámetros

👉 **Recomendación**: usar Adam como baseline y ajustar RMSProp solo si es necesario.

---

## Resumen final

Adam domina en:
- velocidad
- estabilidad
- facilidad de uso

RMSProp requiere más ajuste pero sigue siendo útil en escenarios concretos.