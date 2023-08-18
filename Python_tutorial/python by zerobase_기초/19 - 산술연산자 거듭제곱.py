iniMoney = 200
aft12Month = iniMoney * 2 ** 11

print('12개월 후 용돈: {}'.format(aft12Month))

aft12MonthForm = format(aft12Month, ',d')
print('12개월 후 용돈: {}'.format(aft12MonthForm))
print('type: {}'.format(type(aft12MonthForm)))

aft12MonthForm = format(aft12Month, ',')
print('12개월 후 용돈: {}'.format(aft12MonthForm))
print('type: {}'.format(type(aft12MonthForm)))

