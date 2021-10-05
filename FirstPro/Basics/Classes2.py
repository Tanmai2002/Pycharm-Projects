class Players:
    NoOfPlayers=12
    def __init__(self,PlayerName):
        self.name=PlayerName
    def printDetails(self):
        return f"Name is {self.name}"


tanu=Players("Tanmai")
print(tanu.printDetails())
#print(Players.printDetails())  #returns error

class p2:
    test=1010
    @staticmethod
    def addno(i1,i2):
        return i1+i2

    @classmethod
    def changeTest(cls,t):
        cls.test=t

    _itsProtec=10 #Declaring protected var
    __itsprivate=1000 #declaring Private var

t1=p2()
print(p2.addno(10,11)) #21

print(t1.addno(10,11)) #21
print( t1.test)
t1.changeTest(50) #1010
print( t1.test) #50
print(p2.test) #50
print(t1._itsProtec) #10
#print(t1.__itsprivate) Throws error
print(t1._p2__itsprivate) #1000

