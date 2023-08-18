import random as rd

x = rd.randint(100, 1000)                       # 비교할 두 개의 난수 발생
y = rd.randint(100, 1000)

maxDiv = 0

print(f'발생한 두 난수: x = {x}, y = {y}')

for i in range(1, min(x, y)+1):             # 최대 공약수 찾기
    if x % i == 0 and y % i == 0:
        maxDiv = i
        
print(f'{x}와 {y}의 최대 공약수: {maxDiv}')

minMul = (x * y) // maxDiv                  # 유클리드 호제법을 통한 최소 공배수 찾기

print(f'{x}와 {y}의 최소 공배수: {minMul}')
