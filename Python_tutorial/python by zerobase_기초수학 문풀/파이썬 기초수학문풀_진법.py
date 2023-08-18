userInput = input('변환하고자 하는 수 입력: ')
beforeX = int(input('해당 숫자의 진수 입력(2, 8, 10, 16): '))

if beforeX == 10:
    print(f'{userInput}의 2진수 표현: {bin(int(userInput))}')
    print(f'{userInput}의 8진수 표현: {oct(int(userInput))}')
    print(f'{userInput}의 16진수 표현: {hex(int(userInput))}')

elif beforeX == 2:
    print(f'{userInput}의 8진수 표현: {oct(int(userInput, 2))}')
    print(f'{userInput}의 10진수 표현: {int(userInput, 2)}')
    print(f'{userInput}의 16진수 표현: {hex(int(userInput, 2))}')

elif beforeX == 8:
    print(f'{userInput}의 2진수 표현: {bin(int(userInput, 8))}')
    print(f'{userInput}의 10진수 표현: {int(userInput, 8)}')
    print(f'{userInput}의 16진수 표현: {hex(int(userInput, 8))}')

else:
    print(f'{userInput}의 2진수 표현: {bin(int(userInput, 16))}')
    print(f'{userInput}의 8진수 표현: {oct(int(userInput, 16))}')
    print(f'{userInput}의 10진수 표현: {int(userInput, 16)}')

