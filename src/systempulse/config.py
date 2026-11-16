import json


def load_config(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    if "websites" not in data:
        raise ValueError("Missing required key: websites")

    if not isinstance(data["websites"], list):
        raise ValueError("Websites must be a list")

    return data
