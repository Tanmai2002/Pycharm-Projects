import cv2
import numpy as np
import MyFunct
v='vtest.avi'


def linesOnVideo(video):
    cap=cv2.VideoCapture(video)
    _,f1=cap.read()
    canny=cv2.Canny(cv2.cvtColor(f1,cv2.COLOR_BGR2GRAY),100,200)
    ROI,POI=MyFunct.MarkRoi(canny)
    while cap.isOpened():
        lines=cv2.HoughLinesP(ROI,2,np.pi/180,150,minLineLength=50,maxLineGap=5)
        if lines :
            for l in lines:
                [x,y,w,h]=l[0]
                cv2.line(f1,(x,y),(w,h),(0,0,255),2)
        cv2.imshow("Trail",f1)
        if cv2.waitKey(10) & 0xFF==ord('d'):
            cv2.destroyAllWindows()
            break
        _,f1=cap.read()
        canny = cv2.Canny(cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY),100, 200)
        ROI=MyFunct.getROI(canny,POI)
linesOnVideo(v)
