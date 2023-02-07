# create thumbnails of all images in a directory
from os import listdir
from os import makedirs
from os.path import splitext
from os.path import join
from PIL import Image
 
# load an image and save a thumbnail version
def save_thumbnail(inpath, outpath):
    # load the image
    with Image.open(inpath) as image:
        # create a thumbnail image
        image.thumbnail((128,128))
        # save the thumbnail image in PNG format
        image.save(outpath, 'PNG')

# return the output path for a thumbnail image
def get_output_path(save_path, filename, extension):
    # separate the filename into name and extension
    name, _ = splitext(filename)
    # construct a new filename
    out_filename = f'{name}_thumbnail.{extension}'
    # construct the output path
    outpath = join(save_path, out_filename)
    return outpath
 
# entry point
def main():
    # location for loading images
    image_path = 'gatto'
    # location for saving image thumbnails
    save_path = 'tmp'
    # create the output directory
    makedirs(save_path, exist_ok=True)
    # list all images in the source location
    for filename in listdir(image_path):
        # construct the input path
        inpath = join(image_path, filename)
        # construct the output path
        outpath = get_output_path(save_path, filename, 'png')
        # create the thumbnail
        save_thumbnail(inpath, outpath)
        # report progress
        print(f'.saved {outpath}')
 
if __name__ == '__main__':
    main()

