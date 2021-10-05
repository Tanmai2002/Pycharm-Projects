from pygame import mixer
import time


def playSound(sound, code):
    print(f"\n Enter {code} when done")
    mixer.init()
    mixer.music.load(sound)
    mixer.music.play(100000)
    c = input("Enter the code plz :")
    if (c.__eq__(code)):
        mixer.music.stop()
        printInLog(code)

    else:
        playSound(sound, code)


def printInLog(didWhat):
    c = ["Drank", "ExDone", "EyDone"]
    d=["Drank water", "Physical Exercise done","Eyes Exercise Done"]
    fil=list(filter(lambda x:x==didWhat,c))
    did=d[c.index(fil[0])]
    with open("HealthyPro.txt", "a") as f:
        str = f"{time.asctime(time.localtime(time.time()))}\t {did}\n"
        f.write(str)


def getLog():
    with open("HealthyPro.txt", "r")as f:
        for line in f.readlines():
            print(line, end="")

wtime = time.time()
etime = time.time()
ptime = time.time()
checkTimers=[wtime,ptime,etime]
val = time.localtime(time.time()).tm_hour > 9 and time.localtime(time.time()).tm_hour < 20
isDrinkingTime = False
isExTime = False
isEyesTime = False
while val:
    isDrinkingTime = ((time.time() - checkTimers[0]) / 60) > 20
    isExTime = (time.time() - checkTimers[1]) / 60 > 45
    isEyesTime = (time.time() - checkTimers[2]) / 60 > 30

    tValues = [isDrinkingTime, isExTime, isEyesTime]
    sound = ["water.mp3", "phyExer.mp3", "eyesExer.mp3"]
    codes = ["Drank", "ExDone", "EyDone"]
    t1=list(map(lambda tv, s, cod: playSound(s, cod) if tv else None, tValues, sound, codes))
    checkTimers=list(map(lambda tv,timers:time.time()if tv else timers,tValues,checkTimers))
    val = time.localtime(time.time()).tm_hour > 9 and time.localtime(time.time()).tm_hour < 20




# printInLog("Start")
