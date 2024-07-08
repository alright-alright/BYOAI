import argparse
import os
import shutil

# Directory where modules are installed
MODULES_DIR = 'modules'

# Directory where repository modules are stored
REPOSITORY_DIR = 'repository'

def search_module(module_name):
    print(f"Searching for module: {module_name}")
    module_path = os.path.join(REPOSITORY_DIR, f"{module_name}.py")
    if os.path.exists(module_path):
        print(f"Module found: {module_name}")
    else:
        print(f"Module {module_name} not found in the repository.")

def install_module(module_name):
    print(f"Installing module: {module_name}")
    module_path = os.path.join(REPOSITORY_DIR, f"{module_name}.py")
    if os.path.exists(module_path):
        shutil.copy(module_path, os.path.join(MODULES_DIR, f"{module_name}.py"))
        print(f"Module {module_name} installed successfully.")
    else:
        print(f"Module {module_name} not found in the repository.")

def update_modules():
    print("Updating all modules")
    for module_name in os.listdir(MODULES_DIR):
        if module_name.endswith('.py'):
            module_name = module_name[:-3]
            module_path = os.path.join(REPOSITORY_DIR, f"{module_name}.py")
            if os.path.exists(module_path):
                shutil.copy(module_path, os.path.join(MODULES_DIR, f"{module_name}.py"))
                print(f"Updated {module_name}")
            else:
                print(f"Module {module_name} not found in the repository.")
    print("All modules updated successfully.")

def main():
    parser = argparse.ArgumentParser(description="BYOAI Package Manager")
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search", help="Search for a module")
    search_parser.add_argument("module_name", help="Name of the module to search for")

    install_parser = subparsers.add_parser("install", help="Install a module")
    install_parser.add_argument("module_name", help="Name of the module to install")

    update_parser = subparsers.add_parser("update", help="Update all modules")

    args = parser.parse_args()

    if args.command == "search":
        search_module(args.module_name)
    elif args.command == "install":
        install_module(args.module_name)
    elif args.command == "update":
        update_modules()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
