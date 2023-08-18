midT = input('중간 고사 점수: ')
endT = input('기말 고사 점수: ')

if midT.isdigit() and endT.isdigit() :
    tot = int(midT) + int(endT)
    totSt = str(tot)[0] + ('*'*(len(str(tot))-1))
    avg = tot / 2
    print('총점 : %s, 평균: %.1f' %(totSt, avg))
else:
    print('잘못 입력했습니다.')

print()

midT = input('중간 고사 점수: ')
endT = input('기말 고사 점수: ')

if midT.isdigit() and endT.isdigit() :
    tot = int(midT) + int(endT)
    totSt = str(tot)[0] + ('*'*(len(str(tot))-1))
    avg = tot / 2
    print('총점 : %s, 평균: %.1f' %(totSt, avg))
else:
    print('잘못 입력했습니다.')