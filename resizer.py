from PIL import Image

import os

def resize(filename):
    img = Image.open(filename)
    filename, ext = os.path.splitext(filename)
    generate_hd(filename, ext, img)
    generate_720(filename, ext, img)

def generate_hd(filename, ext, img):
    width, height = img.size
    size = (1920, 1080)
    quality = "HD"
    if width < height:
        size = (1080, 1920)
        quality = "HD"
    if height < width:
        size = (1920, 1080)
        quality = "HD"

    img.thumbnail(size,Image.ANTIALIAS)
    img.save(f"{filename}_{quality}{ext}")

def generate_720(filename, ext, img):
    width, height = img.size
    size = (1280, 720)
    quality = "720"
    if width < height:
        size = (720, 1280)
        quality = "720"
    if height < width:
        size = (1280, 720)
        quality = "720"

    img.thumbnail(size,Image.ANTIALIAS)
    img.save(f"{filename}_{quality}{ext}")


def look(dir_path):
    for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                if not path.split(".")[-1].lower() in ["png", "jpg", "jpeg", "mp4", "mkv"]:
                    continue

                if "HD" in path or "720" in path:
                    continue

                if path.split(".")[-1].lower() in ["png", "jpg", "jpeg"]:
                    resize(os.path.join(dir_path, path))
                    print("Resized {}".format(path))

            if os.path.isdir(os.path.join(dir_path, path)):
                look(os.path.join(dir_path, path))

look("/mnt/volume-hel1-1/")