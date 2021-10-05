with open("FileName or Path") as f:
    print(f.read())

with open("FileName or Path",'w') as f:
    f.write("Xyz")

with open("FileName or Path",'a') as f:
    f.write("wxudjk")

with open("FileName or Path",'r+') as f:
    print(f.read())
f=open("FileName or Path",'a')

f.write("Hello")
f.close()# Very imp
#Import

import datetime
import pandas


#pip install pandas


#Main
if __name__ == '__main__':
    print("hello")