def dec1(fun):
    def in1():
        print("hii")
        fun()
        print("end")
    return in1
@dec1
def f1():
    print("My name is Tanmai")

def f2():
    print("My name is f2")

f1()

f3=dec1(f2)
f3()#adding parenthese runs the program else it will be just an argument

