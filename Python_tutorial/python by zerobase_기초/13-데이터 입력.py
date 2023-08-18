# 13_Data Input: 데이터 입력

"""
print('키보드를 통해서 데이터를 입력하세요.')
userInputData = input()
    >> this can be simplified by userInputData = input('키보드를 통해서 데이터를 입력하세요.')

print(userInputData)

* input() function 'always' assigns data as string
* if you want to change the data type of input()
  >> use data casting: int(input()), float(input()), bool(input())

#실습
#오늘의 날씨를 입력하고 출력해보자

weather = input('오늘의 날씨를 입력해주세요 : ')
print('오늘의 날씨는 \'%s\'입니다.' %weather)

# 사용자 이름을 입력하고 입력한 데이터의 자료형을 확인하는 코드를 작성해보자

userName = input('사용자의 이름을 입력해주세요 : ')
print('작성한 데이터의 자료형은', type(userName), '입니다.')

# 사용자가 가로, 세로 길이를 입력하면 삼각형과 사각형의 넓이가 출려되는 코드를 작성해보자
width = int(input('삼각형과 사각형의 넓이를 구하도록 너비를 입력해주세요.'))
height = int(input('다음으로 높이를 입력해주세요.'))
print('입력하신 너비는 %d이며, 높이는 %d입니다.\n삼각형의 넓이는 %d입니다.\n사각형의 넓이는 %d입니다'
      %(width, height, width * height / 2, width * height))
"""
