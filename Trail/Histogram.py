import cv2
from matplotlib import pyplot
img=cv2.imread('lena.jpg',0)

hist=cv2.calcHist([img],[0],None,[256],[0,256])

pyplot.plot(hist)
pyplot.show()
