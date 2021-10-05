# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2.cv2 as cv
import mediapipe as mp
import numpy as np
cap=cv.VideoCapture(0)

cap.set(3,cw)
cap.set(4,ch)
mpHand=mp.solutions.hands
hands=mpHand.Hands(min_detection_confidence=0.7)
drawer=mp.solutions.drawing_utils
while cap.isOpened():
    _,img=cap.read()
    imgRgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    res=hands.process(imgRgb)
    if res.multi_hand_landmarks:
        points=[]
        for handLmK in res.multi_hand_landmarks:
            drawer.draw_landmarks(img,handLmK,mpHand.HAND_CONNECTIONS)
            for i,lmk in enumerate(handLmK.landmark):
                points.append([i,lmk.x*cw,lmk.y*ch,lmk.z*ch])
            distance=((points[8][1]-points[5][1])**2+(points[8][2]-points[5][2])**2+(points[8][3]-points[5][3])**2)**(0.5)
            print(distance)

    cv.imshow("Test",img)
    cv.waitKey(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
