import cv2
import numpy as np

def DoSomething(x):
    return

img=np.zeros((300,500,3),np.uint8)
cv2.namedWindow('img')


cv2.createTrackbar('b','img',0,255,DoSomething)
cv2.createTrackbar('g','img',0,255,DoSomething)
cv2.createTrackbar('r','img',0,255,DoSomething)
while True:
    cv2.imshow('img',img)

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos('b','img')
    g=cv2.getTrackbarPos('g','img')
    r=cv2.getTrackbarPos('r','img')
    img[:]=[b,g,r]

cv2.destroyAllWindows()