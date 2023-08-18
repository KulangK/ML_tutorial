def facto(n):

    if n == 1:
        return n

    return n * facto(n-1)


userInput = int(input('숫자 입력: '))

print(format(facto(userInput), ','))