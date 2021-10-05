import numpy as np
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def onCli(event,x,y,flags,params):

    if event== cv2.EVENT_LBUTTONDOWN:
        font =cv2.FONT_HERSHEY_PLAIN
        text=f'({x},{y})'

        cv2.putText( img,text,(x,y),font,0.7,(255,255,255))
        cv2.imshow('Title',img)
    if event == cv2.EVENT_RBUTTONDOWN:
            font = cv2.FONT_HERSHEY_PLAIN
            text = f'({img[y,x,0]},{img[y,x,1]},{img[y,x,2]})'

            cv2.putText(img, text, (x, y), font, 0.7, (0, 255, 255))
            cv2.imshow('Title', img)


img=cv2.imread('lena.jpg',1)
cv2.imshow('Title',img)
cv2.setMouseCallback('Title', onCli)
cv2.waitKey(0)
cv2.destroyAllWindows()