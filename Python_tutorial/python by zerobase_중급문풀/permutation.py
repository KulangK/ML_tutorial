# 순열 계산 모듈

# 순열 = Permutation
# 공식 = nPr = n! / (n-r)!

# e.g. 8 P 5 = 8! / (8-5)! = 8! / 3! = 8 * 7 * 6 * 5 * 4
# n~(n-r+1)까지 곱하면 됨

def setPermutation():
    num = []
    n = int(input('numN 입력: '))
    r = int(input('numR 입력: '))
    num = [n, r]
    return num                                      # 첫번째 실수, return을 하지 않아 밑 get 함수에서 읽어오지 못함.

def getPermutation(num):
    answ = 1
    for i in range(num[0]-num[1]+1, num[0]+1):
        answ *= i

    for i in range(num[0], num[0]-num[1], -1):
        print(f'n : {i}')

    print(f'{num[0]}P{num[1]}: {answ}')

from itertools import permutations

def getPermutationGroups(num):
    ns = range(1, num[0] + 1)
    r = num[1]
    pList = list(permutations(ns, r))               # permutations(ns, r) 의 기능과 list의 기능?
                                                    # permutations(ns, r) >> ns라는 list에서 r갯수 만큼 원소를 뽑아 집합 만듦
                                                    # list는 이러한 permutations(ns, r)을 자료형으로 저장하기 위한 기능
    print(f'{len(ns)}P{r} 개수: {len(pList)}')

    for n in permutations(ns, r):
        print(n, end='')