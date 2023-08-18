# 상수도 요금 계산기
"""
가정용 (사용량 무관) - 540 원
대중탕용
 - 50 이하 : 820원
 - 50 초과 300 이하 : 1920원
 - 300 초과 : 2,400원
공업용
 - 500 이하 : 240원
 - 500 초과 : 470원
"""

choice = int(input('용도 선택: 1. 가정용 \t 2. 대중탕용 \t 3. 공업용 '))
liter = int(input('사용량 입력: '))
price = 0

if choice == 1:
      price = liter * 540

if choice == 2:
      if liter <= 50:
            price = liter * 820
      elif liter > 50 and liter <= 300:
            price = liter * 1920
      else:
            price = liter * 2400

if choice == 3:
      if liter <= 500:
            price = liter * 240
      else:
            price = liter * 470

print('=' * 50)
print('상수도 요금표')
print('-' * 50)
print('사용량 \t : \t 요금\n{} \t : \t {}원'.format(liter, format(price, ',')))
print('=' * 50)
