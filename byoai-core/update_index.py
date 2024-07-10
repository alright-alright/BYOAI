import requests
import json
import os

def fetch_model_metadata(model_name):
    response = requests.get(f"https://huggingface.co/api/models/{model_name}")
    if response.status_code == 200:
        metadata = response.json()
        return {
            "name": model_name,
            "description": metadata.get("pipeline_tag", "No description available"),
            "url": f"https://huggingface.co/{model_name}",
            "source": "huggingface"
        }
    return None

def update_index_file(index_file_path):
    try:
        with open(index_file_path, 'r') as f:
            models = json.load(f)
    except FileNotFoundError:
        print("Index file not found.")
        return

    updated_models = []
    for model in models:
        model_name = model.get("name")
        if model_name:
            metadata = fetch_model_metadata(model_name)
            if metadata:
                updated_models.append(metadata)
            else:
                updated_models.append(model)
        else:
            updated_models.append(model)

    with open(index_file_path, 'w') as f:
        json.dump(updated_models, f, indent=4)

if __name__ == "__main__":
    index_file_path = "./byoai-core/index.json"
    update_index_file(index_file_path)
    print("Index file updated successfully.")
