def nextPalidrome(i):
    while True:
        i=i+1
        if str(i).__eq__(str(i)[::-1]):
            return i
while True:
    n=nextPalidrome(int(input("Enter a Number :")))
    print(n)