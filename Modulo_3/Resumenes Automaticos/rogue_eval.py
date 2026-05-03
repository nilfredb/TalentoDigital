from rouge_score import rouge_scorer

def rouge_scores(referencia, candidato):
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
    scores = scorer.score(referencia, candidato)
    return {k: v.fmeasure for k, v in scores.items()}

if __name__ == "__main__":
    # Crea un 'resumen de referencia' manual breve (3-5 frases) en referencia.txt
    with open("referencia.txt", "r", encoding="utf-8") as f: ref = f.read()
    with open("resumen_extractivo.txt", "r", encoding="utf-8") as f: ext = f.read()
    with open("resumen_abstractivo.txt", "r", encoding="utf-8") as f: abs = f.read()
    print("ROUGE extractivo:", rouge_scores(ref, ext))
    print("ROUGE abstractivo:", rouge_scores(ref, abs))
