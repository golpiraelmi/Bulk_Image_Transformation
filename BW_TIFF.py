from PIL import Image
import os

# Finding the absolute path to the folder where the input images are located
path = os.path.abspath('input_images/')

# Creates a folder for output images
os.mkdir('BW_TIFF')

for f in os.listdir(path):
    if f.endswith('.jpg'):
        path_image = path + '/' + f  # This creates the absolute path for each image
        img = Image.open(path_image)
        file_name, file_extension = os.path.splitext(f)  # Separating the file name from its extension

        # Creating a black and white .tiff images from original .jpg files
        img.convert(mode='L').save('BW_TIFF/{}.tiff'.format(file_name))

        