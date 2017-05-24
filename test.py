from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
im = Image.open(r'D:\temp\0020.jpg')
box = im.copy() #直接复制图像
box = (300,250,800,400)
region = im.crop(box)
region.save(r'D:\temp\1\20.tiff','TIFF',dpi=(300,300) )