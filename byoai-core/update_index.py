import requests
import json
import os

# Define Hugging Face API URL
HUGGINGFACE_API_URL = "https://huggingface.co/api/models"

def fetch_model_metadata(model_name):
    api_url = f"https://huggingface.co/api/models/{model_name}"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        metadata = response.json()

        # Attempt to locate a valid script file by checking common filenames
        possible_files = [
            f"{model_name.split('/')[-1]}.py",
            "model.py",
            "main.py",
            "script.py",
        ]
        
        for filename in possible_files:
            model_url = f"https://huggingface.co/{model_name}/resolve/main/{filename}"
            file_response = requests.head(model_url, timeout=10)
            if file_response.status_code == 200:
                return {
                    "name": model_name,
                    "description": metadata.get("pipeline_tag", "No description available"),
                    "url": model_url,
                    "repo_id": model_name,
                    "source": "huggingface"
                }
        
        # Check for any .py file in the model repository
        model_files_url = f"https://huggingface.co/api/models/{model_name}/tree/main"
        files_response = requests.get(model_files_url, timeout=10)
        if files_response.status_code == 200:
            files = files_response.json()
            for file in files:
                if file["path"].endswith(".py"):
                    model_url = f"https://huggingface.co/{model_name}/resolve/main/{file['path']}"
                    return {
                        "name": model_name,
                        "description": metadata.get("pipeline_tag", "No description available"),
                        "url": model_url,
                        "repo_id": model_name,
                        "source": "huggingface"
                    }

        print(f"Model URL not found for {model_name}")
    except requests.RequestException as e:
        print(f"Error fetching metadata for {model_name}: {e}")
    return None

def fetch_models(limit=10):
    try:
        response = requests.get(HUGGINGFACE_API_URL, timeout=10)
        response.raise_for_status()
        models = response.json()[:limit]  # Limit the number of models for testing
        return models
    except requests.RequestException as e:
        print(f"Failed to fetch models from Hugging Face API: {e}")
        return []

def update_index_file(index_file_path):
    models = fetch_models()
    print(f"Fetched {len(models)} models from Hugging Face API")
    updated_models = []
    for i, model in enumerate(models):
        model_name = model.get("modelId")
        if model_name:
            metadata = fetch_model_metadata(model_name)
            if metadata:
                updated_models.append(metadata)
                print(f"Added {model_name} to index.")
            else:
                print(f"Skipped {model_name} due to missing valid script.")
        if i % 10 == 0:
            print(f"Processed {i} models...")

    with open(index_file_path, 'w') as f:
        json.dump(updated_models, f, indent=4)
    print(f"Total models added to index: {len(updated_models)}")

if __name__ == "__main__":
    index_file_path = "./index.json"
    if os.path.exists(index_file_path):
        backup_path = "./index_backup.json"
        os.rename(index_file_path, backup_path)
        print(f"Backed up {index_file_path} to {backup_path}")
    else:
        print(f"Index file not found. Creating a new one at {index_file_path}")
        
    update_index_file(index_file_path)
    print("Index file updated successfully.")
