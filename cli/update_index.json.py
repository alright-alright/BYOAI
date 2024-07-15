from huggingface_hub import HfApi, list_repo_files
import json
import os

def fetch_model_metadata(model_name):
    """
    Fetch metadata for a given model from Hugging Face API.
    """
    api = HfApi()
    try:
        print(f"Fetching metadata for model: {model_name}")
        metadata = api.model_info(repo_id=model_name, timeout=10)
        print(f"Fetched metadata for {model_name}")

        # List all files in the repository
        print(f"Listing files in repository: {model_name}")
        files = list(list_repo_files(repo_id=model_name))
        print(f"Files in {model_name}: {files}")

        # Check for any .py file in the model repository
        for file in files:
            if file.endswith(".py"):
                model_url = f"https://huggingface.co/{model_name}/resolve/main/{file}"
                print(f"Found script file: {file}")
                return {
                    "name": model_name,
                    "description": metadata.pipeline_tag or "No description available",
                    "url": model_url,
                    "repo_id": model_name,
                    "source": "huggingface"
                }

        # If no .py file is found, default to a common config file
        for file in files:
            if file == "config.json":
                model_url = f"https://huggingface.co/{model_name}/resolve/main/{file}"
                print(f"Found config file: {file}")
                return {
                    "name": model_name,
                    "description": metadata.pipeline_tag or "No description available",
                    "url": model_url,
                    "repo_id": model_name,
                    "source": "huggingface"
                }

        print(f"Model URL not found for {model_name}")
    except Exception as e:
        print(f"Error fetching metadata for {model_name}: {e}")
    return None

def fetch_models(limit=200):
    """
    Fetch a list of models from Hugging Face API, limited to the specified number.
    """
    api = HfApi()
    models = []
    try:
        print("Fetching models from Hugging Face API...")
        models_generator = api.list_models(full=True, limit=limit)
        models = list(models_generator)
        print(f"Fetched {len(models)} models from Hugging Face API")
    except Exception as e:
        print(f"Failed to fetch models from Hugging Face API: {e}")
    return models

def update_index_file(index_file_path):
    """
    Update the index file with metadata for the top models without downloading large files.
    """
    print("Starting update_index_file function...")
    models = fetch_models()
    print(f"Fetched {len(models)} models from Hugging Face API")
    if not models:
        print("No models fetched, exiting.")
        return

    updated_models = []
    for i, model in enumerate(models):
        model_name = model.modelId
        print(f"Processing model {model_name} ({i + 1}/{len(models)})")
        if model_name:
            metadata = fetch_model_metadata(model_name)
            if metadata:
                updated_models.append(metadata)
                print(f"Added {model_name} to index.")
            else:
                print(f"Skipped {model_name} due to missing valid script.")
        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1} models...")

    print("Writing updated models to index file...")
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
