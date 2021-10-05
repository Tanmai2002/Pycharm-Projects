import random
import time


def printScore(Player, p1, p2):
    state = f"{Player}\t :{p1} \t Computer\t :{p2}"
    print(state)


def Duel():
  try:
    list1 = ["Gun", "Snake", "Water"]

    pt = input("Enter Your Choice:\n S for Snake \n G for Gun \n W for Water \n :")
    p = pt.capitalize()
    c:str = random.choice(list1)

    dict1 = {"G": {"G": 1, "S": 2, "W": 0}, "S": {"G": 0, "S": 1, "W": 2}, "W": {"G": 2, "S": 0, "W": 1}}
    t = dict1.get(p).get(c.__getitem__(0))

    s1 = "Its a Draw!!"
    if t==2:
        s1 = "You Won !!"
    elif t==0:
        s1 = "You Lose"
    print(f"\n Computer selected :{c}\n",s1,"\n")
    return t
  except:
      print("Error,Wrong Value Entered\n")
      Duel()


isExit = False

name = input("Enter Your name :")

print("Lets Start The Game \n ")
i = 0
while not isExit:
    p1 = 0
    p2 = 0
    for i in range(10):
        printScore(name, p1, p2)
        res = Duel()
        if res == 0:
            p2 = p2 + 1
        elif res == 2:
            p1 = p1 + 1
        time.sleep(2)
    s = "Its a Draw!!"
    if p1 > p2:
        s = "You Won !!"
    elif p1 < p2:
        s = "You Lost"
    print(f"\nFinal Score: \n {name} :{p1} \n Computer :{p2} \n\n {s} \n")
    play = input("Wana Play Again? :y for Yes, N for No\n :")
    p = play.capitalize()
    isExit = True
    if p=="Y":
        isExit=False
