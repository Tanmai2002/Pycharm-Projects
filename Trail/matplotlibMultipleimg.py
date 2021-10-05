import cv2
import numpy as np
from matplotlib import pyplot as plt
def GradientImg(rows,columns):
    t=255/columns
    img2=list(map(lambda y:[int(y*t),int(y*t),int(y*t)] ,range(columns)))
    img3=np.array(list(img2 for i in range(rows) ),np.uint8)
    return img3
img=GradientImg(500,500)
_,img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,img3=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

_,img5=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

_,img6=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

imaages=[img,img2,img3,img5,img6]
titles=['t1','t2','t3','t4','t5',]

for i in range(len(imaages)):
    plt.subplot(5,5,i+1)
    plt.imshow(imaages[i])
    plt.title(titles[i])
plt.show()

