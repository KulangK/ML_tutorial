# 난수 맞추기 게임 (1~1000)

import random

target = random.randint(1, 1000)
user = 0
count = 0

while target != user:
      user= int(input(('1에서 1000까지의 정수 입력: ')))
      count += 1

      if user > target:
            print('난수가 작다.')
      elif user < target:
            print('난수가 크다.')

print('정답\n난수: {}, 시도 횟수: {}'.format(target, count))

# while 조건 안에 flag 같은 것을 넣고, if 문을 추가하여
# target == user 일때 정답을 표시하는 방법도 있음. 물론 그때는 flag도 false로 바꿔줘야 함