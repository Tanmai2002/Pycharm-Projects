import random
import time
#97-122 lower case
#65-90 upper case
def checkAns(stri):
    print(stri)
    inpu = input()

    if inpu.__eq__(str(stri)):

        return True
    else:

        print('Error : Try again')
        return checkAns(stri)


if __name__ == '__main__':
    t=time.time()
    Errors=0
    l=[]
    for i in range(32,123):
         l.append(chr(i))
    l.remove(' ')
    for i in range(10):
        r=''
        for i in range(random.randint(1,9)):
            r+=str(random.choice(l))
        checkAns(r)
    t=(time.time()-t)/60
    print(f'Hurrah :Exercise complete :{t}')


