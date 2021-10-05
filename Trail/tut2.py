import cv2
img=cv2.imread('lena.jpg',0)
cv2.imshow("Trial",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('lenaCopy.jpg',img,)
