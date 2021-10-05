import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('messi5.jpg',0)
canny=cv2.Canny(img,100,200)
imaages=[img,canny]
titles=['img','lap','SX','SY','MB','BF']

for i in range(len(imaages)):
    plt.subplot(1,3,i+1)
    plt.imshow(imaages[i],'gray')
    plt.title(titles[i])
    plt.xticks(()),plt.yticks(())
plt.show()

