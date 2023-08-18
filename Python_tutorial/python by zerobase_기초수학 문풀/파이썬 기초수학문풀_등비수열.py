# 등비수열 일반항: a1 * r^(n-1)
# 등비수열의 합: a1 * (1-r^n) / (1-r)

userA = int(input('a1 입력: '))
userN = int(input('n항 입력: '))
userR = int(input('r 입력: '))

sumN = 0                                            # for문으로 표현할 합
sumNCal = userA * (1-userR**userN) / (1-userR)      # 계산식으로 표현할 합


for i in range(1, userN+1):
    if i == 1:
        sumN += userA
        print(f'{i}항: {userA}')
        continue
    userA *= userR
    sumN += userA
    print(f'{i}항: {userA}')

print(f'{userN}항 까지의 합: {sumN}')
print(f'{userN}항 까지의 합: {sumNCal}')



