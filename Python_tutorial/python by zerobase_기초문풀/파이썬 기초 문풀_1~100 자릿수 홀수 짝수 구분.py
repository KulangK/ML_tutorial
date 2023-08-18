# 1부터 100까지 정수 중 십의 자리와 일의 자리에 대해 각각 홀/짝수를 구분하는 프로그램 만들기

for i in range(1, 101):
      if i < 10:
            if i % 2 == 0:
                  print('[{}]: {}'.format(i, '짝수!'))
            else:
                  print('[{}]: {}'.format(i, '홀수!'))
      else:
            print('[{}]'.format(i), end=' ')
            if str(i)[-2] == '0':
                  print('십의 자리: 0', end=', ')
            elif (i // 10) % 2 == 0:
                  print('십의 자리: 짝수!!', end=', ')
            else:
                  print('십의 자리: 홀수!!', end=', ')
            if str(i)[-1] == '0':
                  print('일의 자리: 0')
            elif i % 2 == 0:
                  print('일의 자리: 짝수!!')
            else:
                  print('일의 자리: 홀수!!')
