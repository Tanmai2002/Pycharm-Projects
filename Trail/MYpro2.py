import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('sudoku.png')
cv2.imshow('Trail',img)
POI=[]
def Mouseclick(event,x,y,flags,params):
    global img
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.line(img,(x,y),(x,y),(0,0,255),2)
        cv2.imshow('Trail',img)
        POI.append((x,y))
    if event==cv2.EVENT_RBUTTONDOWN:
        mask=np.zeros_like(img)
        chanels=img.shape[2]
        mask_color=(255,)*chanels
        cv2.fillPoly(mask,np.array([POI],np.int32),mask_color)
        final=cv2.bitwise_and(img,mask)

        img=final
        cv2.destroyAllWindows()
        plt.imshow(final)
        cv2.imshow('Trail3', mask)
        cv2.imshow('Trail2', img)
        plt.show()



cv2.setMouseCallback('Trail',Mouseclick)
cv2.waitKey(0)
cv2.destroyAllWindows()
