from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def resumir_extractive(ruta, num_sent=5, idioma="spanish"):
    parser = PlaintextParser.from_file(ruta, Tokenizer(idioma))
    summarizer = TextRankSummarizer()
    sents = summarizer(parser.document, num_sent)
    return " ".join(str(s) for s in sents)

if __name__ == "__main__":
    print(resumir_extractive("texto_largo.txt", num_sent=6))