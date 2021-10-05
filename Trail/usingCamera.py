import cv2
cap =cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('Trail',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):

        break
cap.release()
cv2.destroyAllWindows()