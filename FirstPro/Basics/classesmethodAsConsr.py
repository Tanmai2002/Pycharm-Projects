
class Players:
    NoOfPlayers=12
    def __init__(self,PlayerName,salary,position):
        self.name=PlayerName
        self.salary=salary
        self.position=position
    def printDetails(self):
        return f"Name is {self.name}"

    @classmethod
    def makeNewInstuctor(cls,name):
        return cls(name,4500,"Instructor")
    @staticmethod
    def addno(i1,i2):
        print( i1+i2)
if __name__ == '__main__':


    tanu=Players("Tanmai",2000,"player")
    anu=Players.makeNewInstuctor("anu")
    print(tanu.__dict__)
    print(anu.__dict__)
    Players.addno(1,3) #4