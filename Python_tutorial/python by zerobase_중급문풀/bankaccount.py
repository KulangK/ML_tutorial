import random as rd

class TransactionException(Exception):
    def __init__(self, a, b):
        super().__init__(f'잔고부족!, 잔액: {a}, 출금액: {b}')

class account():
    def __init__(self):
        aName = input('통장 개설을 위한 예금주 입력: ')
        self.aName = aName
        self.aAccount = str(rd.randint(0, 99999)).zfill(5)
        self.aBalan = 0
        self.printAccountInfo()
        self.transaction()

    def printAccountInfo(self):
        print('-'*30)
        print(f'account_name: {self.aName}')
        print(f'account_no: {self.aAccount}')
        print(f'totalMoney: {self.aBalan}')
        print('-'*30)

    def transaction(self):
        while 1:
            x = int(input((f'1.입금, 2.출금, 3.종료:  ')))
            if x == 1:
                self.deposit()
                self.printAccountInfo()
            elif x == 2:
                try:
                    self.withdrawl()
                except TransactionException as e:
                    print(e)
                finally:
                    self.printAccountInfo()
            elif x == 3:
                print('Bye~')
                break

    def deposit(self):
        self.aBalan += int(input(f'입금액 입력: '))

    def withdrawl(self):
        withd = int(input(f'출금액 입력: '))
        if self.aBalan < withd:
            raise TransactionException(self.aBalan, withd)
        self.aBalan -= withd

