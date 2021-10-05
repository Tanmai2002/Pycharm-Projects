class person:
    def __init__(self, Name,SurName):
        self.name=Name
        self.sname=SurName

    @property #this make the method as class instance rather than funcion
    def email(self):
        return f"{self.name}.{self.sname}@gmail.com"

    @email.setter # used when we want to change/declare fun with property decorater
    def email(self,other):
        l1=str.split(other,"@")
        l2=str.split(l1[0],".")
        self.name = l2[0]
        self.sname = l2[1]

tanu=person("Tanmai","Kamat")
print(tanu.email) #Tanmai.Kamat@gmail.com
tanu.email="Tanu.salvi@gmail.com"
print(tanu.email) #Tanu.salvi@gmail.com
print(tanu.name) #Tanu
print(tanu.sname) #salvi