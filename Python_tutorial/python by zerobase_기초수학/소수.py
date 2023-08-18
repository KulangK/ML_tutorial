userNum = int(input('0보다 큰 정수 입력: '))

for i in range(2, userNum +1):          # 2부터 userNum까지 list를 만듦
    flag = True
    for j in range(2, i):               # 위 list에서 숫자를 하나씩 받아, 2부터 해당 숫자 전까지 나눠봄
        if i % j == 0:                  # 나눠 떨어지는 숫자가 존재시, 반복문 중단, flag = False
            flag = False
            break
    if flag:
        print(f'{i}: 소수')
    else:
        print(f'{i}: 합성수')
