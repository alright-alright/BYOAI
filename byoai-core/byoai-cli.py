import json
import requests
import sys

REPO_URL = "https://path/to/your/model/repository/index.json"

def fetch_model_index():
    response = requests.get(REPO_URL)
    if response.status_code == 200:
        return response.json()
    else:
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
    else:
        print(f"Unknown command: {command}")
        print("Available commands: search, list")
        sys.exit(1)

if __name__ == "__main__":
    main()
