import cv2
import datetime
cap =cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_PLAIN
        text=f'Width :{cap.get(cv2.CAP_PROP_FRAME_WIDTH)}  Height :{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)} '

        time=str(datetime.datetime.now())
        frame = cv2.putText(frame, time, (10, 20), font, 1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('Trail',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
             break
    else:
        break
cap.release()
cv2.destroyAllWindows()