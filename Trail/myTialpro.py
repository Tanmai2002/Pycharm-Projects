import cv2
cut=False
def mouseClick(event,x,y,flags,params):
    global cut
    global img
    global iniimg
    print(len(temp))
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if len(points)==2:

            iniimg=temp[-1]
            temp.__delitem__(0)
            temp.append(iniimg.copy())
            return
        if len(points)>2 and cut:
            temp2=img[points[0][1]:points[1][1],points[0][0]:points[1][0]]
            img[y:y+points[1][1]-points[0][1],x:x+points[1][0]-points[0][0]]=temp2
            cv2.imshow('Trail',img)
            iniimg=img.copy()
            temp.clear()
            points.clear()
            temp.append(iniimg.copy())
            cut=False
            return

        cv2.circle(temp[-1],(x,y),3,(255,255,0),-1)
        cv2.imshow('Trail',temp[-1])
    if event==cv2.EVENT_MOUSEMOVE and len(points)>0 :
        if len(points)<2 and not cut:
            temp.__delitem__(0)
            temp.append(iniimg.copy())
            cv2.rectangle(temp[-1],points[0],(x,y),(0,0,0),1)
            cv2.imshow('Trail', temp[-1])
        if cut:
            temp.__delitem__(0)
            temp.append(iniimg.copy())
            temp3 = temp[-1][points[0][1]:points[1][1], points[0][0]:points[1][0]]
            temp[-1][y:y + points[1][1] - points[0][1], x:x + points[1][0] - points[0][0]] = temp3
            cv2.imshow('Trail', temp[-1])
    if event==cv2.EVENT_RBUTTONDOWN and len(points)>1:

        cut=True
    if event==cv2.EVENT_RBUTTONDBLCLK:
        iniimg = img.copy()
        temp.clear()
        points.clear()
        iniimg = img.copy()
        temp.append(img.copy())
        cv2.imshow('Trail', temp[-1])
        cut = False
        return






points=[]
finalpoints=[]
img=cv2.imread('lena.jpg',1)
iniimg=img.copy()
temp=[iniimg.copy()]
cv2.imshow('Trail',temp[-1])
cv2.setMouseCallback('Trail',mouseClick)

cv2.waitKey(0)
cv2.destroyAllWindows()