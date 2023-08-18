# 1부터 100까지 정수 중에서 홀수인 난수를 반환하는 함수 선언

import random

def odd():
    while 1:
        x = random.randint(1, 100)
        if x % 2 != 0:
            break
        print('난수 발생, {}는 홀수가 아닙니다.'.format(x))
    return x

print(f'홀수 생성 완료: {odd()}')