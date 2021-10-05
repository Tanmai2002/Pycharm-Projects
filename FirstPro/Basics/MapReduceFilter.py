# MAP Function : used to assign all the elements of any list a function
l1 = ["1", "2", "3","4"]
l1 = list(map(int, l1))  # coverts all elements to int
print(l1)



l2 = list(map(lambda x: x * x, l1))
print(l2)


def addTwo(i):
    return i + 2
l3 = list(map(addTwo, l1))
print(l3)


l4=list(map(lambda x,y:x+y,l1,l1))
print(l4)

#FILTER : used to filter out using functions

l1=[1,"2","tanu",50,27,324,4]
l1=list(filter(lambda x:type(x) is int,l1))
print(l1) #[1, 50, 27, 324, 4]
#l2=list(filter(lambda x,y:x+y>10,l1,l1)) gives error
l2=list(filter(lambda x:x>10,l1))
print(l2)

#REDUCE: used to run on whole list n return a singl value
from functools import reduce
l1=[1,2,3,4,5,6,10,5]
l2=reduce(lambda x,y:x+y,l1)
print(l2) #21
l3=reduce(lambda x,y:x+1,l1)
print(l3) #6
#this shows reduce func operates on 1st elements, it reduces sequencially
l4=reduce(lambda  x,y:x if(x>y) else y,l1)
print(l4) #10