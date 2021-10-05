l=[i for i in range(10) if i%3==0]
print(l)
dict={i:f"Item{i}" for i in range(10)}
print(dict)
sqaures={i:i*i for i in range(10) if i%2==0}
print(sqaures)

a={i for i in [1,100,1,100,123,1262]}
print(a) #{1, 123, 100, 1262} #this is a set
print(type(a)) #<class 'set'>

b=(i for i in range(10) if i%2==0)
print(type(b))#<class 'generator'>
print(b) #<generator object <genexpr> at 0x01778568>