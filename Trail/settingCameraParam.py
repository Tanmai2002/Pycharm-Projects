import cv2
cap =cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:



        cv2.imshow('Trail',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
             break
    else:
        break
cap.release()
cv2.destroyAllWindows()