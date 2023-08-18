import random as rd

x = rd.randint(100, 1000)       # 난수 발생
divisor = []        # 약수 리스트
prime = []          # 소수 리스트
prime_div = []      # 소인수 리스트

print('100부터 1000사이의 난수: {}'.format(x))

for i in range(1, x + 1):                           # 약수
    if x % i == 0:
        divisor.append(i)

print(f'{x}의 약수: {list(divisor)}')

for i in range(2, x + 1):                           # 소수
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(i)

print(f'{x}이하 소수: {list(prime)}')

for i, num in enumerate(prime):                     # 소인수 (약수 중에서 소수를 구하던, 소수 중에서 약수를 구하던)
    if x % prime[i] == 0:
        prime_div.append(num)

print(f'{x}이하 소인수: {list(prime_div)}')

