# Rule Evaluation Script

This project contains a small Python script that compares two decision rules:

- `symbolic(score, complete)`
- `threshold(probability)`

It prints whether the two rules agree for several sample cases.

## Setup

1. Make sure Python is installed on your system.
2. Open a terminal in the project folder.
3. If needed, create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

## Run the script

From the project folder, run:

```bash
python rules.py
```

## Expected output

```text
case | symbolic | threshold | disagreement
complete_high | Review | Review | False
complete_low | Hold | Review | True
incomplete_high | Hold | Review | True
boundary | Review | Review | False
```

## File description

- `rules.py` — contains the logic and sample test cases.

## Notes

This script is intended for learning and quick validation of simple decision logic. If you want, you can extend it with additional test cases or turn it into a reusable function-based program.
