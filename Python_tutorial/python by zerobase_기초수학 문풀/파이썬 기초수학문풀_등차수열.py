# aGroup = 4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64...

# an = a1 + (n-1)*d
# Sn = n(a1 + an) / 2

print(f'수열: 4, 10, 16, 22, 28, 34, 40, 46, 52, 58, 64...')

userInput = int(input('n항 입력: '))

an = 4 + (userInput-1)*6
sn = (userInput * (4 + an)) / 2

print(f'n항의 값: {an}\nn항까지의 합: {int(sn)}')