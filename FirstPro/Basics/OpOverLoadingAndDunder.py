class A:
    def __init__(self,name,game):
        self.name=name;
        self.game=game;
    def __add__(self, other):
        return f"{self.name} + {other.name}"
    def __repr__(self):# used to represent how to declare the class
        return f"A('{self.name}','{self.game}')"
    def __str__(self):
        return f"{self.name} plays {self.game}"

a=A("tanu","coc")
b=A("anu","cr")
print(a+b) #tanu + anu
print(a) #tanu plays coc : if str wont exist , it wld have print repr
print(repr(a)) #A('tanu','coc')