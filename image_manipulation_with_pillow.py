# -----------------------------------
# Practical Image Manipulation With Pillow
# -------------------------------------------
from PIL import Image

# open the image
myImage = Image.open('simon.jpg')

# show the image
myImage.show()

# crop image
box = (0, 0, 400, 400)
newImage = myImage.crop(box)
newImage.show()
