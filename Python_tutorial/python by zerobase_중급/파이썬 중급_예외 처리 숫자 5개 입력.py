nums = []

n = 1
while n < 6:
    try:
        num = int(input('input number: '))
    except:
        print('예외 발생, 정수를 입력해주세요')
        continue                                # continue가 없으면, line 11, 12 진행되어 이전 숫자가 들어감

    nums.append(num)
    n += 1

print(f'nums: {nums}')