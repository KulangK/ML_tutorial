import random as rd

def lottoCom(x):
        n = 0
        count = 0
        lottoGen = []
        sameNum = []
        for i in range(7):
                n = rd.randint(1, 45)
                lottoGen.append(n)
        for i in range(7):
                for j in range (i):
                        if x[j] == lottoGen[i]:
                                sameNum.append(x[j])
                                count += 1

        if count == 6:
                print('1등 당첨입니다.')
        elif count == 5:
                print('2등 당첨입니다.')
        elif count == 4:
                print('3등 당첨입니다.')
        else:
                print('아쉽습니다. 다음 기회에~')
        print(f'기계 번호: {lottoGen[0:5]}')
        print(f'보너스 번호: {lottoGen[6]}')
        print(f'선택 번호: {x}')
        print(f'일치 번호: {sameNum}')