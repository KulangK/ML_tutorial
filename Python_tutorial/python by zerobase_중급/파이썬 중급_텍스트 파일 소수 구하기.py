def writePrimeNumber(n):
    file = open('C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급/test3.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNum = int(input('0보다 큰 정수 입력: '))

for i in range(2, (inputNum + 1)):
    flag = True
    for n in range(2, i):
        if i % n == 0:
            flag = False
            break

    if flag:
        print(i)
        writePrimeNumber(i)
