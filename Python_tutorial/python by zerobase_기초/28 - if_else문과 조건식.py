ltemp = int(input('최저 기온 입력: '))
htemp = int(input('최고 기온 입력: '))

if (htemp - ltemp) >= 11 :
    print('일교차: {}도\n\'감기 조심하세요.\''.format(int(htemp-ltemp)))
else:
    print('일교차: {}도\n\'산책하기 좋은 날씨입니다.\''.format(int(htemp-ltemp)))