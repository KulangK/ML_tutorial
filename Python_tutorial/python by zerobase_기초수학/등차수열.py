# 등차수열: 연속된 두 항의 차이가 일정한 수열 (공차를 갖는 수열)

# 일반항: an = a1 + (n-1)*d
# a1 = 첫번째 항, n = 항 수, d = 공차

# 등차 중항: 연속된 세 항의 가운데 항
# an = (a(n-1) + a(n+1)) / 2

# 등차 수열의 합
# Sn = n(a1 + an)/2

inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
n = 1
while n <= inputN:
    if n == 1:
        valueN = inputN1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue

    valueN = valueN + inputD
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1

# 등차수열 공식 이용 >> valueN = inputN1 + (inputN - 1) * inputD