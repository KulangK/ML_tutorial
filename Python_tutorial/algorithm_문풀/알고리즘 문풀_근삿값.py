depth = [0, 5, 10, 15, 20, 25, 30]     # 깊이와 온도 연결되니 딕셔너리 사용해도 됨
temp = [24, 22, 20, 16, 13, 10, 6]

x = int(input('input depth: '))

print(f'depth: {x}m')

compare = 0
compIdx = 0
for i, num in enumerate(depth):
    if i == 0:
        compare = num - x
    elif abs(num-x) < abs(depth[i-1]-x):
        compare = abs(num-x)
        compIdx = i

print(f'water temperature: {temp[compIdx]}도')
# 근삿값 알고리즘 다시 한번 볼 것