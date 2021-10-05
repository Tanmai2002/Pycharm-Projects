def f1(a1):
    print("This is f1", a1, end="\n\n")


def f2(a1, *arg1):  # note order, normal values can only be taken first,(*arg,a1) is invalid
    print("This is f2", a1, end="\n\n")
    for i in arg1:
        print(i)


def f3(a1, a2, *xyz, **Kwarg1):  # Note order (normal,args,kwargs)
    print("This is f3", a1,a2, end="\n\n")
    for i in xyz:
        print(i)
    for key, values in Kwarg1.items():
        print(f"{key} is {values}")


f1("hii")  # This is f1

f2(1, 2, 3, 35)
"""
This is f2 1

2
3
35
"""

t1 = ["hi", 551, 554]
f2(100, *t1)  # note the str
""""
This is f2 100

hi
551
554
"""
d1 = {"tanm": "50", "zee": "tee"}
f3(10, 100, *t1, **d1)
