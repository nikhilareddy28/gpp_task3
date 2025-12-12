# Custom CSV Reader & Writer

This project implements a custom CSV Reader and CSV Writer in Python, comparing their performance against Python’s built-in `csv` module.

It includes:
- A custom CSV reader written from scratch
- A custom CSV writer written from scratch
- Benchmarks comparing custom vs built-in CSV performance
- Tests on small (10,000 rows) and large (1,000,000 rows) CSV files

The goal is to understand how CSV parsing works internally and measure performance differences between pure Python and optimized CSV libraries.



Here is your **project structure in clean, correct, professional Markdown format**:

---

## 📁 Project Structure

```
custom-csv/
│
├── README.md  
├── custom_reader.py        # Custom CSV reader implementation
├── custom_writer.py        # Custom CSV writer implementation
├── benchmark.py            # Benchmark script for small & large CSV files
├── test.csv                # Generated test file (sample data)
└── big.csv                 # Generated large CSV file (1M rows)
```

## 🚀 Setup Instructions

### 1. Create project folder

Command used:

```cmd
mkdir custom-csv
cd custom-csv
```

What this does: `mkdir` makes a new folder named `custom-csv`. `cd` changes the current terminal directory into that folder so all subsequent commands run inside the project directory. After this you’ll create and edit files inside `custom-csv`.

---

### 2. Create virtual environment

Command used:

```cmd
python -m venv .venv
```

What this does: this creates an isolated Python environment in the `.venv` folder. It keeps project dependencies and Python settings separate from your system Python so running scripts is reproducible and safe.

Files created: the `.venv` folder (contains Python executable, site-packages, and scripts).

---

### 3. Activate environment

Command used (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

(or in CMD: `.venv\Scripts\activate.bat`)
What this does: it activates the virtual environment for the current terminal session. You’ll see `(.venv)` appear at the start of your prompt, which tells you Python commands now use the environment’s interpreter and packages.

Why activate: ensures `python` and any installed packages are the ones in `.venv`, not the system Python.

---

### ▶️ Running the Benchmark

Command used:

```cmd
python benchmark.py
```

What the script does (brief):

* Generates a small CSV (`test.csv`, 10k rows) with sample edge cases (commas, quotes, newlines).
* Runs the **custom reader** to parse `test.csv` and measures elapsed time.
* Runs Python’s built-in `csv.reader` on the same file and measures elapsed time.
* Writes output with the custom writer (`custom_output.csv`) and with the builtin writer (`standard_output.csv`) and measures times.
* Generates a large CSV (`big.csv`, 1,000,000 rows) and repeats reading benchmarks on that large file to compare scalability.

What to look for in output: the script prints timing lines such as:

```
Custom Reader Time:   0.0550 sec
Python csv.reader:    0.0055 sec
```

Interpretation: these numbers show elapsed wall-clock time. Lower is better; the builtin `csv` is faster (it’s implemented in optimized C), while the custom pure-Python parser is slower but demonstrates correct parsing and edge-case handling.

---

## Quick troubleshooting & tips

* If `python benchmark.py` says module not found, ensure you are in the `custom-csv` folder and the virtualenv is active.
* If you accidentally committed `.venv` to Git, add a `.gitignore` with `.venv/` and run `git rm -r --cached .venv` then commit & push.
* To re-run only the small test without regenerating big.csv, edit the script or remove the large-file section temporarily.

---
