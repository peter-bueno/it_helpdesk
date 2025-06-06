import json
import os


def save_json(file_path, data):
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
        
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}