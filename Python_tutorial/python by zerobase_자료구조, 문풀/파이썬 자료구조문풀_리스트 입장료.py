import random as rd

infant = []; child = []; juvenile = []; adult = []; senior = []

n = 0
while n < 100:
    x = rd.randint(1, 100)
    if x <= 7:
        infant.append(x)
    elif x > 7 and x <= 13:
        child.append(x)
    elif x > 13 and x <= 19:
        juvenile.append(x)
    elif x > 19 and x <= 64:
        adult.append(x)
    else:
        senior.append(x)
    n += 1

a1 = 0; a2 = 200*len(child); a3 = 300*len(juvenile); a4 = 500*len(adult)  # 가격
a5 = 0
tot = a1 + a2 + a3 + a4 + a5

print('-'*30)
print(f'영유아 \t : {len(infant)}명  \t : {a1}원')
print(f'어린이 \t : {len(child)}명  \t : {a2}원')
print(f'청소년 \t : {len(juvenile)}명  \t : {a3}원')
print(f'성인 \t : {len(adult)}명  \t : {a4}원')
print(f'어르신 \t : {len(senior)}명  \t : {a5}원')
print('-'*30)
print('1일 요금 총합계: {}원'.format(format(tot, ',')))
print('-'*30)
