scoreDic = {}

uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급/'

with open(uri + 'score.txt', 'r') as f:         # 파일 오픈 (읽기 모드)
    line = f.readline()                         # 첫 번째 라인 할당

    while line != '':                           # 반복문 시작
        templist = line.split(':')              # line 변수에 해당하는 행 ':' 기점으로 나눠서 리스트 할당
        scoreDic[templist[0]] = int(templist[1].strip('\n'))   # .strip: 개행 때문에 \n 문자열도 리스트에 들어가기 때문에, 
                                                               # 해당 문자를 뜯어내는 구문
        line = f.readline()                     # 다음 행을 line 변수에 할당

print(f'scoreDic: {scoreDic}')