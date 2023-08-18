def factorial(num):

    if num > 0:
        return num * factorial(num-1)

    else:
        return 1

def gcd(n1, n2):            # 최대 공약수

    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)

def moveDisc(discCnt, fromBar, toBar, viaBar):
    if discCnt == 1:
        print(f'{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동')

    else:
        # (discNo-1)개를 경유 기둥으로 이동
        moveDisc(discCnt-1, fromBar, viaBar, toBar)

        # discNo를 목적 기둥으로 이동
        print(f'{discCnt}disc를 {fromBar}에서 {toBar}(으)로 이동')

        # (discNo-1)개를 목적 기둥으로 이동
        moveDisc(discCnt-1, viaBar, toBar, fromBar)

def mSort(ns, asc=True):    # 병합 정렬

    if len(ns) < 2:         # 아이템이 1개 혹은 0개인 경우, 정렬할 필요 없음
        return ns

    midIdx = len(ns) // 2   # 리스트를 반으로 나눠주기 위함
    if asc:
        leftNums = mSort(ns[:midIdx])
        rightNums = mSort(ns[midIdx:])
    else:
        leftNums = mSort(ns[:midIdx], asc=False)
        rightNums = mSort(ns[midIdx:], asc=False)
    # 위 4줄은 재귀함수로, 리스트가 원소 1개씩 남을 때까지 분해하게 됨.
    # if > 오름차순, else > 내림차순

    mergeNums = []
    leftIdx = 0; rightIdx = 0
    if asc:        # 오름차순
        while leftIdx < len(leftNums) and rightIdx < len(rightNums):

            if leftNums[leftIdx] < rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

        mergeNums = mergeNums + leftNums[leftIdx:]
        mergeNums = mergeNums + rightNums[rightIdx:]

        return mergeNums
    else:           # 내림차순
        while leftIdx < len(leftNums) and rightIdx < len(rightNums):

            if leftNums[leftIdx] > rightNums[rightIdx]:
                mergeNums.append(leftNums[leftIdx])
                leftIdx += 1

            else:
                mergeNums.append(rightNums[rightIdx])
                rightIdx += 1

        mergeNums = mergeNums + leftNums[leftIdx:]
        mergeNums = mergeNums + rightNums[rightIdx:]

        return mergeNums

def qSort(ns, asc=True):        # 퀵 정렬

    if len(ns) < 2:
        return ns

    midIdx = len(ns) // 2
    midVal = ns[midIdx]

    smallNums = []; sameNums = []; bigNums = []

    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n == midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)

    if asc:
        return qSort(smallNums) + sameNums + qSort(bigNums)

    else:
        return qSort(bigNums, asc=asc) + sameNums + qSort(smallNums, asc=asc)
