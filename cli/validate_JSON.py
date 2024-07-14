import json

try:
    with open('index.json', 'r') as f:
        data = json.load(f)
    print("JSON is valid")
except json.JSONDecodeError as e:
    print(f"JSON is invalid: {e}")
except FileNotFoundError:
    print("index.json file not found")
