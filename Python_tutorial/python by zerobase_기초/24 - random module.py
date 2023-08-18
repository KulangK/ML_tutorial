import operator
import random

rInt = random.randint(10, 100)

num10 = operator.floordiv(rInt, 10)
num1 = operator.mod(rInt, 10)

print('난수 : {}'.format(rInt))
print('십의 자리 : {}'.format(num10))
print('일의 자리 : {}'.format(num1))

print('십의 자리는 3의 배수이다. : {}'.format(operator.mod(num10, 3) == 0))
print('일의 자리는 3의 배수이다. : {}'.format(operator.mod(num1, 3) == 0))
