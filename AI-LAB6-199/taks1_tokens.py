import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "یہ ایک مثال ہے"
]

print("=== TOKENIZATION COMPARISON ===")
for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(f"\nOriginal: {repr(text)}")
    print(f"Whitespace ({len(ws)}): {ws}")
    print(f"Word-like ({len(words)}): {words}")

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    print("\n=== MODEL SUBWORD TOKENIZER ===")
    for text in samples[:3]:
        subwords = model.tokenizer.tokenize(text)
        print(f"{text} -> Subwords: {subwords}")
except Exception as e:
    print("\nSentenceTransformer model not available locally.")