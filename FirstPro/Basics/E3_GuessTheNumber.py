import random

n = random.randint(0,100)
print("Total Chances:9")
i = 0
while (i < 9):
    print("\nChances left:", (9 - i))
    t1 = int(input("Guess the Number :"))
    if (t1 > n):
        print("Number is too big")
    elif (t1 < n):
        print("Number is too small")
    elif (t1 == n):
        break;
    i = i + 1
if (i < 9):
    print("You Won")
    print("You Completed in ",i+1,"guesses!!!")
else:
    print("Game Over")
