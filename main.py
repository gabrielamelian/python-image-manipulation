from PIL import Image, ImageFilter
import os

images_location = './Images/'

# size_300 = (300, 300)
#
# for f in os.listdir(images_location):
#     if f.endswith('.jpg'):
#         i = Image.open(images_location + f)
#         fn, fext = os.path.splitext(f)
#
#         i.thumbnail(size_300)
#         i.save(images_location + '300/{}_300{}'.format(fn, fext))


image1 = Image.open(images_location + 'cubes.png')
image1.filter(ImageFilter.GaussianBlur(15)).save(images_location + 'cubesedit.png')
