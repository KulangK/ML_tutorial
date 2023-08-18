# 군수열도 마찬가지로 우리가 입력하는 값의 규칙을 찾아내는 것이 아니라,
# 프로그램을 만드는 사람이 규칙을 찾고 그에 맞게 프로그램을 짜는 것임.

# e.g. 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5...

userInput = int(input('n 항 입력: '))

flag = True
n = 1; nCnt = 1; searchN = 0
while flag:

    for i in range(1, n + 1):
        if i == n:
            print('{} '.format(i), end= '')
        else:                                  # 군의 끝 숫자 도달하기까지의 숫자 표현
            print('{} '.format(i), end= '')    # 없으면 마지막 숫자만 출력하게 됨.

        nCnt += 1                              # 각 숫자별 카운팅으로 userInput 도달하도록 유도
        if (nCnt > userInput):
            searchN = i                        # 숫자 도달시 원하는 숫자가 userInput에 멈추도록 설계
            flag = False
            break
    print()
    n += 1

print('{}항: {}'.format(userInput, searchN))