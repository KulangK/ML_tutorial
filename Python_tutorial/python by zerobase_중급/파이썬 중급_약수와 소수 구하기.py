userInput1 = int(input('약수를 구하고자 하는 수: '))
userInput2 = int(input('해당 숫자까지의 소수: '))

div = []
prime = []
primeUse = []

for i in range(1, userInput1+1):
    if userInput1 % i == 0:
        div.append(i)

for i in range(2, userInput2+1):
    for j in range(1, i+1):
        if i % j == 0:
            primeUse.append(j)
            print(primeUse)
    if len(primeUse) == 2:
        prime.append(i)
    primeUse = []

print('{}의 약수 : {}'.format(userInput1, div))
print('{}까지의 소수 : {}'.format(userInput2, prime))