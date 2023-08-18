ans = int(input('출퇴근 대상자입니까? 1. YES \t 2. NO : '))

if ans == 1:
    print('주로 이용하는 교통수단을 선택하세요.')
    trans = int(input('1.도보, 자전거 \t 2.버스, 지하철 \t 3.자가용 : '))

    if trans == 1:
        print('세금 감면 5% 대상자입니다.')
    elif trans == 2:
        print('세금 감면 3% 대상자입니다.')
    elif trans == 3:
        print('추가 세금 1% 대상자입니다.')

elif ans == 2:
    print('세금 변동 대상자가 아닙니다.')
else:
    print('잘못 입력하셨습니다.')
