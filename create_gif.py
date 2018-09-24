import imageio
import os

def gif_from_folder(path, extensions, filename):
    

    image_folder = os.fsencode(path)

    filenames = []

    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        if filename.endswith( extensions ):
            filenames.append(os.path.join(path, filename))

    filenames.sort() # this iteration technique has no built in order, so sort the frames

    images = list(map(lambda filename: imageio.imread(filename), filenames))
    imageio.mimsave(filename, images, duration = 0.04) # modify duration as needed
