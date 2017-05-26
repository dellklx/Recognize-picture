import pytesseract
import os
from PIL import Image
import cv2
result = []
image_folder = input('Input image folder:')
count = 0
for image_name in os.listdir(image_folder):
    result.append(int(image_name.split('.')[0]))
    # imagetostring = Image.open('%s\%s'%(image_folder,image_name))
    #
    # try:
    #     number = int(pytesseract.image_to_string(imagetostring))
    # except ValueError:
    #     image = cv2.imread('%s\%s' % (image_folder, image_name))
    #     res = cv2.resize(image, (512, 512), interpolation=cv2.INTER_CUBIC)
    #     cv2.namedWindow("Image")
    #     cv2.imshow("Image", res)
    #     cv2.waitKey(10)
    #     number = int(input("input right number:"))
    #     cv2.destroyAllWindows()

#     result.append(number)
#     count += 1
#     print(count)
#
print(result)