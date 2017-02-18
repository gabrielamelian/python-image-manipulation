from PIL import Image
import os

# image1 = Image.open('./Images/cubes.png')
imagesLocation = './Images/'

for f in os.listdir(imagesLocation):
    if f.endswith('.jpg'):
        i = Image.open(imagesLocation + f)
        fn, fext = os.path.splitext(f)
        print fn
# image1.save('./Images/cubes.jpg')
# image1.show()
