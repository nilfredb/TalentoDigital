from rouge_score import rouge_scorer
import sacrebleu

# textos de ejemplo (puedes cambiarlos por tus pares reales)
referencia = (
    "La traducción neuronal mejora la fluidez y el contexto al interpretar secuencias completas, "
    "reduciendo errores frecuentes de los métodos estadísticos tradicionales."
)
candidato1 = (
    "La traducción con redes neuronales mejora la fluidez y el contexto al considerar oraciones completas, "
    "y reduce errores comunes de los enfoques estadísticos."
)
candidato2 = (
    "Los métodos antiguos de traducción no sirven. El nuevo sistema es mejor."
)

# 1) ROUGE-1/2/L
scorer = rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'], use_stemmer=True)
for i, cand in enumerate([candidato1, candidato2], start=1):
    scores = scorer.score(referencia, cand)
    f1s = {k: round(v.fmeasure, 4) for k, v in scores.items()}
    print(f"Candidato {i} — ROUGE:", f1s)

# 2) BLEU (n-grama hasta 4)
#    sacrebleu espera listas: hipótesis y referencias (puede haber múltiples referencias)
bleu1 = sacrebleu.corpus_bleu([candidato1], [[referencia]])
bleu2 = sacrebleu.corpus_bleu([candidato2], [[referencia]])
print("Candidato 1 — BLEU:", round(bleu1.score, 2))
print("Candidato 2 — BLEU:", round(bleu2.score, 2))

print("Interpretación: mayores ROUGE/BLEU indican mayor solapamiento con la referencia (no necesariamente mejor calidad semántica).")
