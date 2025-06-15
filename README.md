# Advanced Project Environment Generator

This is a Python script to quickly generate a structured and OS-specific Python project environment. It creates all necessary directories, configuration files, and optionally, a basic test suite.

## Features

- Creates a complete Python project structure with folders for:
  - Source code (`src/`)
  - Data (`data/raw`, `data/interim`, etc.)
  - Models, notebooks, references, reports
- Adds essential files:
  - `README.md`, `requirements.txt`, `setup.cfg`, `pyproject.toml`, `Makefile`
- OS-specific configuration (`config_windows.ini` or `config_linux.ini`)
- Optional test setup (`tests/test_main.py`)

## Usage

Run the script with Python 3:

```bash
python project_generator.py
```

You will be prompted to:

- Choose the target OS (Linux or Windows)
- Enter the project name
- Enter the main module name
- Choose whether to include a `tests` folder

The generator will detect your OS automatically, but allows manual override for Linux/Windows-specific settings.

## Example

```
=== Advanced Project Environment Generator ===

Generate project structure for Linux or Windows? [linux/windows]: linux
Project name: my-awesome-project
Name of your main Python module (e.g., myproject): awesome_module
Include tests folder? [y/n]: y

✅ Project 'my-awesome-project' created with module 'awesome_module' for Linux.
```

## Output Structure

```
my-awesome-project/
├── Makefile
├── README.md
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
├── references/
├── reports/
│   └── figures/
├── requirements.txt
├── setup.cfg
├── src/
│   └── awesome_module/
│       ├── __init__.py
│       ├── config.py
│       ├── dataset.py
│       ├── features.py
│       ├── modeling/
│       │   ├── __init__.py
│       │   ├── predict.py
│       │   └── train.py
│       └── plots.py
└── tests/
    └── test_main.py  # Optional
```