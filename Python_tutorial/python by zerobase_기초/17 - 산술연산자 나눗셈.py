# 3가지 과목의 점수 입력, 합계와 평균 출력

kor = int(input('국어 점수: '))
eng = int(input('영어 점수: '))
mat = int(input('수학 점수: '))

total = kor + eng + mat
avg = total / 3

print('국어 점수: {}\n영어 점수: {}\n수학 점수: {}'.format(kor, eng, mat))
print('종합 점수: {}\n점수 평균: %.2f'.format(total) % avg)
