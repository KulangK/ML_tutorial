def geometric(x, y, z):

    valueN = 0
    sumN = 0
    i = 1

    while i <= z:
        if i == 1:
            valueN = x
            sumN = x
            print(f'{i}번째 항의 값: {valueN}')
            print(f'{i}번째 항까지의 합: {sumN}')
            i += 1
            continue

        valueN *= y
        sumN += valueN
        print(f'{i}번째 항의 값: {valueN}')
        print(f'{i}번째 항까지의 합: {sumN}')
        i += 1

userInput = int(input('a1 입력: '))
geome = int(input('공비 입력: '))
end = int(input('n 입력: '))

geometric(userInput, geome, end)
