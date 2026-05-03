import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix,
                             roc_auc_score)
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

RANDOM_SEED = 42

# 1) Dataset: selecciona 3 categorías para acelerar (requiere internet la 1ra vez)
cats = ['sci.space', 'rec.sport.baseball', 'talk.politics.mideast']
data = fetch_20newsgroups(subset='train', categories=cats, remove=('headers','footers','quotes'))
X_train, X_val, y_train, y_val = train_test_split(data.data, data.target, test_size=0.25, random_state=RANDOM_SEED, stratify=data.target)

# 2) Pipeline: TF-IDF + Regresión Logística (probabilidades → ROC-AUC)
pipe = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), min_df=3, max_df=0.9)),
    ('clf', LogisticRegression(max_iter=200, solver='liblinear', multi_class='ovr'))
])
pipe.fit(X_train, y_train)

# 3) Métricas de clasificación
y_pred = pipe.predict(X_val)
acc = accuracy_score(y_val, y_pred)
print(f"Accuracy: {acc:.3f}")
print(classification_report(y_val, y_pred, target_names=cats))
print("Matriz de confusión:\n", confusion_matrix(y_val, y_pred))

# 4) ROC-AUC (macro) con one-vs-rest (necesita probas)
#    OJO: Para multi-clase, roc_auc_score requiere probas shape [n_samples, n_classes]
probas = pipe.predict_proba(X_val)
auc_macro_ovr = roc_auc_score(y_val, probas, multi_class='ovr', average='macro')
print(f"ROC-AUC macro (OvR): {auc_macro_ovr:.3f}")

# 5) (Opcional) Curva ROC para un caso binario: filtra 2 clases
#   Ejemplo: 'sci.space' (0) vs 'rec.sport.baseball' (1)
from sklearn.preprocessing import label_binarize
mask_bin = np.isin(y_val, [0,1])
y_bin = y_val[mask_bin]
X_bin = np.array(X_val, dtype=object)[mask_bin]
probas_bin = pipe.predict_proba(X_bin)[:, [0,1]]
y_bin_b = label_binarize(y_bin, classes=[0,1]).ravel()

from sklearn.metrics import roc_curve, auc
fpr, tpr, _ = roc_curve(y_bin_b, probas_bin[:,1])
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.2f})")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate"); plt.title("Curva ROC (binaria)")
plt.legend()
plt.savefig("roc_binary.png", dpi=150)
print("Gráfica guardada: roc_binary.png")
