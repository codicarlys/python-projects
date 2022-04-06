__version__ = '0.1.0'

import PIL
from PIL import Image

img = PIL.Image.open('test_image.jpg')
H, W = img.size
compress = Image.resize((H, W), PIL.Image.ANTIALIAS)
compress.save("compress.jpg")
