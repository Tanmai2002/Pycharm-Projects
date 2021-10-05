l = 10


def test1():
    l = 5
    print(l)  # 5


def test2():
    print(l)  # 10


def test3():
    try:
        l = l + 10
        print(l)  # local variable 'l' referenced before assignment
    except Exception as e:
        print(e)


def test4():
    global l
    l = l + 10
    print(l)  # 20


test1()
test2()
test3()
test4()
