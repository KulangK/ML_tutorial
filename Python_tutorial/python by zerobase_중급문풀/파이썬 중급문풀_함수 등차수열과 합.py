def arithmetic(x, y, z):
    n = 0
    for i in range(z):
        print(f'{i + 1}번째 항의 값: {x + i*y}')
        n += x + i*y
        print(f'{i + 1}번째 항까지의 합: {n}')

userInput = int(input('a1 입력: '))
arith = int(input('공차 입력: '))
end = int(input('n 입력: '))

arithmetic(userInput, arith, end)
