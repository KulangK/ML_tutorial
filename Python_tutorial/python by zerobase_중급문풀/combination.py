def setCombination():
    num = []
    n = int(input('numN 입력: '))
    r = int(input('numR 입력: '))
    num = [n, r]
    return num

def getCombination(num):
    permu = 1
    divi = 1
    for i in range(num[0]-num[1]+1, num[0]+1):
        permu *= i
    for x in range(1, num[1]+1):
        divi *= x

    print(f'resultP : {permu}')
    print(f'resultR : {divi}')
    print(f'resultC : {int(permu/divi)}')

from itertools import combinations

def getCombinationGroups(num):
    ns = range(1, num[0] + 1)
    r = num[1]
    pList = list(combinations(ns, r))

    print(f'{len(ns)}P{r} 개수: {len(pList)}')

    for n in combinations(ns, r):
        print(n, end=', ')
