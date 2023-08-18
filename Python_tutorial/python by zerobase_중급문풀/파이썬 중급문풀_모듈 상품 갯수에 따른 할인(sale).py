import sale as sa

totPri = 0
endPri = 0
addItem = []

while 1:
        purchase = int(input('상품을 구매 하시겠어요? 1. 구매 2. 종료 '))
        if purchase == 2:
                break
        else:
                n = int(input('상품 가격 입력: '))
                addItem.append(n)

for i, item in enumerate(addItem):
        totPri += addItem[i]

endPri = format(int(totPri * (1 - (sa.itemSale(addItem)/100))), ',')

print(f'할인 전 가격: {totPri}원')
print(f'할인율: {sa.itemSale(addItem)}%')
print(f'합계: {endPri}원')


