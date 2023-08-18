import accountbook as ab

acBook = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/myaccountbook.txt'
acBalan = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/money.txt'

while True:                                                         # 사용한 방법: 잔고 txt 파일과 가계부 txt 파일 이용
                                                                    # money.txt 는 잔고이므로, 맨 처음 시작할때 0이 있어야함.
    selectNumber = int(input('1. 입금, 2. 출금, 3. 종료  '))

    if selectNumber == 1:
        ab.deposit(acBalan, acBook)

    elif selectNumber == 2:
        try:
            ab.withd(acBalan, acBook)
        except ab.withdrawException as e:
            print(e)

    elif selectNumber == 3:
        print('종료')
        break

