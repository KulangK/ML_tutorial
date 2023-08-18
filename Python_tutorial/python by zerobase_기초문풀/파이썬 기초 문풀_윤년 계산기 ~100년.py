year = int(input('연도 입력: '))

# 윤년 조건: 4로 나누어 떨어지고 100으로 나누어떨어지지 않으면 윤년
# 또는 연도가 400으로 나누어 떨어지면 윤년
# + 100년 까지 평년/윤년 여부 출력

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('{}년 :\t윤년'.format(year))

else:
    print('{}년 :\t평년'.format(year))

for i in range(year+1, year+101):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print('{}년 :\t윤년'.format(i))

    else:
        print('{}년 :\t평년'.format(i))
