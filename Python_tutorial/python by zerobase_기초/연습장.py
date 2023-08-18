import operator
pass1 = 60
pass2 = 70

kor = int(input('국어 점수: '))
eng = int(input('영어 점수: '))
mat = int(input('수학 점수: '))

tot = kor + eng + mat
Avg = tot / 3

print('국어 : PASS') if operator.ge(kor, pass1) else print('국어 : FAIL')
print('영어 : PASS') if operator.ge(eng, pass1) else print('영어 : FAIL')
print('수학 : PASS') if operator.ge(mat, pass1) else print('수학 : FAIL')
print('시험 : PASS') if operator.ge(Avg, pass2) else print('시험 : FAIL')

print('총점: %d, 평균: %.2f' %(tot, Avg))