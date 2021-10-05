import cv2
img=cv2.imread('pic1.png')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(grey,240,255,cv2.THRESH_BINARY)
contour,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)
for c in contour:
    approx=cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
    cv2.drawContours(img,[approx],-1,(255,0,0),5)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    cv2.putText(img,str(len(approx) )+"i",(x,y),cv2.FONT_HERSHEY_PLAIN,3,(0,255,255))
    print(True)

cv2.imshow('Trail',grey)
cv2.waitKey(0)
cv2.destroyAllWindows()