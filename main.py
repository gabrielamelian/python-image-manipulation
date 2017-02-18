from PIL import Image
import os

# image1 = Image.open('./Images/cubes.png')
images_location = './Images/'

for f in os.listdir(images_location):
    if f.endswith('.jpg'):
        i = Image.open(images_location + f)
        fn, fext = os.path.splitext(f)
        print fn
# image1.save('./Images/cubes.jpg')
# image1.show()
