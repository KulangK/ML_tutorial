# 함수를 이용한 산술연산 계산기

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def mod(x, y):
    return x % y

def flodiv(x, y):
    return x // y

def exponen(x, y):
    return x ** y

while 1:
    sign = ''
    result = ''
    print('-'*30)
    op = int(input('1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, 5.나머지, 6. 몫, 7. 제곱승, 8. 종료\t:\t'))
    if op == 8:
        print('종료되었습니다.')
        break
    else:
        num1 = float(input('첫 번째 숫자 입력: '))
        num2 = float(input('두 번째 숫자 입력: '))
        if op == 1:
            result = add(num1, num2)
            sign = '+'
        if op == 2:
            result = sub(num1, num2)
            sign = '-'
        if op == 3:
            result = mul(num1, num2)
            sign = '*'
        if op == 4:
            result = div(num1, num2)
            sign = '/'
        if op == 5:
            result = mod(num1, num2)
            sign = '%'
        if op == 6:
            result = flodiv(num1, num2)
            sign = '//'
        if op == 7:
            result = exponen(num1, num2)
            sign = '**'

    print(f'{num1} \t {sign} \t {num2} \t = \t {result}')
    print('-'*30)