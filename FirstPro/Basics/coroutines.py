def search():
    #///////////////Part1////////////////
    import  time
    time.sleep(4)
    book="Hbdksjsbmnz.dknfaKJSB fjkb fcKABf jkeb fjabfksn lcnkcn.,xcnksn nsabhb trhia this is a abook"
    #///////////////End/////////////
    #//////////////Part2//////////
    while True:
        text=(yield)
        if text in book:
            print("Yes")
        else:
            print("no")

if __name__ == '__main__':
    find=search()
    print("Running Search")
    next(find) # runs find for 1st time , run part 1
    print("ready")
    find.send(input("Enter what u wana search"))# dont run part1
    find.send(input("Enter what u wana search"))# dont run part1
    find.send(input("Enter what u wana search"))# dont run part1
    find.close()#Closes coroutine
