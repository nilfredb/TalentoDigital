"""
Objetivo: mostrar que una métrica intrínseca alta no siempre implica impacto real (extrínseco).
Se simula un clasificador de intenciones para un bot de soporte con 3 intenciones críticas:
 - 'reset_password', 'refund', 'track_order'.
Se miden F1 (intrínseca) y una métrica 'tasas_resueltas' (extrínseca).
"""

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import numpy as np

X = [
    "olvidé mi contraseña", "no puedo entrar a mi cuenta", "resetear contraseña", "reiniciar password",
    "quiero reembolso", "devolver producto", "solicitar devolución", "quiero mi dinero de vuelta",
    "seguimiento de pedido", "dónde está mi orden", "estado del envío", "rastrea mi pedido"
]
y = [
    "reset_password","reset_password","reset_password","reset_password",
    "refund","refund","refund","refund",
    "track_order","track_order","track_order","track_order"
]

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=200))
])
pipe.fit(Xtr, ytr)

yp = pipe.predict(Xte)
f1 = f1_score(yte, yp, average="macro")

# Métrica extrínseca simulada: si se predice intención correcta, se considera "caso resuelto";
# si es incorrecta, el bot hace handoff y no resuelve.
resolved = np.mean(yp == yte)

print(f"F1 macro (intrínseca): {f1:.2f}")
print(f"Tasa de casos resueltos (extrínseca): {resolved:.2f}")
print("Conclusión: ambas métricas son útiles; la extrínseca captura impacto operativo real.")
