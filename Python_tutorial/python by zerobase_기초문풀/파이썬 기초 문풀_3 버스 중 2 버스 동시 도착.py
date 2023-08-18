# 집 앞 버스 정류장에서 학교까지 가는 버스 A, B, C의 운행정보는 다음과 같음. 2대 이상 버스 정차하는 시간대는?
""" 조건
1. 버스 A 운행 정보
    - 오전 6시 첫차: 오후 23시 운행 종료
    - 15분 간격 운행

2. 버스 B 운행정보
    - 오전 6시 첫차: 오후 23시 운행 종료
    - 13분 간격 운행

3. 버스 C 운행 정보
    - 6시 20분 첫차: 오후 22시 운행 종료
    - 8분 간격 운행
"""

# 결국 공배수를 구하는 작업임

busA = 15
busB = 13
busC = 8

endMin = 60*17
for i in range(endMin+1):
    j = i + 20
    if i < 20 or i > (endMin - 60):
        if i % busA == 0 and i % busB == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busA와 busB 동시 정차!! {}:{}'.format(hour, min))
    else:
        if i % busA == 0 and i % busB == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busA와 busB 동시 정차!! {}:{}'.format(hour, min))
        if i % busA == 0 and j % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busA와 busC 동시 정차!! {}:{}'.format(hour, min))
        if i % busA == 0 and i % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busA와 busC 동시 정차!! {}:{}'.format(hour, min))
        if i % busB == 0 and j % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busB와 busC 동시 정차!! {}:{}'.format(hour, min))
        if i % busB == 0 and i % busC == 0:
            hour = 6 + i // 60
            min = i % 60
            print('busB와 busC 동시 정차!! {}:{}'.format(hour, min))