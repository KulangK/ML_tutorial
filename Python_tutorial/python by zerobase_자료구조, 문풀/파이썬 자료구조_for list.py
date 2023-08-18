# 5가지 과목, 점수 입력, 과락 과목과 점수 출력

sub1 = input('1과목 이름과 점수 입력: ').split(',')
sub2 = input('2과목 이름과 점수 입력: ').split(',')
sub3 = input('3과목 이름과 점수 입력: ').split(',')
sub4 = input('4과목 이름과 점수 입력: ').split(',')
sub5 = input('5과목 이름과 점수 입력: ').split(',')

minScore = int(input('과락 점수 입력: '))

subjects = [sub1, sub2, sub3, sub4, sub5]

print(subjects)                 # 리스트 형성 확인을 위한 코드
for i, sco in subjects:
    if int(sco) > minScore:
        continue
    print(f'{i} 과목 과락, 점수: {int(sco)}')


