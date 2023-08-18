import random as rd
import selectSort as ss

scores = []

for i in range(20):
    scores.append(rd.randint(50, 100))

print(f'scores: {scores}')
print(f'scores length: {len(scores)}')

asc = ss.selectSortingAsc(scores)
dsc = ss.selectSortingDsc(scores)

print(f'result(ASC): {asc}')
print(f'results(DSC): {dsc}')

# copy를 import하고, asc = ss.selectSortingAsc(copy.deepcopy(scores)) 를 사용하면
# 원본에 영향 없이 진행할 수 있음
