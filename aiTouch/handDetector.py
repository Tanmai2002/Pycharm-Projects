import mediapipe as mp
import cv2.cv2 as cv
import numpy as np
cw=640
ch=480
class handDetector:
    def __init__(self,minDetect=0.5,minTrack=0.5,detectAndTrack=False,maxHands=2,):
        self.minDetect=minDetect
        self.minTrack=minTrack
        self.detectAndTrack=detectAndTrack
        self.maxHands=maxHands
        self.mpHands=mp.solutions.hands
        self.Hands=self.mpHands.Hands(detectAndTrack,maxHands,minDetect,minTrack)
        self.drawer=mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
        img=cv.flip(img,1)
        imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.res = self.Hands.process(imgRgb)
        if self.res.multi_hand_landmarks and draw:
            for handLmK in self.res.multi_hand_landmarks:
                self.drawer.draw_landmarks(img, handLmK, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPositions(self):
        points=[]
        if self.res.multi_hand_landmarks:
            for handLmK in self.res.multi_hand_landmarks:
                for i, lmk in enumerate(handLmK.landmark):
                    points.append([i, lmk.x * cw, lmk.y * ch, lmk.z * ch])
        return points
    def distance(self,points,startPoint,endPoint,In3D=False):
        distance =np.hypot(points[startPoint][1]-points[endPoint][1],points[startPoint][2]-points[endPoint][2])
        if In3D:
            distance=((points[startPoint][1]-points[endPoint][1])**2+(points[startPoint][2]-points[endPoint][2])**2+
                  (points[startPoint][3]-points[endPoint][3])**2)**0.5
        return distance
    def fingersup(self):
        up=[0]*5
        points=self.findPositions()
        tips=[4,8,12,16,20]
        if len(points)>0:
            for i in range(5):
                if i==0:
                    t=points[20][1]-points[8][1]
                    t=t/abs(t)
                    up[i] = 1 if points[tips[i]][1]*t < points[tips[i] -1][1]*t  else 0
                    continue
                up[i]=1 if points[tips[i]][2]<points[tips[i]-2][2] else 0
        return up
if __name__=="__main__":
    detector=handDetector(minDetect=0.75)
    cap=cv.VideoCapture(0)
    while cap.isOpened():
        _,img=cap.read()
        img=detector.findHands(img)
        l=detector.fingersup()
        print(l)
        cv.imshow("Test",img)
        cv.waitKey(1)