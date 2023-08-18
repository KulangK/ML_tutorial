uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/divisor.txt'

num = int(input('0보다 큰 정수 입력: '))
nums = []

for i in range(1, num+1):
    if num % i == 0:
        nums.append(i)

with open(uri, 'a') as f:
    f.write(f'{num}의 약수: {nums}\n')

print('divisor write complete!')