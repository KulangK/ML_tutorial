def add(n1, n2):
    print('덧셈 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return                                          # 여기서 return하지 않으면 line 15 작동하면서 오류 발생

    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return                                          # 여기만 return하면 다 잡힐 줄 알았는데, 두 번째 피연산자가 숫자면
                                                        # 그냥 넘어가버리게 되므로, 첫 번째 오류를 못잡아냄.

    print(f'{num1} + {num2} = {num1 + num2}')


def sub(n1, n2):
    print('뺄셈 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{num1} - {num2} = {num1 - num2}')

def mul(n1, n2):
    print('곱셈 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{num1} * {num2} = {num1 * num2}')

def div(n1, n2):
    print('나눗셈 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num = num1 / num2
    except:
        print('0으로 나눌 수 없습니다.')
        return
    print(f'{num1} / {num2} = {num}')

def mod(n1, n2):
    print('나머지 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num = num1 % num2
    except:
        print('0으로 나눌 수 없습니다.')
        return
    print(f'{num1} % {num2} = {num}')

def flo(n1, n2):
    print('몫 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num = num1 // num2
    except:
        print('0으로 나눌 수 없습니다.')
        return
    print(f'{num1} // {num2} = {num}')

def exp(n1, n2):
    print('거듭제곱 연산')
    try:
        num1 = float(n1)
    except:
        print('첫 번째 피연산자는 숫자가 아닙니다.')
        return
    try:
        num2 = float(n2)
    except:
        print('두 번째 피연산자는 숫자가 아닙니다.')
        return

    print(f'{num1} ** {num2} = {num1 ** num2}')
