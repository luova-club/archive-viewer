import os

from info import create_data, change_data

import json

# folder path
dir_path = r'/mnt/volume-hel1-1/'

images = []

videos = []

IMAGE_ID = 1

VIDEO_ID = 1
with open("info.json", "r") as f:
    currents = json.load(f)

ids: list = []

for current in currents:
    if not current == "latest_id":
        ids.append[currents[current]["path"]]


def look(dir_path, images, videos):
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if path in ids:
                continue
            if not path.split(".")[-1] in ["png", "jpg", "jpeg", "mp4", "mkv"]:
                continue

            if path.split(".")[-1] in ["png", "jpg", "jpeg"]: #TODO transfer this check to create function
                create("image", IMAGE_ID, os.path.join(dir_path, path))
                IMAGE_ID += 1 #TODO Add kitty cats

            elif path.split(".")[-1] in ["mp4", "mkv"]: #TODO transfer this check to create function
                create("video", VIDEO_ID, video, title=video)

                VIDEO_ID += 1

                videos.append(os.path.join(dir_path, path))

        if os.path.isdir(os.path.join(dir_path, path)):
            look(os.path.join(dir_path, path), images, videos)


look(dir_path, images, videos)


def create(type, id, file, title=""):
    if title == "":
        title = f'{type}_{id}'
    item = create_data(type, 'Unknown', title, file)

    new_path = file.split("/").replace(file.split(".")[-2], item.itemId)
    ids.append(new_path)
    try:
        os.rename(file, new_path)
    except FileNotFoundError:
        return

    change_data(item.itemId, new_path)


for image in images:
    create("image", IMAGE_ID, image)

    IMAGE_ID += 1


for video in videos:
    create("video", VIDEO_ID, video, title=video)

    VIDEO_ID += 1
