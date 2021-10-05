import numpy as np
import cv2

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def onCli(event,x,y,flags,params):

    if event== cv2.EVENT_LBUTTONDOWN:
        font =cv2.FONT_HERSHEY_PLAIN
        points.append((x,y))
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        if(len(points)>=2):
            cv2.line(img,points[-1],points[-2],(0,255,255),3)

        cv2.imshow('Title',img)


points=[]
img=np.zeros((500,500,3),np.uint8)
cv2.imshow('Title',img)
cv2.setMouseCallback('Title', onCli)
cv2.waitKey(0)
cv2.destroyAllWindows()