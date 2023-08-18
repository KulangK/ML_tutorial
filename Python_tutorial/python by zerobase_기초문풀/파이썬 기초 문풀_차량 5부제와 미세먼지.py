# 미세먼지 비상저감 조치, 차량 운행제한 프로그램

""" 조건
1. 미세먼지 수치 150 이하, 차량 5부제 실시
2. 미세먼지 수치 150 초과, 차량 2부제 실시
3. 차량 2부제 실시하더라도 영업용 차량 5부제 실시
4. 미세먼지 수치, 차량 종류, 차량 번호 입력하면 운행가능여부 출력

* 차량 2부제, 5부제 : 차량 끝자리로 분류
      - 2부제: 홀수 끝번호 > 홀수 날 운행
      - 5부제: 1, 6; 2, 7; 등 2그룹씩 해당 날짜 끝자리날 운행 제한
"""

import datetime

dust = int(input('미세먼지 수치 입력: '))
car = int(input('차량 종류 선택: 1. 승용차 \t 2. 영업용 차량 \t '))
carNum = input('차량 번호 뒷 4자리 입력: ')
today = datetime.datetime.today()
day = today.day

print('-'*30)
print(today)
print('-'*30)

if dust <= 150:
    if car == 1:
        if (carNum % 5) == (day % 5):
            print('차량 5부제 적용\n차량 5부제로 금일 운행제한 대상 차량입니다.')
        else:
            print('금일 운행 가능합니다.')
    if car == 2:
        if (carNum % 2) != (day % 2):
            print('금일 운행 가능합니다.')
        else:
            print('차량 2부제 적용\n차량 2부제로 금일 운행제한 대상 차량입니다.')
if dust > 150:
    if (carNum % 2) == (day % 2):
        print('금일 운행 가능합니다.')
    else:
        print('차량 2부제 적용\n차량 2부제로 금일 운행제한 대상 차량입니다.')

print('-'*30)
