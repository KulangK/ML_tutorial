# 난수 이용하여 가위, 바위, 보 게임 테스트

import random

#user = int(input('가위 바위 보 결정: 1. 가위 \t 2. 바위 \t 3. 보 '))

countCom = 0
countUser = 0
count0 = 0

for i in range (100):
      num = random.randint(1, 3)
      user = random.randint(1, 3)
      if (num == 1 and user == 2) or \
              (num == 2 and user == 3) or \
              (num == 3 and user == 1):
            print('유저 승리')
            countUser += 1
      elif num == user:
            print('무승부')
            count0 += 1
      else:
            print('컴퓨터 승리')
            countCom += 1

print('유저 승리 횟수: {}\n컴퓨터 승리 횟수: {}\n무승부 횟수: {}'\
      .format(countUser, countCom, count0))