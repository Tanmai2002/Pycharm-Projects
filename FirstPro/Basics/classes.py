class Employee:
    n=1
    pass

tanu=Employee()
anu=Employee()
tanu.name="Tanmai"
anu.name="Anu"
tanu.std=12
print(anu.__dict__) #{'name': 'Anu'}
print(tanu.__dict__) #{'name': 'Tanmai', 'std': 12}
print(Employee.n) #1
print(tanu.n,":",tanu.name) #1 : Tanmai

Employee.n=100
tanu.n=500
print(Employee.n) #100
print(tanu.n,":",tanu.name) #500 : Tanmai
print(tanu.__dict__) #{'name': 'Tanmai', 'std': 12, 'n': 500}
# this shows that we cannot override any instances of class instead it creates instance of its own when trying to override

