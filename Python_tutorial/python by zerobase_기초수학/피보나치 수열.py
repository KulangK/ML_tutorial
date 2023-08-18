# 세번째 항은 첫번째 항과 두번째 항의 합
# an = a(n-1) + a(n-2)
# 프로그래밍에서는 어차피 a1과 a2는 1일 것임을 알기에 이를 따로 이용

userInput = int(input('n 입력: '))

valueN = 0
sumN = 0

valuePreN2 = 0
valuePreN1 = 0

n = 1

while n <= userInput:
    if n == 1 or n == 2:
        valueN = 1
        valuePreN1 = valueN
        valuePreN2 = valueN

        sumN += valueN
        n += 1

    else:
        valueN = valuePreN1 + valuePreN2
        valuePreN2 = valuePreN1
        valuePreN1 = valueN
        sumN += valueN
        n += 1

print('{}번째 항의 값: {}'.format(userInput, valueN))
print('{}번째 항까지의 합: {}'.format(userInput, sumN))
