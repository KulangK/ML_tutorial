# 13_Data print: 데이터 출력

""" print()
print(a, b, ...etc) : print() function show datas in order
    e.g. print('User name :', userName)

print( ~~~ , end='') # deletes \n
"""

""" f'{}'_포맷 문자열 이용
print(f'~~~') == print('')
print(f'~~~ {}') == print('', )
inside '' of f'' is string, {} inside f'' is calling variables 
    e.g. print(f'User name : {userName}, User age : {userAge}')
"""

""" 특수문자
\t = 탭
\n = 개행 (줄 건너뛰기)

userName = '홍길동'
userAge = 20

print(f'User name\t:\t{userName}\nUser age\t:\t{userAge}')

width = float(input('가로 길이 : '))
height = float(input('세로 길이 : '))
triangle = width * height / 2
rectangle = width * height

print(f'width : {width}\nheight : {height}\nTriangle area : {triangle}\nRectangle area : {rectangle}')
"""