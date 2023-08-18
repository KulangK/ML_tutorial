def ticketRecipt(infant, infantDis, child, childDis, adult, adultDis):
    infantPri = infant * 18000
    infantDisPri = infantDis * 18000 * 0.5
    childPri = child * 25000
    childDisPri = childDis * 25000 * 0.5
    adultPri = adult * 50000
    adultDisPri = adultDis * 50000 * 0.5
    totPeo = infant + infantDis + child + childDis + adult + adultDis
    totPri = infantPri + infantDisPri + childPri + childDisPri + adultPri + adultDisPri

    print('='*60)
    print('유아 {}명 요금: {}원'.format(infant, format(infantPri, ',')))
    print('유아 할인 대상 {}명 요금: {}원'.format(infant, format(int(infantDisPri), ',')))
    print('소아 {}명 요금: {}원'.format(infant, format(childPri, ',')))
    print('소아 할인 대상 {}명 요금: {}원'.format(infant, format(int(childDisPri), ',')))
    print('성인 {}명 요금: {}원'.format(infant, format(adultPri, ',')))
    print('성인 할인 대상 {}명 요금: {}원'.format(infant, format(int(adultDisPri), ',')))
    print('='*60)
    print(f'Total: {totPeo}')
    print('TotalPrice: {}원'.format(format(int(totPri), ',')))
    print('='*60)

print('infantPrice(24개월 미만) \t : 18,000원')
print('childPrice(만 12세 미만) \t : 25,000원')
print('adultPrice(만 12세 이상) \t : 50,000원')
print('국가 유공자 및 장애우 할인 \t\t : 50%\n')

infant = int(input('유아 수 입력: '))
infantDis = int(input('할인대상 유아 수 입력: '))
child = int(input('소아 수 입력: '))
childDis = int(input('할인대상 소아 수 입력: '))
adult = int(input('성인 수 입력: '))
adultDis = int(input('할인대상 성인 수 입력: '))

ticketRecipt(infant, infantDis, child, childDis, adult, adultDis)
