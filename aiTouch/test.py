import cv2.cv2 as cv
import mediapipe as mp
cap=cv.VideoCapture(0)
test=mp.solutions.face_detection.FaceDetection()
drawer=mp.solutions.drawing_utils
while cap.isOpened():
    _,img=cap.read()
    imgRgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    poses=test.process(image=imgRgb)
    if poses.detections:
        for detection in poses.detections:
                drawer.draw_detection(img,detection,)
        print("Tr")
    cv.imshow("Test",img)
    cv.waitKey(1)