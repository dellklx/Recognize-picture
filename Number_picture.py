import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Picture_folder = input('Picture folder:')
image_names = []
for name in os.listdir(Picture_folder):
    image_names.append('%s\%s'%(Picture_folder,name))

Save_path = input('Save path:')
for image_name in image_names:
    im = Image.open(image_name)
    box = im.copy() #直接复制图像
    box = (300,250,800,400)
    region = im.crop(box)
    region.save('%s\%s.tiff'%(Save_path,os.path.split(image_name)[1].split('.')[0]),'TIFF',dpi=(300,300))