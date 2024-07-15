import requests
import json

# URL of Hugging Face API for models
HUGGINGFACE_API_URL = "https://huggingface.co/api/models"

def fetch_huggingface_models():
    response = requests.get(HUGGINGFACE_API_URL)
    response.raise_for_status()  # Check for request errors
    models = response.json()

    model_data = []
    for model in models:
        model_info = {
            "name": model['modelId'],
            "description": model.get('description', 'No description available'),
            "url": f"https://huggingface.co/{model['modelId']}/resolve/main/{model['modelId']}.py",  # Construct the URL
            "repo_id": model['modelId'],  # Add the repo_id field
            "source": "huggingface"
        }
        model_data.append(model_info)

    return model_data

def update_index(models, index_path="./byoai-core/index.json"):
    try:
        with open(index_path, 'r') as f:
            current_index = json.load(f)
    except FileNotFoundError:
        current_index = []

    current_index.extend(models)

    with open(index_path, 'w') as f:
        json.dump(current_index, f, indent=4)

if __name__ == "__main__":
    hf_models = fetch_huggingface_models()
    update_index(hf_models)
