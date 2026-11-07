import re

def word_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]

def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not (0 <= overlap < size):
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    spans = word_spans(text)
    if not spans:
        return []
    result = []
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result

def sentence_chunks(text, size=40):
    if size <= 0:
        raise ValueError("size must be positive")
    cuts = [0] + [m.end() for m in re.finditer(r"[.!?]\s+", text)] + [len(text)]
    out, pending, count = [], None, 0
    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if not n:
            continue
        if n > size:
            if pending is not None:
                out.append(pending)
            out.extend(windows(segment, size, 0, a))
            pending, count = None, 0
        elif pending is not None and count + n <= size:
            pending, count = (pending[0], b), count + n
        else:
            if pending is not None:
                out.append(pending)
            pending, count = (a, b), n
    if pending is not None:
        out.append(pending)
    return out

def make_chunks(docs, strategy):
    result = []
    for doc_id, text in docs.items():
        if strategy == "sentence":
            spans = sentence_chunks(text)
        else:
            spans = windows(text, size=40, overlap=int(strategy))
        for i, (a, b) in enumerate(spans):
            result.append(dict(id=f"{doc_id}:{i}", doc=doc_id, start=a, end=b, text=text[a:b]))
    return result

if __name__ == "__main__":
    docs = {"test_doc": "Late submission is normally penalized. Illness extensions require medical evidence before the deadline. Ask the coordinator first."}
    for strat in ["0", "10", "sentence"]:
        print(f"\n--- Strategy: {strat} ---")
        chunks = make_chunks(docs, strat)
        for c in chunks:
            print(c)