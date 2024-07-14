import os
import json
import sys
from colorama import init, Fore, Style

# Initialize colorama
init()

# File paths
REPO_URL = "./index.json"
INSTALL_DIR = "./user_space/"
LOG_FILE = "byoai_log.txt"

current_project = None
current_model = None

def color_text(text, color_code):
    return f"{color_code}{text}{Style.RESET_ALL}"

# Check for required libraries
required_libraries = {
    "torch": "PyTorch",
    "transformers": "Transformers",
    "huggingface_hub": "Hugging Face Hub"
}

missing_libraries = []

for lib, name in required_libraries.items():
    try:
        __import__(lib)
    except ImportError:
        missing_libraries.append(name)

if missing_libraries:
    print(color_text("The following required libraries are missing:", Fore.YELLOW))
    for lib in missing_libraries:
        print(f"- {lib}")
    print("\nPlease install them using pip:")
    print(color_text("pip install torch transformers huggingface_hub", Fore.CYAN))
    print("\nAfter installation, please restart the script.")
    sys.exit(1)

# Now that we've checked, we can safely import these
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForCausalLM

def log_message(message):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(message + "\n")

def fetch_model_index():
    try:
        with open(REPO_URL, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(color_text(f"Failed to fetch model index. File not found at: {REPO_URL}", Fore.RED))
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(color_text(f"Failed to parse JSON. Ensure the index.json is valid. Error: {e}", Fore.RED))
        sys.exit(1)

def list_models():
    models = fetch_model_index()
    print(color_text("Available models:", Fore.CYAN))
    for model in models:
        print(f"{color_text(model['name'], Fore.GREEN)} - {model['description']}")

def install_model(model_name):
    global current_project, current_model
    if not current_project:
        print(color_text("No project selected. Please select or create a project first.", Fore.YELLOW))
        return

    models = fetch_model_index()
    model = next((m for m in models if model_name.lower() in m["name"].lower()), None)
    
    if not model:
        print(color_text(f"Model '{model_name}' not found.", Fore.RED))
        return

    repo_id = model["repo_id"]
    
    try:
        print(f"Downloading {model['name']}...")
        project_dir = os.path.join(INSTALL_DIR, current_project)
        model_dir = os.path.join(project_dir, model['name'])
        os.makedirs(model_dir, exist_ok=True)
        
        # Download the model
        AutoModelForCausalLM.from_pretrained(repo_id, cache_dir=model_dir)
        AutoTokenizer.from_pretrained(repo_id, cache_dir=model_dir)
        
        print(color_text(f"Model '{model['name']}' downloaded to: {model_dir}", Fore.GREEN))
        log_message(f"Model '{model['name']}' downloaded to: {model_dir}")
        current_model = model['name']
    except Exception as e:
        print(color_text(f"Failed to download the model '{model['name']}': {str(e)}", Fore.RED))
        log_message(f"Failed to download the model '{model['name']}': {str(e)}")

def create_project():
    global current_project
    project_name = input("Enter the name of the new project: ").strip()
    if not project_name:
        print(color_text("Project name cannot be empty.", Fore.RED))
        return None
    
    project_path = os.path.join(INSTALL_DIR, project_name)
    try:
        os.makedirs(project_path, exist_ok=True)
        print(color_text(f"Project '{project_name}' created successfully.", Fore.GREEN))
        current_project = project_name
        return project_name
    except Exception as e:
        print(color_text(f"Failed to create project: {str(e)}", Fore.RED))
        return None

def list_projects():
    global current_project
    projects = [d for d in os.listdir(INSTALL_DIR) if os.path.isdir(os.path.join(INSTALL_DIR, d))]
    if not projects:
        print(color_text("No projects found.", Fore.YELLOW))
        return None
    
    print(color_text("Existing projects:", Fore.CYAN))
    for i, project in enumerate(projects, 1):
        print(f"{i}. {project}")
    
    while True:
        choice = input("Enter the number of the project to select (or 0 to cancel): ").strip()
        if choice == '0':
            return None
        try:
            project_index = int(choice) - 1
            if 0 <= project_index < len(projects):
                current_project = projects[project_index]
                return current_project
            else:
                print(color_text("Invalid project number. Please try again.", Fore.RED))
        except ValueError:
            print(color_text("Invalid input. Please enter a number.", Fore.RED))

def check_model_files(model_dir):
    print(f"Checking contents of {model_dir}:")
    for root, dirs, files in os.walk(model_dir):
        level = root.replace(model_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")
    
    required_files = ['config.json', 'tokenizer.json', 'tokenizer_config.json']
    model_files = ['pytorch_model.bin', 'model.safetensors']
    
    missing_files = []
    for file in required_files + model_files:
        if not any(file in files for root, dirs, files in os.walk(model_dir)):
            missing_files.append(file)
    
    return missing_files

def find_model_files(model_dir):
    print(f"Searching for model files in: {model_dir}")
    
    # Check the specific nested structure
    nested_dir = os.path.join(model_dir, 'models--gpt2', 'snapshots')
    if os.path.exists(nested_dir):
        snapshot_dirs = [d for d in os.listdir(nested_dir) if os.path.isdir(os.path.join(nested_dir, d))]
        if snapshot_dirs:
            snapshot_dir = os.path.join(nested_dir, snapshot_dirs[0])
            if os.path.isfile(os.path.join(snapshot_dir, 'config.json')) and \
               (os.path.isfile(os.path.join(snapshot_dir, 'model.safetensors')) or \
                os.path.isfile(os.path.join(snapshot_dir, 'pytorch_model.bin'))):
                print(f"Found model files in: {snapshot_dir}")
                return snapshot_dir
    
    # If not found in the specific structure, fall back to the previous search method
    for root, dirs, files in os.walk(model_dir):
        if 'config.json' in files and ('model.safetensors' in files or 'pytorch_model.bin' in files):
            print(f"Found model files in: {root}")
            return root
    
    print(f"Could not find model files in {model_dir} or its subdirectories")
    return None

def interact_with_model():
    global current_project, current_model
    if not current_project or not current_model:
        print(color_text("No project or model selected. Please select a project and install a model first.", Fore.YELLOW))
        return

    base_model_dir = os.path.join(INSTALL_DIR, current_project, current_model)
    print(f"Base model directory: {base_model_dir}")
    
    model_dir = find_model_files(base_model_dir)
    if not model_dir:
        print(color_text(f"Could not find the necessary model files in {base_model_dir}", Fore.RED))
        print("Please try reinstalling the model.")
        check_model_files(base_model_dir)
        return

    try:
        print(color_text(f"Loading model: {current_model}", Fore.CYAN))
        print(color_text(f"Model directory: {model_dir}", Fore.CYAN))
        
        tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained(model_dir, local_files_only=True)

        print(color_text(f"Interacting with model: {current_model}", Fore.CYAN))
        while True:
            user_input = input("Enter your prompt (or 'quit' to exit): ").strip()
            if user_input.lower() == 'quit':
                break

            inputs = tokenizer(user_input, return_tensors="pt")
            outputs = model.generate(**inputs, max_length=100)
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print(color_text("Model response:", Fore.GREEN), response)

    except Exception as e:
        print(color_text(f"Error interacting with the model: {str(e)}", Fore.RED))
        print("Make sure you have PyTorch installed and the model is fully downloaded.")
        print(f"Model directory: {model_dir}")
        check_model_files(model_dir)

def main_menu():
    global current_project, current_model
    while True:
        print("\n" + color_text("BYOAI CLI", Fore.CYAN))
        print(f"Current Project: {color_text(current_project or 'None', Fore.YELLOW)}")
        print(f"Current Model: {color_text(current_model or 'None', Fore.YELLOW)}")
        print("1. Create a new project")
        print("2. Select an existing project")
        print("3. List available models")
        print("4. Install a model")
        print("5. Interact with the model")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            create_project()
        elif choice == '2':
            list_projects()
        elif choice == '3':
            list_models()
        elif choice == '4':
            if not current_project:
                print(color_text("Please select a project first.", Fore.YELLOW))
                continue
            print("Available models:")
            list_models()
            model_name = input("Enter the name or part of the name of the model to install: ").strip()
            if model_name:
                install_model(model_name)
            else:
                print(color_text("Model name cannot be empty.", Fore.RED))
        elif choice == '5':
            interact_with_model()
        elif choice == '6':
            print("Exiting BYOAI. Goodbye!")
            sys.exit()
        else:
            print(color_text("Invalid choice. Please try again.", Fore.RED))

if __name__ == "__main__":
    # Clear the screen once when the app starts
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
