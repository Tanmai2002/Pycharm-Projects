# used with lists ,returns index with val
l1=["Tanmai","kiran","niki","ash"]
l2=enumerate(l1)
print((l2)) #<class 'enumerate'>

for i,names in l2:# u can use enumaterate(l1) directly here
    print(f"{i} is {names}")
"""
0 is Tanmai
1 is kiran
2 is niki
3 is ash
"""