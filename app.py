from pathlib import Path
import platform

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

def create_structure(project_name: str, target_os: str, include_tests: bool):
    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)

    # Base files
    create_file(project_path / "main.py", '# Entry point\nprint("Hello world")')
    create_file(project_path / "requirements.txt")
    create_file(project_path / "README.md", f"# {project_name}\n\nGenerated for {target_os}.")

    # OS-specific config
    config_name = get_os_config_filename(target_os)
    config_content = get_os_config_content(target_os)
    create_file(project_path / config_name, config_content)

    # Optional tests
    if include_tests:
        test_file = project_path / "tests" / "test_main.py"
        test_code = "# Test file\n\ndef test_dummy():\n    assert True"
        create_file(test_file, test_code)

def main():
    print("=== Project Environment Generator ===\n")

    detected_os = platform.system()
    if detected_os == "Windows":
        target_os = "Windows"
    else:
        choice = prompt_choice("Generate project structure for Linux or Windows? [linux/windows]: ", ["linux", "windows"])
        target_os = "Windows" if choice == "windows" else "Linux"

    project_name = input("Project name: ").strip()
    include_tests = prompt_choice("Include tests folder? [y/n]: ", ["y", "n"]) == "y"

    create_structure(project_name, target_os, include_tests)
    print(f"\n✅ Project '{project_name}' created for {target_os}.")

if __name__ == "__main__":
    main()
