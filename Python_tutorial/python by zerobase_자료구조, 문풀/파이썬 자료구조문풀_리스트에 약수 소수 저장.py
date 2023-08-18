userInput = int(input('1보다 큰 정수 입력: '))

div = []
prime = []

for i in range(1, userInput + 1):
    if userInput % i == 0:
        div.append(i)

for i in range(2, userInput):
    flag = True
    for f in range(2, i):
        if i % f == 0:
            flag = False
            break
    if flag:
        prime.append(i)

print(f'{userInput}의 약수: {div}')
print(f'{userInput}이하 소수: {prime}')
