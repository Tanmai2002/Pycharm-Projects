import cv2
import numpy as np
#img=cv2.imread('lena.jpg',1)
img=np.zeros([255,255,3])
img2=cv2.line(img,(0,0),(255,255),(255,255,0),1)

cv2.imshow("Trial",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

