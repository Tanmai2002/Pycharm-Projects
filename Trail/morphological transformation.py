import cv2
import numpy as np
from matplotlib import pyplot as plt
def GradientImg(rows,columns):
    t=255/columns
    img2=list(map(lambda y:[int(y*t),int(y*t),int(y*t)] ,range(columns)))
    img3=np.array(list(img2 for i in range(rows) ),np.uint8)
    return img3
img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
dil=cv2.dilate(mask,kernal,iterations=2)
erode=cv2.erode(mask,kernal)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closings =cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
imaages=[img,mask,dil,erode,opening,closings]
titles=['img','mask','dilation','erode','opening','closings']

for i in range(len(imaages)):
    plt.subplot(2,3,i+1)
    plt.imshow(imaages[i],'gray')
    plt.title(titles[i])
    plt.xticks(())
    plt.yticks(())
plt.show()