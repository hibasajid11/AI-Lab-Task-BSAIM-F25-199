# Lab 2 AI - Classroom Control Agent

This project contains a simple Python agent that decides a classroom HVAC target mode based on temperature and occupancy, and avoids sending duplicate commands when the target mode does not change.

## Setup

1. Open the project folder in VS Code.
2. Make sure Python is installed.
3. You can use the default Python interpreter in VS Code.

## Run the program

Open a terminal in the project folder and run:

```bash
python model.py
```

On Windows PowerShell, this also works:

```powershell
python .\model.py
```

## What the script does

- Checks occupancy first.
- If the room is empty, target mode is `ECO`.
- If the room is occupied:
  - `temp > 26` -> `COOL`
  - `temp < 20` -> `WARM`
  - otherwise -> `IDLE`
- Prevents sending the same command repeatedly if the target mode is unchanged.
- Prints the previous mode, percept, target mode, and whether a command was sent.

## Expected output

The program prints lines like:

```text
Step 1 | Previous Mode: None | Percept: (29, True) | Target: COOL | Command Sent: True
Step 2 | Previous Mode: COOL | Percept: (29, True) | Target: COOL | Command Sent: False
```

## File

- `model.py` - main agent logic and test cases
