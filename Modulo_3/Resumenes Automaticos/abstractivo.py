from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

MODEL = "sshleifer/distilbart-cnn-12-6"  # ligero y rápido
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

def resumir_abstractive(texto, max_palabras=120):
    # max_length está en tokens; ajusta según tu texto
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    out = summarizer(
        texto,
        max_length=180,    # prueba 120-220
        min_length=60,
        do_sample=False
    )
    return out[0]["summary_text"]

if __name__ == "__main__":
    with open("texto_largo.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(resumir_abstractive(texto))
