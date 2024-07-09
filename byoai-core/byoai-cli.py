import json
import os
import sys
import requests
from urllib.parse import urlparse

REPO_URL = "./byoai-core/index.json"
INSTALL_DIR = "./modules/"

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
            print(f"Model: {model['name']}")
            print(f"Description: {model['description']}")
            print(f"URL: {model['url']}")
            print()

def list_models():
    models = fetch_model_index()
    for model in models:
        print(f"Model: {model['name']}")
        print(f"Description: {model['description']}")
        print()

def install_model(model_name):
    models = fetch_model_index()
    for model in models:
        if model_name.lower() == model["name"].lower():
            url = model["url"]
            parsed_url = urlparse(url)
            file_extension = os.path.splitext(parsed_url.path)[1] or ".py"
            model_dir = os.path.join(INSTALL_DIR, os.path.dirname(model_name.replace("/", "_")))
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            model_path = os.path.join(model_dir, f"{os.path.basename(model_name)}{file_extension}")
            if parsed_url.scheme.startswith("http"):
                response = requests.get(url)
                if response.status_code == 200:
                    with open(model_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Model {model_name} installed successfully from URL.")
                else:
                    print(f"Failed to download the model: {model_name}")
            else:
                print(f"Unsupported URL scheme for model: {model_name}")
            return
    print(f"Model {model_name} not found.")

def update_models():
    models = fetch_model_index()
    for model in models:
        install_model(model["name"])

def bundle_models(models):
    # Placeholder for bundling logic
    print(f"Bundling models: {', '.join(models)}")
    # Additional logic for bundling can be added here

def main():
    if len(sys.argv) < 2:
        print("Usage: byoai <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "search":
        if len(sys.argv) < 3:
            print("Usage: byoai search <query>")
            sys.exit(1)
        query = sys.argv[2]
        search_models(query)
    elif command == "list":
        list_models()
    elif command == "install":
        if len(sys.argv) < 3:
            print("Usage: byoai install <model_name>")
            sys.exit(1)
        model_name = sys.argv[2]
        install_model(model_name)
    elif command == "update":
        update_models()
    elif command == "bundle":
        if len(sys.argv) < 3:
            print("Usage: byoai bundle <model1> <model2> ...")
            sys.exit(1)
        models = sys.argv[2:]
        bundle_models(models)
    else:
        print(f"Unknown command: {command}")
        print("Usage: byoai <command> [<args>]")
        sys.exit(1)

if __name__ == "__main__":
    main()
