import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
lap=cv2.Laplacian(img,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))

Sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
Sobelx=np.uint8(np.absolute(Sobelx))
Sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
Sobely=np.uint8(np.absolute(Sobely))

Sobelcomb1=cv2.Sobel(img,cv2.CV_64F,1,1)
Sobelcomb1=np.uint8(np.absolute(Sobelcomb1))

soblcomb2=np.bitwise_or(Sobelx,Sobely)
imaages=[img,lap,Sobelx,Sobely,Sobelcomb1,soblcomb2]
titles=['img','lap','SX','SY','MB','BF']

for i in range(len(imaages)):
    plt.subplot(2,3,i+1)
    plt.imshow(imaages[i])
    plt.title(titles[i])
    plt.xticks(()),plt.yticks(())
plt.show()

