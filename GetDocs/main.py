import os
import cv2
from pathlib import Path
currentFolderPath='C:\\Users\\tanma\\Desktop\\GetDoc'
os.chdir(currentFolderPath)
def getfiles():
    t=0
    for i in os.listdir(currentFolderPath):
        t+=1
        print(f'{t}:{i}')
    del t
def changeDir(folder):
    global currentFolderPath

    if folder != "..":
        temp = currentFolderPath
        try:
            currentFolderPath = currentFolderPath + '\\' + folder
            os.chdir(currentFolderPath)
            getfiles()
        except Exception as e:
            print(e)
            currentFolderPath = temp
        del temp
        return
    currentFolderPath=(Path(currentFolderPath).parent)
    os.chdir(currentFolderPath)
    return
changeDir('Tanmai')




