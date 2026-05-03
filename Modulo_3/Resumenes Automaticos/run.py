from extractivo import resumir_extractive
from abstractivo import resumir_abstractive

if __name__ == "__main__":
    texto_path = "texto_largo.txt"
    resumen_ext = resumir_extractive(texto_path, num_sent=6)
    with open("resumen_extractivo.txt", "w", encoding="utf-8") as f: f.write(resumen_ext)

    with open(texto_path, "r", encoding="utf-8") as f: texto = f.read()
    resumen_abs = resumir_abstractive(texto)
    with open("resumen_abstractivo.txt", "w", encoding="utf-8") as f: f.write(resumen_abs)

    print("Listo. Archivos: resumen_extractivo.txt, resumen_abstractivo.txt")
