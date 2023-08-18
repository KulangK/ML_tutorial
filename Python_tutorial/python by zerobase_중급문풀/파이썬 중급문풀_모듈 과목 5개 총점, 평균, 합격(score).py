import score

tot = 0
totAvg = 0

scores = [int(input('과목1 점수 입력: ')),
        int(input('과목2 점수 입력: ')),
        int(input('과목3 점수 입력: ')),
        int(input('과목4 점수 입력: ')),
        int(input('과목5 점수 입력: '))]

for i, x in enumerate(scores):
        tot += x

totAvg = tot / len(scores)
print(f'총점: {tot}')
print(f'평균: {totAvg}')

score.testpass(scores)