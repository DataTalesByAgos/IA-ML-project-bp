def prompt_choice(prompt, options):
    """Prompt the user for a valid choice."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice


def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def get_os_config_filename(target_os: str) -> str:
    return "config_windows.ini" if target_os == "Windows" else "config_linux.ini"


def get_os_config_content(target_os: str) -> str:
    path = "C:\\logs\\" if target_os == "Windows" else "/var/logs/"
    return f"[config]\nlog_path = {path}"


def create_advanced_structure(project_name: str, module_name: str, target_os: str, include_tests: bool):
    p = Path(project_name)

    # Base files
    create_file(p / "README.md", f"# {project_name}\n\nGenerated for {target_os}.")
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
    print("=== Advanced Project Environment Generator ===\n")

    detected_os = platform.system()
    if detected_os == "Windows":
        target_os = "Windows"
    else:
        choice = prompt_choice("Generate project structure for Linux or Windows? [linux/windows]: ", ["linux", "windows"])
        target_os = "Windows" if choice == "windows" else "Linux"

    project_name = input("Project name: ").strip()
    module_name = input("Name of your main Python module (e.g., myproject): ").strip()
    include_tests = prompt_choice("Include tests folder? [y/n]: ", ["y", "n"]) == "y"

    create_advanced_structure(project_name, module_name, target_os, include_tests)
    print(f"\n✅ Project '{project_name}' created with module '{module_name}' for {target_os}.")


if __name__ == "__main__":
    main()