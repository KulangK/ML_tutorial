import random as rd

x = rd.randint(100, 1000)

print('100부터 1000사이의 난수: {}'.format(x))

prime_div = []

n = 2
while n <= x:                                           # 소인수 분해
    if x % n == 0:
        print('소인수: {}'.format(n))
        x /= n
        prime_div.append(n)
    else:
        n += 1

print(list(prime_div))

for i, num in enumerate(prime_div):
    if prime_div[i] == prime_div[i-1]:                  # 중복되는 숫자가 다시 출력되지 않도록
        continue
    else:
        print(f'{num}의 지수: {prime_div.count(num)}')