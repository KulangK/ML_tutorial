# 소인수 = 약수(인수) 중에서 소수인 숫자
# 소인수 분해로 약수를 정확하고 쉽게 구할 수 있음

userNum = int(input('0보다 큰 정수 입력: '))
divisor = []
div_prime = []

for i in range(1, userNum +1):
    if userNum % i == 0:                    # 나머지가 0인 i가 userNum의 약수인 것.
        print(f'{userNum}의 약수: {i}')
        divisor.append(i)
print(f'{userNum}의 약수: {list(divisor)}')

for i in divisor:           # 약수 중에서 소수 골라내기
    flag = True
    for j in range(2, i):               
        if i % j == 0:                  
            flag = False
            break
    if flag:
        div_prime.append(i)
div_prime.pop(0)            # 항상 1이 포함되며, 첫번째 인덱스이기에 빼주는 것
print(f'{userNum}의 소인수: {list(div_prime)}')
