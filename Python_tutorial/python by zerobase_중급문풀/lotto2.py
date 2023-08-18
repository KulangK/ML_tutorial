import random

userNums = []; randNums = []; collNums = []
randBonuNum = 0

def setUserNums(ns):
        global userNums
        userNums = ns

def getUserNums():
        return userNums

def setRandNums():
        global randNums
        randNums = random.sample(range(1, 46), 6)

def getRandNums():
        return randNums

def setBonuNum():
        global randBonuNum

        while 1:
                randBonuNum = random.randint(1, 45)
                if randBonuNum not in randNums:
                        break

def getBonuNum():
        return randBonuNum

def lottoResult():
        global userNums
        global randNums
        global collNums

        collNums = []
        for un in userNums:
                if un in randNums:
                        collNums.append(un)

        if len(collNums) == 6:
                print('1등 당첨')
                print(f'번호: {collNums}')
        elif len(collNums) == 5 and randBonuNum in userNums:
                print('2등 당첨')
                print(f'번호: {collNums}, 보너스 번호: {randBonuNum}')
        elif len(collNums) == 5:
                print('3등 당첨')
                print(f'번호: {collNums}')
        else:
                print('아쉽습니다. 다음 기회에~')
                print(f'기계 번호: {randNums}')
                print(f'보너스 번호: {randBonuNum}')
                print(f'선택 번호: {userNums}')
                print(f'일치 번호: {collNums}')


def startLotto():
        n1 = int(input('번호(1~45) 입력: '))
        n2 = int(input('번호(1~45) 입력: '))
        n3 = int(input('번호(1~45) 입력: '))
        n4 = int(input('번호(1~45) 입력: '))
        n5 = int(input('번호(1~45) 입력: '))
        n6 = int(input('번호(1~45) 입력: '))
        selecNums = [n1, n2, n3, n4, n5, n6]

        setUserNums(selecNums)
        setRandNums()
        setBonuNum()

        lottoResult()