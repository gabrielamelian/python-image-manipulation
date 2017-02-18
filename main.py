from PIL import Image
import os

# image1 = Image.open('./Images/cubes.png')
images_location = './Images/'

size_300 = (300, 300)

for f in os.listdir(images_location):
    if f.endswith('.jpg'):
        i = Image.open(images_location + f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save(images_location + '300/{}_300{}'.format(fn, fext))


# image1.save('./Images/cubes.jpg')
# image1.show()
