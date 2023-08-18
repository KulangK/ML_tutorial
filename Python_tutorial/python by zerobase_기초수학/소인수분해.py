userNum = int(input('1보다 큰 정수 입력: '))

n = 2
while n <= userNum:
    if userNum % n == 0:                # 2가 가장 작은 소수이기에 2부터 시작하는 것
        print('소인수: {}'.format(n))
        userNum /= n                    # 첫번째 시도에 2가 소인수일 경우, 나눠서 나머지를 이용해야함. 
    else:
        n += 1
