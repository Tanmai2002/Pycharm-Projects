import cv2.cv2 as cv2
import numpy as np
def GradientImg(rows,columns):
    t=255/columns
    img2=list(map(lambda y:[int(y*t),int(y*t),int(y*t)] ,range(columns)))
    img3=np.array(list(img2 for i in range(rows) ),np.uint8)
    return img3
img=GradientImg(500,500)
out=cv2.imwrite('gradient.jpg',img)
print(out)
_,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,img3=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

_,img5=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

_,img6=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)




cv2.imshow('try',img2)
cv2.imshow('try2',img5)
cv2.waitKey(0)
cv2.destroyAllWindows()