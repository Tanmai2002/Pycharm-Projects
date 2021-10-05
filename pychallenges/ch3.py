stri=""
upper=list(i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower=list(i for i in "abcdefghijklmnopqrstuvwxyz")
def checkforMid(strin):
    for t1 in range(9):
        if t1==4 or t1==0 or t1==8:
            if str(strin)[t1] in upper:
                return False
        else:
            if str(strin)[t1] in lower:
                    return False
    return True
with open('t3.txt','r') as f:
    for line in f:
        c=0
        z=len(line)
        while (z)>(c+8):
            temp=line[c:c+9]
            if (checkforMid(temp)):
                stri=stri+temp[4]
            c=c+1
print(stri)









