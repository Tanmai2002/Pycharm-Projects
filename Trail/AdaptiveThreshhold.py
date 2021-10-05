import cv2
import numpy as np
def GradientImg(rows,columns):
    t=255/columns
    img2=list(map(lambda y:[int(y*t),int(y*t),int(y*t)] ,range(columns)))
    img3=np.array(list(img2 for i in range(rows) ),np.uint8)
    return img3
img=cv2.imread('lena.jpg',0)
_,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
img3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,7)



cv2.imshow('try',img3)
cv2.imshow('try2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()