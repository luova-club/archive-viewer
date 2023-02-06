import json


from models import item


def load_data() -> dict:
    with open("info.json", "r") as f:
        data = json.load(f)

    return data


def load_items() -> list:
    data = load_data()
    items = []

    for item in data:
        if item == "latest_id":
            continue
        items.append(get_data(item))

    return items


def get_data(itemId) -> dict:
    data = load_data()

    type = data[itemId]["type"]
    owner = data[itemId]["owner"]
    title = data[itemId]["title"]
    path = data[itemId]["path"]

    item_model = item(itemId, type, owner, title, path)

    return item_model


def create_data(type, owner, title, path) -> item:
    data = load_data()

    data["latest_id"] = int(data["latest_id"])+1

    latest_id = data["latest_id"]

    data[latest_id] = {"type": type, "owner": owner,
                       "title": title, "path": path}

    item_model = item(latest_id, type, owner, title, path)

    with open("info.json", "w") as f:
        json.dump(data, f)

    return item_model


def change_data(itemId, path):
    data = load_data()

    data[itemId]["path"] = path

    with open("info.json", "w") as f:
        json.dump(data, f)
