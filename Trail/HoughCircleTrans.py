import cv2
import numpy as np

img=cv2.imread('smarties.png')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(grey,5)

circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=40,minRadius=0,maxRadius=0)
detet=np.uint16(np.around(circles))
for (x,y,r) in detet[0,:]:
    cv2.circle(img,(x,y),r,(0,255,0),2)

#cv2.imshow('Test1',grey)
cv2.imshow('Test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()