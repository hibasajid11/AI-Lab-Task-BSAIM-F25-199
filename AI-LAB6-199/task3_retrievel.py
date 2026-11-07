import json, time, csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks

def create_sample_files():
    docs = {
        "late": "Late submission is normally penalized. Illness extensions require medical evidence before the deadline.",
        "password": "Reset a forgotten password using the recovery link. Never share recovery codes with anyone.",
        "assignment": "Upload assignments through the learning portal. Submit the final file as a PDF document.",
        "contractor": "Contractors can work remotely only if the signed contract permits it. Employee rules do not apply.",
        "printer": "For blank printer pages, check ink levels and run the cleaning utility. Print a test page afterwards."
    }
    queries = [
        {"query": "What is required for illness extensions?", "doc": "late", "evidence": "Illness extensions require medical evidence before the deadline.", "split": "dev"},
        {"query": "How do I reset a forgotten password?", "doc": "password", "evidence": "Reset a forgotten password using the recovery link.", "split": "dev"},
        {"query": "Where do I upload assignments?", "doc": "assignment", "evidence": "Upload assignments through the learning portal.", "split": "dev"},
        {"query": "Can contractors work remotely?", "doc": "contractor", "evidence": "Contractors can work remotely only if the signed contract permits it.", "split": "dev"},
        {"query": "What do I do for blank printer pages?", "doc": "printer", "evidence": "For blank printer pages, check ink levels and run the cleaning utility.", "split": "test"},
        {"query": "How can I recover my login access?", "doc": "password", "evidence": "Reset a forgotten password using the recovery link.", "split": "test"},
        {"query": "How should I hand in my coursework?", "doc": "assignment", "evidence": "Upload assignments through the learning portal.", "split": "test"},
        {"query": "What proof is needed when I was ill?", "doc": "late", "evidence": "Illness extensions require medical evidence before the deadline.", "split": "test"},
        {"query": "What are tomorrow's flight prices?", "doc": None, "evidence": None, "split": "test"},
        {"query": "Who won the football match?", "doc": None, "evidence": None, "split": "test"}
    ]
    with open("corpus.json", "w") as f: json.dump(docs, f, indent=2)
    with open("queries.json", "w") as f: json.dump(queries, f, indent=2)

def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [rank for rank, i in enumerate(top, 1) if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]]
        hits.append(bool(good))
        reciprocal.append(1 / good[0] if good else 0)
    return (float(np.mean(hits)), float(np.mean(reciprocal))) if hits else (None, None)

if __name__ == "__main__":
    create_sample_files()
    with open("corpus.json") as f: docs = json.load(f)
    with open("queries.json") as f: items = json.load(f)
    
    chunks = make_chunks(docs, "sentence")
    texts = [c["text"] for c in chunks]
    query_texts = [q["query"] for q in items]
    
    vec = TfidfVectorizer()
    C = vec.fit_transform(texts)
    Q = vec.transform(query_texts)
    scores = (Q @ C.T).toarray()
    
    hit, mrr = evaluate(scores, chunks, items)
    print(f"Evaluation Results (TF-IDF Baseline): Hit@3 = {hit:.3f}, MRR@3 = {mrr:.3f}")