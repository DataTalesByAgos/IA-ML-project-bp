# ML Project Scaffold CLI

**CLI tool to scaffold machine learning project directories with config files, test structure, and OS-specific setup (Windows/Linux).**

This tool helps you quickly start machine learning or data science projects with a consistent folder structure and useful boilerplate files.

---

## 🚀 Features

- OS-specific config file (`config_windows.ini` or `config_linux.ini`)
- Organized data directories (`raw`, `processed`, `external`, etc.)
- Structured `src/` folder with modular Python files
- Optional test folder with a sample test
- Ready-to-use `Makefile`, `pyproject.toml`, and `setup.cfg`
- Docker-compatible for zero-setup usage

---

## 🐳 Using with Docker

### 1. Build the Docker image

```bash
docker build -t ml-scaffold .
```

### 2. Run the generator

```bash
docker run --rm -v $(pwd):/output ml-scaffold \
  --project my-ml-project \
  --module core_module \
  --os linux \
  --tests y
```

This will create a folder named `my-ml-project` inside your current directory with the full structure.

---

## 🧾 CLI Usage (without Docker)

If you prefer to run the script directly (you need Python 3.8+):

```bash
python project_generator.py \
  --project my-ml-project \
  --module core_module \
  --os linux \
  --tests y
```

### Arguments

- `--project`: Name of the project (required)
- `--module`: Name of the main module under `src/` (required)
- `--os`: Target OS (`linux` or `windows`) — defaults to auto-detect
- `--tests`: Include tests folder? (`y` or `n`)

---

## 📂 Example Output

```
my-ml-project/
├── config_linux.ini
├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── docs/
├── models/
├── notebooks/
├── pyproject.toml
├── README.md
├── references/
├── reports/
│   └── figures/
├── requirements.txt
├── setup.cfg
├── Makefile
├── LICENSE
├── src/
│   └── core_module/
│       ├── __init__.py
│       ├── config.py
│       ├── dataset.py
│       ├── features.py
│       ├── plots.py
│       └── modeling/
│           ├── __init__.py
│           ├── train.py
│           └── predict.py
└── tests/
    └── test_main.py  # If --tests y
```

---

## 🧪 License

MIT License
