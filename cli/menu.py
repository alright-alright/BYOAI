import os
import subprocess
import json
import requests
from colorama import init, Fore, Style
from urllib.parse import urlparse
import sys
import inquirer

# Initialize colorama
init()

# File paths
REPO_URL = "../byoai-core/index.json"
INSTALL_DIR = "../modules/"
LOG_FILE = "byoai_log.txt"

# Function to log messages to a file
def log_message(message):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(message + "\n")

# Helper functions
def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls', shell=True)

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def fetch_model_index():
    log_message("Fetching model index...")
    try:
        with open(REPO_URL, 'r') as f:
            data = json.load(f)
            log_message(f"Model index fetched: {data}")
            return data
    except FileNotFoundError:
        log_message("Failed to fetch model index. Please ensure the index.json file is located at '../byoai-core/index.json'.")
        sys.exit(1)

def fetch_tf_models():
    log_message("Fetching TensorFlow models...")
    try:
        with open("../tf_models.json", 'r') as f:
            data = json.load(f)
            log_message(f"TensorFlow models fetched: {data}")
            return data
    except FileNotFoundError:
        log_message("Failed to fetch TensorFlow models index. Please ensure the tf_models.json file exists.")
        sys.exit(1)

def search_models(query, source):
    log_message(f"Searching models: {query} in {source}")
    models = fetch_model_index() if source == 'huggingface' else fetch_tf_models()
    for model in models:
        if query.lower() in model["name"].lower():
            print(f"{color_text('Model -->', '37')} {color_text(model['name'], '32')} {color_text('| Description -->', '33')} {color_text(model['description'] or 'No description available', '36' if model['description'] == 'No description available' else '32')}")
            print(f"{color_text('URL:', '37')} {color_text(model['url'], '32')}")
            print()

def list_models(source, for_bundling=False):
    log_message(f"Listing models from source: {source}")
    models = fetch_model_index() if source == 'huggingface' else fetch_tf_models()
    selected_models = []

    log_message(f"Models: {models}")
    model_choices = [
        inquirer.Checkbox(
            'models',
            message=color_text("Select models to bundle:", '33'),
            choices=[(model['name'], model['name']) for model in models]
        )
    ]

    answers = inquirer.prompt(model_choices)
    selected_models = answers['models']

    log_message(f"Selected models: {selected_models}")
    return selected_models

def install_model(model_name, source):
    log_message(f"Installing model: {model_name} from {source}")
    models = fetch_model_index() if source == 'huggingface' else fetch_tf_models()
    for model in models:
        if model_name.lower() == model["name"].lower():
            url = model["url"]
            response = requests.get(url)
            if response.status_code == 200:
                model_dir = os.path.join(INSTALL_DIR, model_name)
                os.makedirs(model_dir, exist_ok=True)
                file_extension = os.path.splitext(urlparse(url).path)[1]
                model_path = os.path.join(model_dir, f"{os.path.basename(model_name)}{file_extension}")
                with open(model_path, 'wb') as f:
                    f.write(response.content)
                log_message(f"Model '{model_name}' installed successfully from URL.")
                print(f"{color_text('Model:', '37')} {color_text(model_name, '32')} {color_text('installed successfully from URL.', '36')}")
                print_model_usage(model_name)
            else:
                log_message(f"Failed to download the model: {model_name}")
                print(f"{color_text('Failed to download the model:', '31')} {color_text(model_name, '32')}")
            return
    log_message(f"Model '{model_name}' not found.")
    print(f"{color_text('Model:', '31')} {color_text(model_name, '32')} {color_text('not found.', '31')}")

def print_model_usage(model_name):
    print(f"\n{color_text('To use the model, you can run:', '37')}")
    print(f"{color_text(f'python modules/{model_name}/{os.path.basename(model_name)}.py [your_input_here]', '32')}")

def update_models():
    log_message("Updating models...")
    models = fetch_model_index()
    for model in models:
        install_model(model["name"], 'huggingface')

def bundle_models(models):
    log_message(f"Bundling models: {', '.join(models)}")
    print(f"Bundling models: {', '.join(models)}")

def use_installed_model():
    models = os.listdir(INSTALL_DIR)
    if not models:
        log_message("No models installed.")
        print("No models installed. Install a model first.")
        return

    print("Installed models:")
    for index, model in enumerate(models, start=1):
        print(f"{color_text(str(index), '37')}. {color_text(model, '33')}")

    choice = input(color_text('Enter the number of the model you want to use: ', '37'))
    try:
        model_index = int(choice) - 1
        if 0 <= model_index < len(models):
            model_name = models[model_index]
            model_path = os.path.join(INSTALL_DIR, model_name, f"{os.path.basename(model_name)}.py")
            if os.path.exists(model_path):
                user_input = input("Enter input for the model: ")
                os.system(f"python {model_path} {user_input}")
            else:
                log_message(f"Model script {model_path} not found.")
                print(f"Model script {model_path} not found.")
        else:
            log_message("Invalid choice. Please try again.")
            print("Invalid choice. Please try again.")
    except ValueError:
        log_message("Invalid input. Please enter a number.")
        print("Invalid input. Please enter a number.")

def byoai_prompt():
    while True:
        command = input(f"{color_text('BYOAI >', '36')} ")
        if command.strip().lower() == 'exit':
            break
        try:
            os.system(command)
        except Exception as e:
            log_message(f"Error: {str(e)}")
            print(f"{color_text('Error:', '31')} {str(e)}")

def print_header(text):
    print(Fore.CYAN + "=" * 23)
    print(Fore.CYAN + text.center(23))
    print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)

def main_menu():
    clear_screen()
    print_header("Welcome to BYOAI")
    print(Fore.YELLOW + "1. Project Management" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Model Management" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Training & Deployment" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. BYOAI Terminal" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Settings" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. Help" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. Exit" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
    choice = input(color_text("Select an option (1-7): ", '37'))
    return choice

def project_management_menu():
    clear_screen()
    print_header("Project Management")
    print(Fore.YELLOW + "1. Create New Project" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. View Projects" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Delete Project" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. Back to Main Menu" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
    choice = input(color_text("Select an option (1-4): ", '37'))
    return choice
def model_management_menu():
    while True:
        clear_screen()
        print_header("Model Management")
        print(Fore.YELLOW + "1. Search Models" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. List and Bundle Models" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Install Model" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Update Models" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Use Installed Model" + Style.RESET_ALL)
        print(Fore.YELLOW + "6. Back to Main Menu" + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
        choice = input(color_text("Select an option (1-6): ", '37'))
        
        if choice == '1':
            query = input(color_text("Enter a search query: ", '37'))
            search_models(query, 'huggingface')
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '2':
            models_to_bundle = list_models('huggingface', for_bundling=True)
            bundle_models(models_to_bundle)
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '3':
            model_name = input(color_text("Enter the name of the model to install: ", '37'))
            install_model(model_name, 'huggingface')
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '4':
            update_models()
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '5':
            use_installed_model()
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '6':
            break
        else:
            print(f"{color_text('Invalid choice:', '31')} {choice}")
            input(color_text("Press Enter to continue...", '37'))

def training_deployment_menu():
    clear_screen()
    print_header("Training & Deployment")
    print(Fore.YELLOW + "1. Train New Model" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Deploy Model" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Back to Main Menu" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
    choice = input(color_text("Select an option (1-3): ", '37'))
    return choice

def settings_menu():
    while True:
        clear_screen()
        print_header("Settings")
        print(Fore.YELLOW + "1. Change Installation Directory" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. View Log" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Back to Main Menu" + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
        choice = input(color_text("Select an option (1-3): ", '37'))
        
        if choice == '1':
            log_message("Changing installation directory.")
            print("Functionality not implemented yet.")
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '2':
            log_message("Viewing log.")
            with open(LOG_FILE, 'r') as log_file:
                print(log_file.read())
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '3':
            log_message("Returning to the main menu.")
            break
        else:
            log_message(f"Invalid choice: {choice}")
            print(f"{color_text('Invalid choice:', '31')} {choice}")
            input(color_text("Press Enter to continue...", '37'))

def help_menu():
    while True:
        clear_screen()
        print_header("Help")
        print(Fore.YELLOW + "1. BYOAI Documentation" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. About BYOAI" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Back to Main Menu" + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 23 + Style.RESET_ALL)
        choice = input(color_text("Select an option (1-3): ", '37'))
        
        if choice == '1':
            log_message("Opening BYOAI documentation.")
            print("Functionality not implemented yet.")
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '2':
            log_message("Displaying information about BYOAI.")
            print("Functionality not implemented yet.")
            input(color_text("Press Enter to continue...", '37'))
        elif choice == '3':
            log_message("Returning to the main menu.")
            break
        else:
            log_message(f"Invalid choice: {choice}")
            print(f"{color_text('Invalid choice:', '31')} {choice}")
            input(color_text("Press Enter to continue...", '37'))

if __name__ == "__main__":
    while True:
        choice = main_menu()

        if choice == '1':
            while True:
                choice = project_management_menu()
                if choice == '1':
                    log_message("Creating a new project.")
                    print("Functionality not implemented yet.")
                    input(color_text("Press Enter to continue...", '37'))
                elif choice == '2':
                    log_message("Viewing projects.")
                    print("Functionality not implemented yet.")
                    input(color_text("Press Enter to continue...", '37'))
                elif choice == '3':
                    log_message("Deleting a project.")
                    print("Functionality not implemented yet.")
                    input(color_text("Press Enter to continue...", '37'))
                elif choice == '4':
                    log_message("Returning to the main menu.")
                    break
                else:
                    log_message(f"Invalid choice: {choice}")
                    print(f"{color_text('Invalid choice:', '31')} {choice}")
                    input(color_text("Press Enter to continue...", '37'))
                    
        elif choice == '2':
            model_management_menu()

        elif choice == '3':
            while True:
                choice = training_deployment_menu()
                if choice == '1':
                    log_message("Training a new model.")
                    print("Functionality not implemented yet.")
                    input(color_text("Press Enter to continue...", '37'))
                elif choice == '2':
                    log_message("Deploying a model.")
                    print("Functionality not implemented yet.")
                    input(color_text("Press Enter to continue...", '37'))
                elif choice == '3':
                    log_message("Returning to the main menu.")
                    break
                else:
                    log_message(f"Invalid choice: {choice}")
                    print(f"{color_text('Invalid choice:', '31')} {choice}")
                    input(color_text("Press Enter to continue...", '37'))

        elif choice == '4':
            byoai_prompt()

        elif choice == '5':
            settings_menu()

        elif choice == '6':
            help_menu()

        elif choice == '7':
            print("Exiting BYOAI. Goodbye!")
            break

        else:
            print(f"{color_text('Invalid choice:', '31')} {choice}")
            input(color_text("Press Enter to continue...", '37'))
