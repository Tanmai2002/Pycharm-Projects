import cv2
cap=cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thr=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thr,None,iterations=3)

    cont,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in cont:

        if cv2.contourArea(c)<=1000:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)




    cv2.imshow('Trail',frame1)
    frame1=frame2
    _,frame2=cap.read()
    if cv2.waitKey(50)==27:
        break
cv2.destroyAllWindows()