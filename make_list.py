import os

import json

# folder path
dir_path = r'/mnt/volume-hel1-1/'

# list to store files
res = []

# Iterate directory
def look(dir_path, res):
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    
        if os.path.isdir(os.path.join(dir_path, path)):
            look(os.path.join(dir_path, path), res)

look(dir_path, res)


jso = dict()

for resi in res:
    jso[resi] = {"title": resi, "poster": ""}
with open("info.json", "w") as f:
    json.dump(jso, f)