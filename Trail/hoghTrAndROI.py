import cv2
import numpy as np
import MyFunct
from matplotlib import pyplot as plt
img=cv2.imread('sudoku.png')
canny=cv2.Canny(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),0,200)

tryail,_=MyFunct.MarkRoi(canny)
edges=cv2.HoughLinesP(tryail,1,np.pi/180,10,minLineLength=10,maxLineGap=5)

for l in edges:
    [x,y,w,h]=l[0]
    cv2.line(img,(x,y),(w,h),(0,0,255),1)



cv2.imshow('Trail',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
