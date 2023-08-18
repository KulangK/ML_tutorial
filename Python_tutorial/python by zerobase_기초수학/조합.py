numN = int(input('조합 n 입력: '))
numR = int(input('조합 r 입력: '))

resultP = 1
resultR = 1
resultC = 1

for n in range(numN, numN-numR, -1):
    print('n : {}'.format(n))
    resultP = resultP * n

print('resultP: {}'.format(resultP))

for n in range(1, numR+1):
    resultR *= n

resultC = int(resultP / resultR)

print('resultC: {}'.format(resultC))

# 공식에 따라 nPr / r!을 이용한 코딩임

def combination(n, r):
    resultP = 1
    resultR = 1
    resultC = 1
    for n in range(n, n - r, -1):
        resultP = resultP * n

    for n in range(1, r + 1):
        resultR *= n

    resultC = int(resultP / resultR)
    return resultC