import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernal=np.ones((5,5))/25
filter2D=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5))
GauBlur=cv2.GaussianBlur(img,(5,5),0)
mDBlur=cv2.medianBlur(img,5)
Bil=cv2.bilateralFilter(img,9,75,75)

imaages=[img,filter2D,blur,GauBlur,mDBlur,Bil]
titles=['img','Filter2d','blur','GB','MB','BF']


for i in range(len(imaages)):
    plt.subplot(2,3,i+1)
    plt.imshow(imaages[i])
    plt.title(titles[i])
    plt.xticks(()),plt.yticks(())
plt.show()

