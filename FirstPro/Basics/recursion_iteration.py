def fact_iter(n):
    f=1
    for i in range(n):
        f=f*(n+1)
    return f
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(5))