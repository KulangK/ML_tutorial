studentCnt = ({'cls01':18}, {'cls02':21}, {'cls03':20}, {'cls04':19},
              {'cls05':22}, {'cls06':20}, {'cls07':23}, {'cls08':17})

totCnt = 0
minStdCnt = 0; minCls = ''
maxStdCnt = 0; maxCls = ''
deviation = []

for idx, dic in enumerate(studentCnt):          # enumerate로 인덱스와 딕셔너리 구분
    for k, v in dic.items():                    # .items()로 키와 밸류 구분
        totCnt += v

        if minStdCnt == 0 or minStdCnt > v:     # minStdCnt가 0으로 초기화되어 조건이 없으면 계속 0으로 남음
            minStdCnt = v
            minCls = k

        if maxStdCnt < v:
            maxStdCnt = v
            maxCls = k

avg = totCnt / len(studentCnt)

print(f'전체 학생수: {totCnt}명')
print(f'평균 학생수: {avg}명')
print(f'최대 학생 학급: {maxCls}, 학생수: {maxStdCnt}명')
print(f'최소 학생 학급: {minCls}, 학생수: {minStdCnt}명')

for idx, dic in enumerate(studentCnt):
    for k, v in dic.items():
        deviation.append({k : v-avg})           # .append()로 딕셔너리도 추가할 수 있음

print(f'학급별 학생 편차\n{deviation}')

