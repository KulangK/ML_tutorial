# 07_the reason we are using variables

# ctrl + d copies and pastes a code line
""" program
name = '홍길동'

print('%s 고객님께\n%s 고객님 안녕하세요.\n'
      '고객님께서 접수하신 A/S 건에 대해 연락을 드렸으나 연락이 어려워 메일 드립니다.\n'
      'A/S 접수내용 --- 중략 ---\n---------\n성함 : %s\n내용: 에어컨 고장\n--------' %(name, name, name))
"""
# As we use variables, we don't have to repeat the same words after and after
# This makes a program more efficient

# 08_Naming Variables

"""
recommend naming variables
   1. in English
   2. first should be in lower case
   3. use relevant nouns
      e.g. myWeight, userNameAndAge, userEthnicity
   4. when using two or more words (enhancing readability)
      a. use upper case (userName) >> camel case
      b. use _ to separate (user_name) >> snake case
   5. Do Not use reserved words >> might confuse system (a.k.a. 예약어)
   6. Do Not use special characters (e.g. !@#$%^&*()
   7. Do Not use number at the first (e.g. myName1 >> available, 1myName >> unavailable)
"""
""" program
width = int(input('너비를 입력하세요: '))
height = int(input('높이를 입력하세요: '))

print('입력하신 너비는 %d 이며, 높이는 %d 입니다.\n'
      '해당 값을 이용한 삼각형의 넓이는 %d 입니다.\n'
      '해당 값을 이용한 사각형의 넓이는 %d 입니다.'
      %(width, height, width*height/2, width*height))
"""

#09_Data type: 자료형

"""
int: integer number without decimal place
float: number with decimal places
str: string, sequence of characters
bool: boolean, True or False (boolean algebra logic)
"""
""" program
msg = False
msg1 = 1
msg2 = '1'
msg3 = 1.01

print(type(msg))
print(type(msg1))
print(type(msg2))
print(type(msg3))
"""

# 10_Type Casting: 자료형 변환 (문자)

"""
int() (cannot change str or float into int)
float() (cannot change str into float)
str(), can change bool into str
"""
""" program
msg = True
print(msg)
print(type(msg))

msg = str(msg)
print(msg)
print(type(msg))
"""

# 11_Type Casting: 자료형 변환 (숫자)

"""
Data into number_(int(), float())
문자(열) -> 정수 or 실수
논리 -> 정수 or 실수 (true: 1, false: 0)

var = False
print(var)                  # False
print(type(var))            # bool
var = int(var)
print(var)                  # 0
print(type(var))            # integer
var = str(var)
print(var)                  # 0
print(type(var))            # string

str1 = '10'
str2 = '20'
print(str1 + str2)          # 1020

str1 = int(str1)
str2 = int(str2)
print(str1 + str2)          # 30
"""

# 12_Type Casting: 자료형 변환 (그외 데이터)

"""
'' = 빈 문자, False
' ' = 공백 문자, True
문자의 경우 존재 유무가 true, false를 정함.
숫자는 1이 true이고 0이 false 이지만, 문자는 존재 하면 true, 존재 하지 않으면 false

var = ''
print(var)          # empty line
print(type(var))    # <class 'str'>

var = bool(var)
print(var)          # False
print(type(var))    # <class 'bool'>

var = ' '
print(var)          # empty line with one blank
print(type(var))    # <class 'str'>

var = bool(var)
print(var)          # True
print(type(var))    # <class 'bool'>

var1 = 'True'
var2 = 'False'
print(type(var1))    # <class 'str'>
print(type(var2))    # <class 'str'>

var1 = bool(var1)
var2 = bool(var2)
print(type(var1))    # <class 'bool'>
print(type(var2))    # <class 'bool'>

print(var1 + var2)   # 2
print(type(var1+var2)) # <class 'int'>
"""
