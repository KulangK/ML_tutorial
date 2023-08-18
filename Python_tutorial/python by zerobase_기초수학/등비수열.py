# 연속된 두 항의 비가 일정한 수열
# 일반항: an = a1 * r^(n-1)
# 등비 중항: a(n-1) * a(n+1) = an^2
# 등비 수열의 합: Sn = a1 * (1-r^n)/1-r

inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0

n = 1
while n <= inputN:

    if n == 1:
        valueN = inputN1
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue

    valueN *= inputR
    print('{}번째 항의 값: {}'.format(n, valueN))
    n += 1


