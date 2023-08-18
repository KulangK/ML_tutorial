uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/primenumbers.txt'

num = int(input('0보다 큰 정수 입력: '))
nums = []
primeUse = []

for i in range(2, num+1):
    for j in range(1, i+1):
        if i % j == 0:
            primeUse.append(j)
    if len(primeUse) == 2:
        nums.append(i)
    primeUse = []

with open(uri, 'a') as f:
    f.write(f'{num}의 소수: {nums}\n')

print('primeNum write complete!')