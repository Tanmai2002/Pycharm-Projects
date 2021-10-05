from functools import  lru_cache
import time

@lru_cache(maxsize=2) # stores x latest results equal to maxsixe , thus takes no time to return the value and saves processing time
def some_work(n):
    #do some work
    time.sleep(n)
    return  n

"""@lru_cache(maxsize=int(input())) # cn be used to take input from user to store last x values
"""
if __name__ == '__main__':
    print("Calling first time")
    some_work(3) # takes time
    print("Calling second time")
    some_work(2)# takes time
    print("Calling third time")
    some_work(3)  # dont takes time
    print("Calling fourth time")
    some_work(4)  # takes time
    print("Calling fifth time")
    some_work(2)  # takes time