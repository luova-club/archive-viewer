import json

PERMISSION_CLASSES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_permissions(userid):
    with open("users.json", "r") as f:
        data = json.load(f)

    if data[userid] in PERMISSION_CLASSES:
        return data[userid]
