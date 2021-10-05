import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('sudoku.png')
h=img.shape[0]
w=img.shape[1]
pointOFROI=[(0,h),
            (w/2,h/2),
            (w,h)]

def Roi(img,points):
    mask=np.zeros_like(img)
    channel=img.shape[2]
    matchMaskColor=(255,)*channel
    cv2.fillPoly(mask,points,matchMaskColor)
    return cv2.bitwise_and(mask,img)

img2 =Roi(img,np.array([pointOFROI],np.int32))
plt.imshow(img2)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()