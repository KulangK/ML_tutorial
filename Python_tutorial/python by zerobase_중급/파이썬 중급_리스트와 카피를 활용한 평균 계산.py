scores = [int(input('국어 점수 입력: ')),
          int(input('영어 점수 입력: ')),
          int(input('수학 점수 입력: '))]

print(scores)

copyScores = scores.copy()

for i, score in enumerate(copyScores): # 그냥 list 그대로 쓰면, index 적용이 안되고, i는 score 자체를 읽음
    result = score * 1.1
    copyScores[i] = 100 if result > 100 else result # 평균이 10% 올랐을때 100을 넘는 경우 때문에 추가된 line

print(f'이전 평균: {round(sum(scores) / len(scores), 2)}')
print(f'이후 평균: {round(sum(copyScores) / len(copyScores), 2)}')

