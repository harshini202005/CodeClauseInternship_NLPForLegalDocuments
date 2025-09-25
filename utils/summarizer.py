from transformers import pipeline, BartTokenizer
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

SUMMARIZER = pipeline("summarization", model="facebook/bart-large-cnn")
TOKENIZER = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
MAX_TOKENS = 1024  

def chunk_text(text, max_tokens=MAX_TOKENS):
    sentences = sent_tokenize(text)
    chunks = []
    current = []
    current_tokens = 0

    for s in sentences:
        token_count = len(TOKENIZER.tokenize(s))
        if current_tokens + token_count <= max_tokens:
            current.append(s)
            current_tokens += token_count
        else:
            if current:
                chunks.append(" ".join(current))
            current = [s]
            current_tokens = token_count

    if current:
        chunks.append(" ".join(current))

    return chunks

def summarize_text(text, max_length=150, min_length=30):
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        out = SUMMARIZER(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summaries.append(out[0]["summary_text"])

    if len(summaries) == 1:
        return summaries[0]
    else:
        combined = " ".join(summaries)
        final = SUMMARIZER(combined, max_length=max_length, min_length=min_length, do_sample=False)
        return final[0]["summary_text"]
