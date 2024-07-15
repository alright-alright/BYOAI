import os
import subprocess

# Path to the index.json file and the update_index.py script
index_file_path = "./byoai-core/index.json"
update_script_path = "./update_index.py"

def remove_index_file(index_file_path):
    try:
        if os.path.exists(index_file_path):
            os.remove(index_file_path)
            print(f"Removed {index_file_path} successfully.")
        else:
            print(f"{index_file_path} does not exist.")
    except Exception as e:
        print(f"Error removing {index_file_path}: {e}")

def regenerate_index_file(update_script_path):
    try:
        result = subprocess.run(['python', update_script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("Index file regenerated successfully.")
        else:
            print(f"Error regenerating index file: {result.stderr}")
    except Exception as e:
        print(f"Error running {update_script_path}: {e}")

if __name__ == "__main__":
    remove_index_file(index_file_path)
    regenerate_index_file(update_script_path)
