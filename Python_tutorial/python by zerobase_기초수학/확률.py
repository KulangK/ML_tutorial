# 박스 안에 x개의 당첨과 y개의 꽝이 담겼다고 했을 때, z개의 꽝과 w개의 당첨을 뽑는 경우는?
# 순서는 상관 없기에 combination 이용, 전체 수인 n = x + y, 꽝과 당첨을 뽑는 경우는 yCz*xCw / nC(z+w)

def cb(n, r):                                       # cb = combination
    resultP = 1
    resultR = 1
    resultC = 1
    for n in range(n, n - r, -1):
        resultP = resultP * n

    for n in range(1, r + 1):
        resultR *= n

    resultC = int(resultP / resultR)
    return resultC

x = int(input('당첨 갯수 입력: '))
y = int(input('꽝 갯수 입력: '))
z = int(input('뽑는 꽝 갯수 입력: '))
w = int(input('뽑는 당첨 갯수 입력: '))

n = x + y                       # 표본의 총 갯수
r = z + w                       # 표본 중 획득 표적 갯수

whole = cb(n, r)
defeat = cb(y, z)
win = cb(x, w)

result = round(((defeat*win)/whole) * 100, 2)


print('result in possibility: {}%'.format(result))