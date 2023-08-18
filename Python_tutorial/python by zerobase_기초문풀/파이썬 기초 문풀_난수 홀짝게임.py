# 난수 이용하여 홀짝 게임

import random

num = random.randint(1,2)
user = int(input('숫자 선택, 1: 홀, 2: 짝: '))

if num == 1 and user == 1:
      print('정답, 홀수')
elif num == 2 and user == 1:
      print('오답, 짝수')
elif num == 1 and user == 2:
      print('오답, 홀수')
elif num == 2 and user == 2:
      print('정답, 짝수')