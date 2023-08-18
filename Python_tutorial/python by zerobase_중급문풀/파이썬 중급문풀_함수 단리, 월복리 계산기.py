def form(n):
    return format(n, ',')       # formatted form으로 만드는 function

def simpleInter(x, y, z):
    totalMoney = 0
    totalRate = 0

    for i in range(y):
        totalRate += x * (z * 0.01)

    totalMoney = x + totalRate  # 단리이므로 이자 계산후 원금에 더하면 됨.
    return int(totalMoney)


def monCompInter(x, y, z):
    totalMoney = x
    totalRate = 0

    y = y * 12              # 월복리이므로 연 복리를 12로 나눠줌.
    z = z/12 * 0.01         # 월복리이므로 연 이자를 12로 나누어 월 이자로 만들어줌.

    for i in range(y):
        totalMoney += totalMoney * z  # 복리이므로, 매 계산에 (원금 + 이자) 가 들어가게 됨.

    return int(totalMoney)

money = int(input('예치금(원): '))
year = int(input('기간(년): '))
rate = int(input('연 이율(%): '))

simpleMoney = simpleInter(money, year, rate)
compoundMoney = monCompInter(money, year, rate)

print('[단리 계산기]')
print('='*40)
print(f'예치금   \t : {form(money)}원')
print(f'예치기간 \t : {year}년')
print(f'연 이율  \t : {rate}%')
print('-'*40)
print(f'{year}년 후 총 수령액: {form(simpleMoney)}원')
print('='*40, '\n')

print('[월 복리 계산기]')
print('='*40)
print(f'예치금   \t : {form(money)}원')
print(f'예치기간 \t : {year}년')
print(f'연 이율  \t : {rate}%')
print('-'*40)
print(f'{year}년 후 총 수령액: {form(compoundMoney)}원')
print('='*40)