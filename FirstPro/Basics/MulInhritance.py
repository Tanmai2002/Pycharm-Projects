class class1:
    var=2
    pass
class class2:
    var=3
    pass
class class3(class1,class2):
    pass

tan=class3()
print(tan.var) #2 : this is becoz class1 is firsst inheritated
# python checks cuurnt class then first class then second n so on for any methods or variables
