import argparse
import platform
from pathlib import Path


def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def get_os_config_filename(target_os: str) -> str:
    return "config_windows.ini" if target_os == "windows" else "config_linux.ini"


def get_os_config_content(target_os: str) -> str:
    path = "C:\\logs\\" if target_os == "windows" else "/var/logs/"
    return f"[config]\nlog_path = {path}"


def create_advanced_structure(project_name: str, module_name: str, target_os: str, include_tests: bool):
    p = Path("/output") / project_name

    # Base files
    create_file(p / "README.md", f"# {project_name}\n\nGenerated for {target_os.capitalize()}.")
    create_file(p / "requirements.txt")
    create_file(p / "LICENSE", "MIT License\n\nCopyright (c)")
    create_file(p / "Makefile", "# Add make targets like `make data` or `make train` here.")
    create_file(p / "setup.cfg", "[flake8]\nmax-line-length = 88")
    create_file(p / "pyproject.toml", f"[project]\nname = \"{project_name}\"\nversion = \"0.1.0\"")

    # Data folders
    for sub in ["raw", "interim", "processed", "external"]:
        (p / "data" / sub).mkdir(parents=True, exist_ok=True)

    # Other folders
    for folder in ["docs", "models", "notebooks", "references", "reports/figures"]:
        (p / folder).mkdir(parents=True, exist_ok=True)

    # Source code structure
    src_base = p / "src" / module_name
    create_file(src_base / "__init__.py", f"# {module_name} module")
    create_file(src_base / "config.py", "# Configuration variables")
    create_file(src_base / "dataset.py", "# Data loading and saving")
    create_file(src_base / "features.py", "# Feature engineering")
    create_file(src_base / "plots.py", "# Plotting utilities")
    modeling_path = src_base / "modeling"
    create_file(modeling_path / "__init__.py")
    create_file(modeling_path / "train.py", "# Training code")
    create_file(modeling_path / "predict.py", "# Prediction code")

    # OS-specific config
    config_name = get_os_config_filename(target_os)
    config_content = get_os_config_content(target_os)
    create_file(p / config_name, config_content)

    # Optional tests
    if include_tests:
        create_file(p / "tests" / "test_main.py", "# Sample test\n\ndef test_dummy():\n    assert True")


def main():
    parser = argparse.ArgumentParser(description="Generate an ML project structure.")
    parser.add_argument("--project", required=True, help="Project name")
    parser.add_argument("--module", required=True, help="Main module name")
    parser.add_argument("--os", choices=["linux", "windows"], help="Target OS (default: auto-detect)")
    parser.add_argument("--tests", choices=["y", "n"], default="n", help="Include tests folder? (y/n)")

    args = parser.parse_args()

    target_os = args.os or ("windows" if platform.system().lower() == "windows" else "linux")
    include_tests = args.tests == "y"

    create_advanced_structure(args.project, args.module, target_os, include_tests)
    print(f"✅ Project '{args.project}' created with module '{args.module}' for {target_os.capitalize()}.")


if __name__ == "__main__":
    main()
