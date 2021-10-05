# OOP - object oriented programming
class Animal:
    nose = 1
    eyes = 2

    def __init__(self,Name):
        self.AnimalName=Name
        self.setSound(input("What sound does it makes :"))


    def setSound(self, sound):
        self.animalSound=sound

    def Sound(self):
        return self.animalSound

class Dog(Animal):

    def __init__(self):
        super().__init__("Dog")

    def SetNameOfDog(self,Name):
        self.NameOfDog=Name



#Declaring class obj

a=Animal("Cat")

