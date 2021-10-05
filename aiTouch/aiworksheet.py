import cv2.cv2 as cv
import numpy as np
from pytesseract import pytesseract as tes
def makePage():
    img=np.zeros((480,360,3),np.uint8)
    img.fill(255)
    cv.line(img,(0,60),(360,60),(0,0,255))
    cv.line(img,(0,58),(360,58),(0,0,255))
    cv.line(img,(60,0),(60,480),(0,0,255))
    cv.line(img,(58,0),(58,480),(0,0,255))
    for i in range(420//20):
        cv.line(img,(0,80+i*20),(360,80+i*20),(0,0,0))
    return img
# path=r'C:\Users\tanma\tesseract\tesseract.exe'
# tes.tesseract_cmd=path
img=cv.imread('test6.jpg')
t=2
for _ in range(t):
    img=cv.pyrDown(img)
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
shap=imggray.shape
fImg=imggray.copy()
for i in range(shap[0]):
    fImg[i,0]=255
    avg=sum(imggray[i,:]/shap[1])
    for j in range(1,shap[1]):
        if imggray[i,j]-avg<(-25):
            fImg[i,j]=0
        else:
            fImg[i,j]=255
fImg2=fImg.copy()
for j in range(shap[1]):
    avg=sum(imggray[:,j]/shap[0])
    for i in range(shap[0]):
        if fImg[i,j]==255 and imggray[i,j]-avg<(-50):
            fImg[i,j]=0
print(fImg)
qimf = img[:, :, 2]
cv.imshow("Test",fImg)
cv.imshow("Test2",fImg2)

cv.waitKey(0)