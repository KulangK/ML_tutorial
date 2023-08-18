import datetime

userAge = input('나이 입력 : ')
today = datetime.datetime.today()

if userAge.isdigit():
    year100 = 100 - int(userAge)
    print('{}년({}년후)에 100살!!'.format(today.year+year100, year100))

else:
    print('숫자를 입력하시오.')
