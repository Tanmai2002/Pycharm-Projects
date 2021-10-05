import os
import shutil
import cv2 as cv
import glob
import test
from test import face
fPath=r'C:\Users\tanma\Desktop\MI19062021\Media\WhatsApp Documents - Copy'


def addFolder(folderName):
    t = f'{fPath}\{folderName}'
    if not os.path.exists(t):
        os.mkdir(t)


if __name__=="__main__":
    fre=test.FaceRecog()
    fre.LoadEncoding()

    tags=[i.tag for i in test.KnownFaces]
    addFolder('Unknown')
    for t in tags:
        print(t)
        addFolder(t)
    for i in glob.glob(f'{fPath}\*.jpg'):
        try:
            CurImg=cv.imread(i)
            e = fre.getFacesEncode(CurImg)

            print(i)
            if e:
                c = fre.compareFaces(e,DontAskunknownver=True)
                tags=[i[2] for i in c]
                tags=list(filter(lambda x:not x.__eq__('Unknown'),tags))
                a='Unknown'
                if len(tags)>0:
                    a=max(tags,key=tags.count)
                k=os.path.split(i)[-1]
                print(k)
                shutil.move(i,f'{fPath}\{a}\{k}')
        except Exception as excp:
            print(excp)
