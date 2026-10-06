import json

FILE_PATH = "Database/leaves.json"


def load_leaves():

    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    return data


def save_leaves(data):

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)