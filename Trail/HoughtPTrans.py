import cv2
import numpy as np

img=cv2.imread('sudoku.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,50,200)
#t1=np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,1,0)))

#t2=np.uint8(np.absolute(cv2.Sobel(gray,cv2.CV_64F,0,1)))
#_,canny=cv2.threshold(np.bitwise_or(t1,t2),100,200,cv2.THRESH_BINARY)

lines=cv2.HoughLinesP(canny,1,np.pi/180,150,minLineLength=10,maxLineGap=15)

for l in lines:
    [x1,y1,x2,y2]=l[0]

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Trail',img)

cv2.imshow('Trail2',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()