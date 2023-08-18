score = [1, 2, 3, 4, 5]
scoreCopy = []

# scoreCopy = score  >> 얕은 복사
#
# print(score)
# print(scoreCopy)
#
# scoreCopy.append(7)
#
# print(score)
# print(scoreCopy)


# for s in score:
#     scoreCopy.append(s) >> score의 각 값만 가져오는 것


# scoreCopy.extend(score) >> score list 를 copy에 확장시키는 것


# scoreCopy = score.copy() >> score list 깊은 복사


# scoreCopy = score[:]  >> slicing score list 전체