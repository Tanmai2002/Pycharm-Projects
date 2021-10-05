import cv2
import numpy as np
t=6
apple=cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
apple_copy=apple.copy()
orange_copy=orange.copy()

#Gaussian Pyramid
gauA=[apple_copy]
gauO=[orange_copy]
for i in range(t):
    apple_copy=cv2.pyrDown(apple_copy)
    orange_copy=cv2.pyrDown(orange_copy)
    gauA.append(apple_copy)
    gauO.append(orange_copy)

#Laplacian Pyramid
lapA=[]
lapO=[]

for i in range(t):
    lApp=cv2.subtract(gauA[i],cv2.pyrUp(gauA[i+1]))
    lapA.append(lApp)

    lOra=cv2.subtract(gauO[i],cv2.pyrUp(gauO[i+1]))
    lapO.append(lOra)
lapA.append(gauA[t])
lapO.append(gauO[t])
#Merging
mer=[]
n=0
for apple_copy,orange_copy in zip(lapA,lapO):
    rows,col,ch=apple_copy.shape
    merged=np.hstack((apple_copy[:,0:int(col/2)],orange_copy[:,int(col/2):]))
    mer.append(merged)
    n=n+1


#ReConstruction
recon=[]
reconst=mer[t]
for i in range(t,0,-1):
    #print(mer[i].shape)
    reconst=cv2.pyrUp(reconst)
    reconst=cv2.add(reconst,mer[i-1])
cv2.imshow('Trail',reconst)

cv2.waitKey(0)
cv2.destroyAllWindows()

