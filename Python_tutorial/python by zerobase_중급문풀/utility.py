# 공과금 = utilities

def formatter(x):
    return format(x, ',')                   # return을 하지 않으면, 값은 none이 됨.

def income():
    x = int(input('수입 입력: '))
    return x

def utilities():
    water = int(input('수도 요금 입력: '))
    elec = int(input('전기 요금 입력: '))
    gas = int(input('가스 요금 입력: '))

    util = water + elec + gas
    return util

def utilityPercen():
    money = income()

    utility = utilities()

    percen = (utility / money) * 100

    print(f'공과금: {formatter(utility)}원')
    print('공과금 비율: %.2f%%' %(percen))