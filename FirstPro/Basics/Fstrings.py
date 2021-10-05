#Basic formatting Methods
#Method 1
ti="Tanmai"
a=3
m="hii %s ,Ur score is %s"%(ti,a)
print(m) #hii Tanmai ,Ur score is 3

#######################
nam="Tanmai"
sur="Kamat"
#Method 2

temp="He is {} {}"
temp2="He is {1} {0}"
a=temp.format(nam,sur)
b=temp2.format(nam,sur)
print(a) #He is Tanmai Kamat
print(b) #He is Kamat Tanmai

#Fstrings
c=f"He is {nam} {sur}"
print(c) #He is Tanmai Kamat