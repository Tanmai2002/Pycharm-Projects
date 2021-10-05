import cv2
import numpy as np
img=cv2.imread('lena.jpg',0)
l=img.copy()
gau=[l.copy()]
#Gaussian pYramid
for i in range(6):
    l=cv2.pyrDown(l)
    gau.append(l.copy())
    #cv2.imshow(f'Trail{i}',gau[i+1])

#LaplacianPyramid
for i in range(6):
    t1=cv2.pyrUp(gau[i+1])
    t2=cv2.subtract(gau[i],t1)
    cv2.imshow(f'Trail{i}',t2)
# img=np.hstack([img,t1,t2])
cv2.imshow("Trail",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
