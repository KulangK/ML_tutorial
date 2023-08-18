g1Price = 2000; g2Price = 1000; g3Price = 800
g4Price = 2000; g5Price = 900               # 물품의 가격선정

def formattedNum(n):
    return format(n, ',')
def calculator(*gcs):                       # 여러 물품, 여러 갯수가 될 수 있으므로 * 추가
                                            # * 사용시 반복 가능한 자료형으로 들어오게 됨.
    gcsDic = {}
    againCntInput = {}

    for idx, gc in enumerate(gcs):          # 입력을 goods1 부터 순서대로 받기 때문에 순서 맞추는 것까지 고려 X
        try:
            gcsDic[f'g{idx+1}'] = int(gc)   # 구매 물품과 구매 갯수를 dic으로 넣음
        except Exception as e:
            againCntInput[f'g{idx+1}'] = gc
            print(e)

    totalPrice = 0
    for g in gcsDic.keys():
        totalPrice += globals()[f'{g}Price'] * gcsDic[g]    # gcsDic[g] = 해당 물품의 갯수
#                     globals()['g1Price']... 전역 변수의 값을 불러오는데 쓰는 방법, 해당 물품의 가격이 됨.
    print('-'*50)
    print(f'총 구매 금액: {formattedNum(totalPrice)}원')
    print('-'*20, '미결제 항목', '-'*20)
    for g in againCntInput.keys():
        print(f'상품: {g}, \t 구매 개수: {againCntInput[g]}')
    print('-'*50)