# x, y의 최대 공약수는 y, r(x%y)의 최대 공약수와 같다.

num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

temp1 = num1; temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp

print(f'{num1}, {num2}의 최대 공약수: {temp1}')

for i in range(1, temp1 + 1):
    if temp1 % i == 0:
        print('{}, {}의 공약수: {}'.format(num1, num2, i))