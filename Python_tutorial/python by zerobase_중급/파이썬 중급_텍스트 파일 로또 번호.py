import random

# 추후 파일 위치 간략화를 위한 변수 선언
uri = 'C:/Users/User/PycharmProjects/pythonProject/python by zerobase_중급/'

def lotto(x):
    for i, n in enumerate(x):           # i = idx, n = 해당 인덱스 문자, x = 배열
        with open(uri + 'lotto.txt', 'a') as f:
            if i < (len(x) - 2):        # 0~4 (5개) 인덱스는 뒤에 쉼표 붙이도록
                f.write(str(n) + ', ')
            elif i == (len(x) - 2):     # 5 (6번째) 인덱스는 쉼표 필요 없음
                f.write(str(n))
            elif i == (len(x) - 1):     # 6 (7번째) 인덱스는 보너스기에 따로 표기
                f.write(f'\nbonus: {str(n)}\n')

lottoNum = random.sample(range(1, 46), 7) # 7개 숫자 발생, 인덱스는 0~6
print(f'lottoNum: {lottoNum}')

lotto(lottoNum)