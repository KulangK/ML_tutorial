import time

class withdrawException(Exception):
    def __init__(self):
        super().__init__(f'출금액은 잔액을 넘을 수 없습니다.')

def deposit(acBalan, acBook):
    lt = time.localtime()
    depo = int(input('입금액 입력: '))
    depoType = input('입금 내역 입력: ')
    timeStr = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)

    with open(acBalan, 'r') as f:
        m = f.read()

    with open(acBalan, 'w') as f:
        f.write(str(int(m) + depo))

    with open(acBook, 'a') as f:
        f.write('-'*40)
        f.write('\n')
        f.write(f'[{timeStr}]\n')
        f.write(f'[입금] {depoType} : {depo}원\n')
        f.write(f'[잔액] {str(int(m) + depo)}원\n')
        print('입금 완료!!')
        print(f'기존 잔액 : {m}원')
        print(f'입금 후 잔액 : {str(int(m) + depo)}원')

def withd(acBalan, acBook):
    lt = time.localtime()
    depo = int(input('출금액 입력: '))
    depoType = input('출금 내역 입력: ')
    timeStr = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)

    with open(acBalan, 'r') as f:
        m = f.read()
        if depo > int(m):
            raise withdrawException()

    with open(acBalan, 'w') as f:
        f.write(str(int(m) - depo))

    with open(acBook, 'a') as f:
        f.write('-'*40)
        f.write('\n')
        f.write(f'[{timeStr}]\n')
        f.write(f'[출금] {depoType} : {depo}원\n')
        f.write(f'[잔액] {str(int(m) - depo)}원\n')
        print('출금 완료!!')
        print(f'기존 잔액 : {m}원')
        print(f'출금 후 잔액 : {str(int(m) - depo)}원')

