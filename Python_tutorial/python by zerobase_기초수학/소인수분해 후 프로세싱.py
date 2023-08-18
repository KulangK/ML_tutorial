# x라는 숫자에 y를 곱하면, z의 제곱이 됨. y에 해당하는 가장 작은 수는?
"""
e.g. 72라는 숫자에 y를 곱하면 z의 제곱
72 = 2 * 2 * 2 * 3 * 3 = z^2
   = 2^2 * 2 * 3^2
   2를 곱해주면 (2 * 2 * 3)^2 가 됨.
   즉 y는 2, z는 12
"""
userNum = int(input('1보다 큰 정수 입력: '))

n = 2
searchNumbers = []
while n <= userNum:
    if userNum % n == 0:                # 2가 가장 작은 소수이기에 2부터 시작하는 것
        print('소인수: {}'.format(n))
        if searchNumbers.count(n) == 0: # n값의 개수 확인, 없으면 추가
            searchNumbers.append(n)
        elif searchNumbers.count(n) == 1: # n값이 1이면 리스트에서 제거, (2개는 제곱되니까 타겟이 아님)
            searchNumbers.remove(n)
        userNum /= n                    # 첫번째 시도에 2가 소인수일 경우, 나눠서 나머지를 이용해야함. 
    else:
        n += 1

print(f'searchNumbers: {searchNumbers}')