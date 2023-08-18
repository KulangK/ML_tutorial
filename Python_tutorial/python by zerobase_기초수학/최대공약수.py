userNum1 = int(input('첫번째 0보다 큰 정수 입력: '))
userNum2 = int(input('두번째 0보다 큰 정수 입력: '))
# userNum3 = int(input('세번째 0보다 큰 정수 입력: ')) >> 포함시 line 7에 조건 하나 추가

x = 0
for i in range(1, userNum1 +1):
    if userNum1 % i == 0 and userNum2 % i == 0:                    
        print(f'{userNum1}과 {userNum2}의 공약수: {i}')
        x = i

print(f'{userNum1}과 {userNum2}의 최대공약수: {x}')

# 소인수분해를 이용하면 최대공약수 및 공약수를 구할 수 있다.
# 소인수분해 후 공통 되는 수만 다 뽑으면 됨.
