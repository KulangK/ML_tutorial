# 국어, 영어, 수학 점수 입력 후 총점, 평균, 최고 점수 과목, 최저 점수 과목,
# 최고 점수와 최저 점수의 차이를 출력하라

kor = int(input('국어 점수 입력: '))
eng = int(input('영어 점수 입력: '))
mat = int(input('수학 점수 입력: '))
tot = kor + eng + mat
avg = tot / 3

print('총점: %d\n평균: %.2f' %(tot, avg))
max = ()
maxn = ()
least = ()
leastn = ()

if kor > eng and kor > mat:
    max = kor
    maxn = '국어'
elif eng > mat and eng > kor:
    max = eng
    maxn = '영어'
elif mat > kor and mat > eng:
    max = mat
    maxn = '수학'

if kor < eng and kor < mat:
    least = kor
    leastn = '국어'
elif eng < mat and eng < kor:
    least = eng
    leastn = '영어'
elif mat < kor and mat < eng:
    least = mat
    leastn = '수학'

print('-'*30)
print('최고 점수 과목(점수): {}({})'.format(maxn, max))
print('최저 점수 과목(점수): {}({})'.format(leastn, least))
print('최고, 최저 점수 차이: {}'.format(max - least))
print('-'*30)

