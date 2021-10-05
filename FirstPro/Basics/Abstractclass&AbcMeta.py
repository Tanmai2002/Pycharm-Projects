from abc import ABC,abstractmethod
#used to predefine a sturcture for inheritated class
#u cant make objects of Abstract class
class Shape(ABC):#or Shape(metaclass=ABCMeta);note to import ABCMeta instead of ABC
    @abstractmethod
    def Area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.l=10
        self.b=20
    def Area(self):
        return self.l*self.b

class Sqaure(Shape):
    def __init__(self):
        self.l=1

try:
    s=Sqaure()
except Exception as e:
    print("Error: ",e ) #Error:  Can't instantiate abstract class Sqaure with abstract methods Area
r=Rectangle()
print(r.Area()) #200
