# Lab 6: Text Processing and Retrieval

This lab contains three tasks: comparing tokenization methods, creating overlapping or sentence-based text chunks, and evaluating a TF-IDF retrieval baseline.

## Requirements

- Python 3
- NumPy and scikit-learn for Task 3
- Task 1's SentenceTransformer tokenizer is optional; if its model is unavailable locally, the script reports that and still completes the basic tokenization comparison.

Install the Task 3 dependencies if needed:

```powershell
python -m pip install numpy scikit-learn
```

## Run the tasks

Run these commands from this folder:

```powershell
python .\taks1_tokens.py
python .\task2_chunks.py
python .\task3_retrievel.py
```

## Files

- `taks1_tokens.py` — compares whitespace, word-like, and optional subword tokenization.
- `task2_chunks.py` — demonstrates fixed-window and sentence-based text chunking.
- `task3_retrievel.py` — evaluates a TF-IDF retrieval baseline. It creates `corpus.json` and `queries.json` when run.
- `output\` — contains the captured output for each task.
