# 정수 두 개를 입력하면 곱셈, 나눗셈 연산 결과를 출력하는 함수를 만들고 호출

def calFun():
    n1 = int(input('첫 번째 정수 입력: '))
    n2 = int(input('두 번째 정수 입력: '))
    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {round(n1 / n2, 2)}')

calFun()

# round(n1 / n2, 2)를 사용하면 반올림 및 소수 2번째 자리까지 표현