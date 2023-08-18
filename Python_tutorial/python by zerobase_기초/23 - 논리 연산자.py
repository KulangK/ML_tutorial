kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

tot = kor + eng + mat
avg = tot / 3

print('평균: {}, 결과: {}'.format(avg, avg>=70))
print('국어: {}, 결과: {}'.format(kor, kor>=60))
print('영어: {}, 결과: {}'.format(eng, eng>=60))
print('수학: {}, 결과: {}'.format(mat, mat>=60))
print('과락 결과: {}'.format(kor >= 60 and eng >= 60 and mat >= 60))
print('최종 결과: {}'.format(avg >= 70 and kor >= 60 and eng >= 60 and mat >= 60))