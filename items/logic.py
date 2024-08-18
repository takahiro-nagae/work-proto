import json
import os


def load_json(filename):
    with open(os.path.join(os.getcwd(), 'items/data', filename), 'r', encoding='utf-8') as file:
        return json.load(file)


def build_dict_for_list(data, key, value):
    return {item[key]: item[value] for item in data}