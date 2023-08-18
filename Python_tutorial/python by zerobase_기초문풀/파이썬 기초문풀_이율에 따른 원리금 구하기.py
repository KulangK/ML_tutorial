money = int(input('금액 입력: '))
intRate = float(input('이율 입력: '))
year = int(input('기간 입력: '))
moneyRes = money
intRate1 = (intRate + 100)/100

for i in range(1, year+1):
    moneyRes *= intRate1 # moneyRes += moneyRes * intRate * 0.01 로도 가능

print('-'*30)
print('이율: %.1f%%\n원금: %s원\n%d년 후 금액: %s원' \
      %(intRate, format(money, ','), year, format(int(moneyRes), ',')))
print('-'*30)
