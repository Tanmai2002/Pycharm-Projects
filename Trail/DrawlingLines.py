import cv2
img=cv2.imread('lena.jpg',1)
img2=cv2.line(img,(0,0),(100,100),(255,255,0),1)

cv2.imshow("Trial",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

