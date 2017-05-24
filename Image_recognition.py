import pytesseract
import os
from PIL import Image

result = []
image_folder = input('Input image folder:')
for image_name in os.listdir(image_folder):
    image = Image.open('%s\%s'%(image_folder,image_name))
    result.append(pytesseract.image_to_string(image))
print(result)
