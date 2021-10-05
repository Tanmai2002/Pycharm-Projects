#Print statements
print('hi') #hi
print("Hello") #Hello
print("ok",
      "will meet You",
      "Tanu") #ok will meet You Tanu


# Declaring Variables
x=10
y:str ="Magic"
#Basic operations
"""

"""
print(2+3) #5
print(2.0+3) #5.0
print(2-3) #-1
print(2/3) #0.66666666
print(2//3) # 0
print(2%3) #2
print(2*3) #6
print(2**3) #8
print("Dazzling"+"Ace") #DazzlingAce
print('hi'*5) #hihihihihi

#Try Except
try:
    print('hi'+3)
#This is TypeError
except Exception as e:
    print(e) # can only concatenate str (not "int") to str


#Taking Inputs:
i1=input()
i2=input("Enter a Value :")
"""
These are in string format
We neet to typecast these  to use them as different types
"""
x1=int(i2)
print("Square of the Number is :" ,
      x1*x1)
#Lists Dictionaries Sets Tuples

l=["Tanu","Anu",100 ,200]

d={"Student":"Tanu","Teacher":"Anu" }

s={1,51,33,33,51}
print(s) #{1, 51, 33}

T=(12,56,"Dazz")

#fstrings

x="Tanu"
print(f"My Name is {x}")


#if_else Loops
i=100
if 1>i:
    print("smaller than 1")
elif 1<i:
    print("Greater than 1")
else:
    print("Equal to 1")

x=100 if i>100 else 20
#For-While loop
l=["Tanu","Anu",100 ,200]
for item in l:
    print(item)

for i in range(10):
    print(i)

k=1
while k<100:
    print(k)
    k=k+1

#functions
def f1():
    print("Hii")
    #This function returns 'None'

def square(number):
    return number*number

#Recursion
def fact(n):
    if n<0:
        return None
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

#Baic func and ways to initialize lists
l=[i for i in range(10)]
l2=l[::2]
print(l2)


