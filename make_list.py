import os

from info import create_data, change_data

# folder path
dir_path = r'/mnt/volume-hel1-1/'

images = []

videos = []

IMAGE_ID = 1

VIDEO_ID = 1


def look(dir_path, images, videos):
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if not path.split(".")[-1] in ["png", "jpg", "jpeg", "mp4", "mkv"]:
                continue

            if path.split(".")[-1] in ["png", "jpg", "jpeg"]:
                images.append(os.path.join(dir_path, path))

            elif path.split(".")[-1] in ["mp4", "mkv"]:
                videos.append(os.path.join(dir_path, path))

        if os.path.isdir(os.path.join(dir_path, path)):
            look(os.path.join(dir_path, path), images, videos)


look(dir_path, images, videos)


def create(type, id, file, title=""):
    if title == "":
        title = f'{type}_{id}'
    item = create_data(type, 'Unknown', title, file)

    new_path = file.split("/").replace(file.split(".")[-2], item.itemId)
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
