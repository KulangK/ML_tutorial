price = input('상품 가격 입력 : ')
payment = input('지불 금액 입력 : ')

if price.isdigit() and payment.isdigit() and int(payment) >= int(price):
    change = int(payment) - int(price)
    changeF = (change // 10) * 10
    print('거스름 돈: {}(원단위 절사)'.format(changeF))
    F50k = 0
    F10k = 0
    F5k = 0
    F1k = 0
    F500 = 0
    F100 = 0
    F10 = 0
    if changeF >= 50000:
        F50k = changeF // 50000
        changeF -= 50000*F50k
    if changeF >= 10000:
        F10k = changeF // 10000
        changeF -= 10000*F10k
    if changeF >= 5000:
        F5k = changeF // 5000
        changeF -= 5000*F5k
    if changeF >= 1000:
        F1k = changeF // 1000
        changeF -= 1000*F1k
    if changeF >= 500:
        F500 = changeF // 500
        changeF -= 500*F500
    if changeF >= 100:
        F100 = changeF // 100
        changeF -= 100*F100
        F10 = changeF // 10
    print('-' * 30)
    print('50,000 {}장\n10,000 {}장\n5,000 {}장\n1,000 {}장\n500 {}개\n100 {}개\n10 {}개'\
          .format(F50k, F10k, F5k, F1k, F500, F100, F10))
    print('-' * 30)
else:
    print('숫자가 아니거나, 지불 금액이 상품 가격보다 낮습니다.')