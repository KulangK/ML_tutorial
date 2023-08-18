pass1 = 60
pass2 = 70

kor = int(input('국어 점수: '))
eng = int(input('영어 점수: '))
mat = int(input('수학 점수: '))

korRes = kor >= pass1
engRes = eng >= pass1
matRes = mat >= pass1
subRes = korRes and engRes and matRes

tot = kor + eng + mat
avg = tot / 3
totRes = avg >= pass2

print('평균: {}, 결과: {}'.format(avg, totRes))
print('국어: {}, 결과: {}'.format(kor, korRes))
print('영어: {}, 결과: {}'.format(eng, engRes))
print('수학: {}, 결과: {}'.format(mat, matRes))
print('과락 결과: {}'.format(subRes))
print('최종 결과: {}'.format(subRes and totRes))