rows=int(input("Enter Number of Rows :"))
b=int(input("If True :Enter 1, for False Enter 0 :\n"))
t1=True
if(b==0):
    t1=False
else :
    t1=True
i=0
lst=[]
str="*"
while i<rows:
    s=str*(i+1)
    lst.append(s)
    i=i+1
if not t1:
    lst.reverse()
for star in lst:
    print(star)
