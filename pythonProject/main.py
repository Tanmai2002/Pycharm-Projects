import cv2 as cv
import  face_recognition as fr
import test
# img=cv.imread('test2.jpg')
frtes=test.FaceRecog()
# img=cv.resize(img,(512,512))
# e1=frtes.getFacesEncode(img)
# c1=frtes.compareFaces(e1)
# c2=frtes.compareFaces(frtes.getFacesEncode(cv.imread('tanmai.jpg')))
# c3=frtes.compareFaces(frtes.getFacesEncode(cv.imread('Tab2.jpg')))

# imgRGb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
# res1 = fr.face_locations(imgRGb)
# print(res1)
# tEn=fr.face_encodings(imgRGb,res1)[0]
# t2=fr.face_encodings(cv.cvtColor(cv.imread('Tab2.jpg'),cv.COLOR_BGR2RGB))[0]
cap=cv.VideoCapture(0)


# for (y, h, k, x) in res1:
#
#     t3=imgRGb[max(y-10,0):min(k+10,512),max(x-10,0):min(h+10,512)]
#     cv.imshow('p',t3)
#     # cv.rectangle(imgRGb, (x, y), (h, k), (255, 0, 0))
#     # cv.imshow('try',imgRGb)
#     cv.waitKey(1500)
#     # z=fr.face_encodings(t3,[(0,h-x,k-y,0)])[0]
#     # z=test.findEncoding(imgRGb,res1[0])
#
#     z=frtes.getFacesEncode(imgRGb)
#     print(z)
#     listTest+=z
# for i in range(3):
#     test.FaceRecog.AddtoKnownEncoding(listTest[i],f'n{i+1}','Me')
# test.FaceRecog.pickleEncodings()
# test.FaceRecog.LoadEncoding()
# while True:
#     _,tes=cap.read()
#     res = fr.face_locations(tes)
#     # for (y, h, k, x) in res:
#     #     cv.rectangle(tes, (x, y), (h, k), (255, 0, 0))
#
#     PEn=fr.face_encodings(tes)
#     # print(len(PEn))
#     if len(PEn)>0:
#         # PEn=PEn[0]
#         comp=frtes.compareFaces(PEn)
#         print(comp[0][0])
#
#     cv.imshow("Test",tes)
#     cv.waitKey(1)
imtest=cv.imread('test4.jpg')
# imtest=cv.resize(imtest,(512,512))
pen=frtes.getFacesEncode(imtest)
if pen:
        compp=frtes.compareFaces(pen)
        print(compp[0][0])
# while True:
#     _,tIm=cap.read()
#     cv.imshow('vid',tIm)
#     e=frtes.getFacesEncode(tIm)
#     if e:
#         c=frtes.compareFaces(e)
#         print(c[0][0])
#         cv.waitKey(1)
#         # print('pickled')
#         # frtes.pickleEncodings()
#         # break
# cv.waitKey(0)
# cv.destroyAllWindows()