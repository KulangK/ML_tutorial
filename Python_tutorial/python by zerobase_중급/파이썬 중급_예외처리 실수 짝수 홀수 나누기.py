floats = []
odds = []
evens = []

n = 1

while n < 6:
    try:
        num = float(input('숫자를 입력하라: '))

    except:
        print('숫자가 아닙니다. 다시 입력하세요.')
        continue

    else:
        if num - int(num) != 0:                 # 실수 거르기
            floats.append(num)                  # 이하 elif 는 정수만 남음
            n += 1
            
        elif num % 2 == 0:                      # 짝수인 정수 거르기
            evens.append(num)                   # 이하 홀수인 정수만 남음
            n += 1
            
        else:
            odds.append(num)
            n += 1

print(f'입력한 실수: {floats}')
print(f'입력한 짝수: {evens}')
print(f'입력한 홀수: {odds}')