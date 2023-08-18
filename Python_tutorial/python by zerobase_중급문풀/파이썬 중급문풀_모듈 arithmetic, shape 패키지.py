from arithmetic import basic_operator as bop
from arithmetic import developer_operator as dop
from shape import circle_area as ci
from shape import triangle_square_area as ar

num1 = float(input('숫자 1 입력: '))
num2 = float(input('숫자 1 입력: '))

bop.bopercal(num1, num2)
dop.dopercal(num1, num2)

width = float(input('가로 길이 입력: '))
height = float(input('세로 길이 입력: '))

ar.area(width, height)

rad = float(input('반지름 입력: '))

ci.circleArea(rad)
