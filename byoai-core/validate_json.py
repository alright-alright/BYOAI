import json

def validate_json(json_file):
    try:
        with open(json_file, 'r') as f:
            json.load(f)
        print("JSON file is valid.")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e.msg}")
        print(f"Error at line {e.lineno}, column {e.colno}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    json_file_path = "/Users/aerynwhite/BYOAI/byoai-core/index.json"
    validate_json(json_file_path)
