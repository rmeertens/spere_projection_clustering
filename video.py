import imageio
import os

path = 'euclidian/' # on Mac: right click on a folder, hold down option, and click "copy as pathname"

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif') ):
        filenames.append(os.path.join(path, filename))

filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

print(images)

imageio.mimsave(os.path.join(path, 'movie.gif'), images, duration = 0.04) # modify duration as needed
