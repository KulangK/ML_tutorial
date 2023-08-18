score = [70, 85, 90, 77, 89]            # 입력 받으면 반복이 번거로워져서 예제에 있는 점수 활용함

baseSco = [95, 85, 75, 65, 55]          # 기준이 되는 점수
trueGrade = ['A', 'B', 'C', 'D', 'F']   # 기준 점수의 인덱스를 따라 grade 리스트 선언
grade = []                              # 참값 - 아이템 값을 넣을 공리스트

tot = sum(score)
avg = tot/len(score)

for n in baseSco:
    grade.append(abs(n-avg))            # 참값 - 아이템 값을 공리스트에 넣음

min = grade[0]                          # 첫번째 값을 비교 값으로 넣음
minIdx = 0                              # trueGrade에서 학점을 가져올 인덱스

for i, n in enumerate(grade):           # 참값 - 아이템 값을 비교하여 최솟값 >> 근삿값 할당
    if min > n:
        min = n
        minIdx = i

print(f'avg: {avg}\ngrade: {trueGrade[minIdx]}')

