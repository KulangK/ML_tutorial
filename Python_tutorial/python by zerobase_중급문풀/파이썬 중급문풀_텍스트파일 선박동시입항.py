uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급문풀/ship.txt'

ship1 = 3                                               # 해설에서 유클리드 호제법 사용
ship2 = 4
ship3 = 5
maxDay = 0

for i in range(1, (ship1 + 1)):                         # ship1 과 ship2의 최대 공약수
    if ship1 % i == 0 and ship2 % i == 0:
        maxDay = i                                      # maxDay = 최대 공약수

minDay = (ship1 * ship2) // maxDay                      # minDay = ship1과 ship2의 최소 공배수

for i in range(1, minDay + 1):
    if ship3 % i == 0 and minDay % i == 0:
        maxDay = i                                      # minDay와 ship3의 최대 공약수

minDay = (ship3 * minDay) // maxDay                     # minDay = 기존 minDay와 ship3의 최소 공배수

print(f'minDay: {minDay}')
print(f'maxDay: {maxDay}')

from datetime import datetime
from datetime import timedelta

n = 1
baseTime = datetime(2021, 1, 1, 10, 0, 0)             # datetime() 함수

with open(uri, 'a') as f:
    f.write(f'2021년 모든 선박 입항일\n')
    f.write(f'{baseTime}\n')

nextTime = baseTime + timedelta(days=minDay)          # timedelta() 함수
while 1:
    with open(uri, 'a') as f:
        f.write(f'{nextTime}\n')

    nextTime = nextTime + timedelta(days=minDay)
    if nextTime.year > 2021:
        break




