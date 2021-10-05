import cv2.cv2 as cv
import handDetector as hd
import autopy
import  numpy as np
cap=cv.VideoCapture(0)

detector=hd.handDetector(minDetect=0.65,maxHands=1)
mouseCTRL=autopy.mouse
cw=640
ch=480
cap.set(3,cw)
cap.set(4,ch)
sw,sh=autopy.screen.size()
px,py=0,0
cy,cx=0,0
smooth=25
fx, fy, padsize, padsize2 = 250, 100,70,70#200,150#70, 70
while cap.isOpened():
    _,img=cap.read()
    img=detector.findHands(img)
    points=detector.findPositions()
    ups=detector.fingersup()
    if ups==[0,1,0,0,0]:
        cv.rectangle(img,(fx,fy),(fx+padsize,fy+padsize2),(0,0,255))
        # print(points[8])
        x1=np.interp(points[8][1],(fx,fx+padsize),(-30,sw+30))
        y1=np.interp(points[8][2],(fy,fy+padsize2),(-30,sh+30))
        cx=px+(x1-px)/smooth
        cy = py + (y1 - py) / smooth
        if(cx>sw):
            cx=sw-1
        elif(cx<0):
            cx=1
        if (cy > sh):
            cy = sh-1
        elif (cy < 0):
            cy = 1
        mouseCTRL.move(cx,cy)
        px=cx
        py=cy
    if ups==[1,1,1,1,1]:
        fx=int(points[7][1]-padsize//2)
        fy = int(points[7][2] - padsize2 // 2)
        # print(fy,fy)
    if ups==[0,1,1,0,0]:
        if detector.distance(points,8,5)/detector.distance(points,8,12)>4:
            mouseCTRL.click()
    cv.imshow("Test",img)
    cv.waitKey(1)