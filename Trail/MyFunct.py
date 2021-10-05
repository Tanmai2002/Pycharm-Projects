import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
POI=[]
def MouseEvent(event,x,y,flags,params):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img.shape)
        mclr = (0,) *( img.shape[2] if len(img.shape)>2 else 1)
        cv2.line(img, (x, y), (x, y), mclr, 2)
        cv2.imshow('Mark Roi', img)
        POI.append((x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        mask = np.zeros_like(img)
        chanels = ( img.shape[2] if len(img.shape)>2 else 1)
        mask_color = (255,) * chanels
        cv2.fillPoly(mask, np.array([POI], np.int32), mask_color)
        final = cv2.bitwise_and(img, mask)

        img = final.copy()
        cv2.destroyAllWindows()
        cv2.putText(final,'Press d to continue',(50,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0))

        cv2.imshow('Trail2', final)

def getROI(i,Points):
    mask = np.zeros_like(i)
    chanels = (i.shape[2] if len(i.shape) > 2 else 1)
    mask_color = (255,) * chanels
    cv2.fillPoly(mask, np.array([Points], np.int32), mask_color)
    final = cv2.bitwise_and(i, mask)

    return final

def MarkRoi(i):
    global img
    img=i
    POI.clear()
    cv2.imshow('Mark Roi',img)
    cv2.setMouseCallback('Mark Roi',MouseEvent)
    if cv2.waitKey(0)& 0xFF== ord('d'):

        cv2.destroyAllWindows()
        return img,POI
def getPOI():
    return POI

