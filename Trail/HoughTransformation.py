import cv2
import numpy as np

img=cv2.imread('sudoku.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,50,200)
lines=cv2.HoughLines(canny,1,np.pi/180,200)

for l in lines:
    r,tita=l[0]
    c=np.cos(tita)
    s=np.sin(tita)

    x1=int(r*c+1000*(-s))
    y1 = int(r * s + 1000 * (c))
    x2 = int(r * c - 1000 * (-s))
    y2 = int(r * s - 1000 * (c))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Trail',img)

cv2.imshow('Trail2',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()