# 구구단 출력 함수 연쇄 호출되도록 함수 선언

def gudan2():
    for i in range(1, 10):
        print(f'2 * {i} = {2*i}')
    print()
    gudan3()

def gudan3():
    for i in range(1, 10):
        print(f'3 * {i} = {3*i}')
    print()
    gudan4()

def gudan4():
    for i in range(1, 10):
        print(f'4 * {i} = {4*i}')
    print()
    gudan5()

def gudan5():
    for i in range(1, 10):
        print(f'5 * {i} = {5*i}')
    print()
    gudan6()

def gudan6():
    for i in range(1, 10):
        print(f'6 * {i} = {6*i}')
    print()
    gudan7()

def gudan7():
    for i in range(1, 10):
        print(f'7 * {i} = {7*i}')
    print()
    gudan8()

def gudan8():
    for i in range(1, 10):
        print(f'8 * {i} = {8*i}')
    print()
    gudan9()

def gudan9():
    for i in range(1, 10):
        print(f'9 * {i} = {9*i}')

gudan2()