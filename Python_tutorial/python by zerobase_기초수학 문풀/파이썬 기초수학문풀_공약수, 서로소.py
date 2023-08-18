import random as rd

x = rd.randint(100, 1000)                       # 비교할 두 개의 난수 발생
y = rd.randint(100, 1000)

print(f'발생한 두 난수: x = {x}, y = {y}')

x_div = []                          # x의 약수 그룹
y_div = []                          # y의 약수 그룹
common_div = []                     # 공약수 그룹

for i in range(1, x + 1):           # x의 약수
    if x % i == 0:
        x_div.append(i)

for i in range(1, y + 1):           # y의 약수
    if y % i == 0:
        y_div.append(i)

print(f'{x}의 약수: {list(x_div)}')
print(f'{y}의 약수: {list(y_div)}')

for i, num in enumerate(x_div):     # x, y의 공약수
    if y % x_div[i] == 0:
        common_div.append(x_div[i])
    
print(f'{x}와 {y}의 공약수: {list(common_div)}')
print(f'{x}와 {y}의 최대공약수: {common_div[-1]}')

if len(common_div) == 1:            # 1은 항상 공약수로 포함됨, 1만 공약수로 존재한다면, 1개 뿐이겠지.
    print(f'{x}와 {y}는 서로소입니다.')
else:
    print(f'{x}와 {y}는 서로소가 아닙니다.')
