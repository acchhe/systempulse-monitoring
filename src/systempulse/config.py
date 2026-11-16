
import json


def load_config(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    if "websites" not in data:
        raise ValueError("Missing required key: websites")

    if not isinstance(data["websites"], list):
        raise ValueError("Websites must be a list")

    # Use 60 seconds if check_interval is missing
    interval = data.get("check_interval", 60)

    if type(interval) is not int:
        raise ValueError("Interval must be of type int")

    if interval <= 0:
        raise ValueError("Interval must be greater than 0")

    data["check_interval"] = interval

    return data

