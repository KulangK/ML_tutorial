import operator

age = int(input('나이 입력: '))

vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))

print('나이 : {}, 백신 접종 대상 여부 : {}'.format(age, vaccine))