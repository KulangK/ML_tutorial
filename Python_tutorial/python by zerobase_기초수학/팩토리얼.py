# 팩토리얼 = 해당 숫자까지의 모든 정수를 곱한 결과
# 0! = 1

userInput = int(input('정수 입력: '))

answer = 1

while 1:
    if userInput == 1 or userInput == 0:
       answer = 1
    else:
        for i in range(1, userInput +1):
            answer *= i
            print(answer)
    break

print('입력한 정수의 팩토리얼: {}'.format(answer))

# 위는 반복문을 이용한 경우, for문도 이용할 수 있음

""" 재귀함수를 이용한 경우
def factorial(n):
    if n == 1: return 1
    
    return n * factorial(n - 1)

print('{} 팩토리얼: {}'.format(userInput, factorial(userInput))
"""