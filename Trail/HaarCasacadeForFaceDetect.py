import cv2
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeCas=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(grey)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=grey[y:y+h,x:x+w]
        roi_col=frame[y:y+h,x:x+w]
        eyes=eyeCas.detectMultiScale(roi_gray)
        for (x1,y1,w1,h1) in eyes:
            cv2.rectangle(roi_col,(x1,y1),(x1+w1,y1+h1),(0,255,0))


    cv2.imshow('Trail',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('d'):

        break
cap.release()
cv2.destroyAllWindows()

