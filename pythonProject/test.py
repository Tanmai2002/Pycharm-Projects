import cv2 as cv
import face_recognition as fr
import pickle
import numpy as np
import mediapipe
import glob
import shutil
# KnownEncodings=[]
# nameofcurEncode=[]
KnownFaces=[]
class FaceRecog():
    @classmethod
    def AddtoKnownEncoding(cls,encoding,name,tag):
        t=face(encoding,name,tag)
        KnownFaces.append(t)
        print(len(KnownFaces))
        FaceRecog.pickleEncodings()

    @classmethod
    def pickleEncodings(cls):
        t={'face':KnownFaces}
        f=open(r'encoding','wb')
        pickle.dump(t,f)
        f.close()


    @classmethod
    def LoadEncoding(cls):
        try:
            global KnownFaces
            f=open(r'encoding','rb')
            t=pickle.load(f)
            f.close()
            KnownFaces=t['face']
        except Exception as e:
            print(e)

    @classmethod
    def findEncoding(cls,img,resElement):
        return fr.face_encodings(img,[resElement])[0]

    def facesdetect(self):
        self.faceLoc=fr.face_locations(self.imgRGB)
        return self.faceLoc

    def getFacesEncode(self,img):
        self.img=img
        self.imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.facesdetect()
        faces=self.faceLoc
        if len(faces)>0:
            l=[]
            for face in faces:
                l.append(FaceRecog.findEncoding(self.imgRGB,face))
            return l
        else:
            return None

    def compareFaces(self,Encodings,DontAskunknownver=False):
        name=[]
        # print(len(Encodings))
        for j,e in enumerate(Encodings):
            t=100
            a=None
            KnownEncodings=[i.encoding for i in KnownFaces]
            res=fr.compare_faces(KnownEncodings,e,0.5)
            dis=fr.face_distance(KnownEncodings,e)
            for i,d in enumerate(dis):
                if res[i]:
                    if d<t:
                        a=KnownFaces[i]
                        t=d
            if t<1:
                name.append([a.name,e,a.tag])
            elif DontAskunknownver:
                name.append(['Unknown', e, 'Unknown'])
            else:
                face=[self.faceLoc[j]]
                tImg = self.img.copy()
                for (y,h,k,x) in face:
                    # print(self.faceLoc[0])


                    try:
                        w, hei,_ = self.img.shape
                        x=int(np.interp(x,(0,hei),(0,512)))
                        h=int(np.interp(h,(0,hei),(0,512)))
                        y=int(np.interp(y,(0,w),(0,512)))
                        k=int(np.interp(k,(0,w),(0,512)))
                        tImg=cv.resize(tImg,(512,512))
                        print(x,y,h,k)
                    except Exception as te:
                        print(te)
                    cv.rectangle(tImg, (x, y), (h, k), (0, 0, 255))

                cv.namedWindow('Identify')
                cv.imshow("Identify", tImg)

                print("Found an Unknown face,Wish to add? \n y:Yes\t n:no\n")
                ans=cv.waitKey(0) & 0xFF
                if ans==ord('y'):
                        cv.destroyWindow('Identify')

                        tName=input('Name :')
                        tag=input('Tag :')
                        # cv.waitKey(10000)
                        if len(tName)>0:
                            ###########################Test############################
                            names=[i.name for  i in KnownFaces]
                            if tName in names:
                                n=names.index(tName)
                                KnownFaces[n].AddEnCoding(e)
                            else:
                            ##########################################################
                                FaceRecog.AddtoKnownEncoding(e,tName,tag)
                            name.append([tName, e,tag])

                        else:
                            name.append(['Unknown', e,'Unknown'])
                else:
                        cv.destroyWindow('Identify')
                        name.append(['Unknown',e,'Unknown'])

        if len(name)>0:

            return name
        else:
            return None




class face():
    def __init__(self,Encoding,Name,Tag):
        self.encoding=Encoding
        self.name=Name
        self.tag=Tag
        self.count=1
    def AddEnCoding(self,e):
        self.encoding=(self.encoding*self.count+e)/(self.count+1)
        self.count+=1





if __name__=='__main__':
    # shutil.move('aai.jpg', r'aai.jpg')
    fre=FaceRecog()
    FaceRecog.LoadEncoding()

    # for i in glob.glob(r'C:\Users\tanma\Desktop\MI19062021\Media\WhatsApp Documents\*.jpg'):
    i=r'C:\Users\tanma\Desktop\MI19062021\Media\WhatsApp Documents - Copy\Trail.jpg'
    CurImg=cv.resize(cv.imread(i), (512, 512))
    e=fre.getFacesEncode(CurImg)
    # cv.imshow('CurImg',CurImg)
    # cv.waitKey(3000)
    # cv.destroyWindow('CurImg')
    print(i)
    if e:
        cv.imshow('CurImg',CurImg)
        cv.waitKey(3000)
        cv.destroyWindow('CurImg')
        c=fre.compareFaces(e)
        for f in c:
            print(f[0])
