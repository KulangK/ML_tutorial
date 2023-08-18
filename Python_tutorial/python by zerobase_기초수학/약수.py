userNum = int(input('0보다 큰 정수 입력: '))

for i in range(1, userNum +1):
    if userNum % i == 0:                    # 나머지가 0인 i가 userNum의 약수인 것.
        print(f'{userNum}의 약수: {i}')