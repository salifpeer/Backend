import json
def load_details():
    with open("Database/register.json", "r") as file:
        data = json.load(file)

    return data
def save_details(data):
    with open("Database/register.json", "w") as file:
        json.dump(data, file, indent=4)
    