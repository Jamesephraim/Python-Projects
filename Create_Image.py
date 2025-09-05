import cv2
import numpy as np
from PIL import Image
image=(0,0,200)
img = Image.new('RGB',(200,200),(image))
img = img.resize((500, 500))
 
img.show()
cv2.waitKey(0)