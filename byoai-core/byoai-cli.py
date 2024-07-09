import json
import os
import sys
import requests
import subprocess
from urllib.parse import urlparse

REPO_URL = "./byoai-core/index.json"
INSTALL_DIR = "./modules/"

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls', shell=True)

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def fetch_model_index():
    try:
        with open(REPO_URL, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Failed to fetch model index.")
        sys.exit(1)

def search_models(query):
    models = fetch_model_index()
    for model in models:
        if query.lower() in model["name"].lower():
            print(f"{color_text('Model -->', '37')} {color_text(model['name'], '32')} {color_text('| Description -->', '33')} {color_text(model['description'] or 'No description available', '36' if model['description'] == 'No description available' else '32')}")
            print(f"{color_text('URL:', '37')} {color_text(model['url'], '32')}")
            print()

def list_models():
    models = fetch_model_index()
    for model in models:
        description_color = '36' if model['description'] == 'No description available' else '32'
        print(f"{color_text('Model -->', '37')} {color_text(model['name'], '32')} {color_text('| Description -->', '33')} {color_text(model['description'] or 'No description available', description_color)}")

def install_model(model_name):
    models = fetch_model_index()
    for model in models:
        if model_name.lower() == model["name"].lower():
            url = model["url"]
            parsed_url = urlparse(url)
            if parsed_url.scheme == "file":
                path = os.path.abspath(os.path.join(os.getcwd(), parsed_url.path.lstrip('/')))
                with open(path, 'r') as f:
                    script_content = f.read()
                with open(os.path.join(INSTALL_DIR, f"{model_name}.py"), 'w') as f:
                    f.write(script_content)
                print(f"{color_text('Model:', '37')} {color_text(model_name, '32')} {color_text('installed successfully from local path.', '36')}")
            else:
                response = requests.get(url)
                if response.status_code == 200:
                    model_dir = os.path.join(INSTALL_DIR, model_name)
                    os.makedirs(model_dir, exist_ok=True)
                    file_extension = os.path.splitext(parsed_url.path)[1]
                    model_path = os.path.join(model_dir, f"{os.path.basename(model_name)}{file_extension}")
                    with open(model_path, 'wb') as f:
                        f.write(response.content)
                    print(f"{color_text('Model:', '37')} {color_text(model_name, '32')} {color_text('installed successfully from URL.', '36')}")
                else:
                    print(f"{color_text('Failed to download the model:', '31')} {color_text(model_name, '32')}")
            return
    print(f"{color_text('Model:', '31')} {color_text(model_name, '32')} {color_text('not found.', '31')}")

def update_models():
    models = fetch_model_index()
    for model in models:
        install_model(model["name"])

def bundle_models(models):
    print(f"Bundling models: {', '.join(models)}")

def main_menu():
    clear_screen()
    print()
    print(f"{color_text('Welcome to the BYOAI build your own AI project', '32')}")
    print()
    print(f"{color_text('Select an option:', '37')}")
    print()
    print(f"{color_text('1.', '37')} {color_text('List Models', '33')}")
    print(f"{color_text('2.', '37')} {color_text('Search Models', '33')}")
    print(f"{color_text('3.', '37')} {color_text('Install Model', '33')}")
    print(f"{color_text('4.', '37')} {color_text('Update Models', '33')}")
    print(f"{color_text('5.', '37')} {color_text('Bundle Models', '33')}")
    print(f"{color_text('6.', '37')} {color_text('BYOAI CLI', '33')}")
    print(f"{color_text('7.', '37')} {color_text('Exit BYOAI', '33')}")
    print()

    choice = input(f"{color_text('Enter your choice:', '37')} ")
    return choice

def byoai_prompt():
    while True:
        command = input(f"{color_text('BYOAI >', '36')} ")
        if command.strip().lower() == 'exit':
            break
        try:
            os.system(command)
        except Exception as e:
            print(f"{color_text('Error:', '31')} {str(e)}")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            clear_screen()
            list_models()
        elif choice == '2':
            clear_screen()
            query = input("Enter the model name to search: ")
            search_models(query)
        elif choice == '3':
            clear_screen()
            model_name = input("Enter the model name to install: ")
            install_model(model_name)
        elif choice == '4':
            clear_screen()
            update_models()
        elif choice == '5':
            clear_screen()
            models = input("Enter the model names to bundle (comma-separated): ").split(',')
            bundle_models(models)
        elif choice == '6':
            clear_screen()
            byoai_prompt()
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
