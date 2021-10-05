#generator _ used to generate value by iteration
def genfibo(n):
    t1=0
    t2=1
    if(n==1):
        yield t1
    if n>1:
        yield t1
        yield t2
    for i in range(n-2):
        t=t2
        t2=t1+t2
        t1=t
        yield t2

g=genfibo(10)

for k in g:
    print(k)