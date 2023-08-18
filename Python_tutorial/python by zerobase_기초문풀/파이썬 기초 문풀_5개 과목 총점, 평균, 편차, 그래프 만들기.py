# 국어, 영어, 수학, 과학, 국사 점수를 입력하면 총점을 비롯한 각종 데이터가 출력되는 프로그램 작성
# 1. 과목별 점수를 입력하면 총점, 평균, 편차 출력
#    각 과목별 평균 (국어: 85, 영어: 82, 수학: 89, 과학: 75, 국사: 94)
# 2. 각종 편차 데이터는 막대그래프로 시각화

kor = int(input('국어 점수 입력: ')); eng = int(input('영어 점수 입력: ')); mat = int(input('수학 점수 입력: '))
sci = int(input('과학 점수 입력: ')); his = int(input('국사 점수 입력: '))

korStan = 85; engStan = 82; matStan = 89; sciStan = 75; hisStan = 94

totStan = korStan + engStan + matStan + sciStan + hisStan
avgStan = int(totStan / 5)

userTot = kor + eng + mat + sci + his
userAvg = int(userTot / 5)

korDif = kor - korStan; engDif = eng - engStan; matDif = mat - matStan
sciDif = sci - sciStan; hisDif = his - hisStan

totDif = userTot - totStan; avgDif = userAvg - avgStan

print('-'*65)
print('총점: {}({}), 평균: {}({})'.format(userTot, totDif, userAvg, avgDif))
print('국어: {}({}), 영어: {}({}), 수학{}({}), 과학{}({}), 국사{}({})'\
      .format(kor, korDif, eng, engDif, mat, matDif, sci,sciDif, his, hisDif))
print('-'*65)
str = '*' if korDif > 0 else '-'
print('국어 편차: {}({})'.format(str * abs(korDif), korDif))
str = '*' if engDif > 0 else '-'
print('영어 편차: {}({})'.format(str * abs(engDif), engDif))
str = '*' if matDif > 0 else '-'
print('수학 편차: {}({})'.format(str * abs(matDif), matDif))
str = '*' if sciDif > 0 else '-'
print('과학 편차: {}({})'.format(str * abs(sciDif), sciDif))
str = '*' if hisDif > 0 else '-'
print('국사 편차: {}({})'.format(str * abs(hisDif), hisDif))
str = '*' if avgDif > 0 else '-'
print('평균 편차: {}({})'.format(str * abs(avgDif), avgDif))
print('-'*65)
