import json


def read_json_file(file_path):
    with open(file_path, 'r',encoding="utf-8") as f:
        data = json.load(f,encoding='utf-8')
    return data

