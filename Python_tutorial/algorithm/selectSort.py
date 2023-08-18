import copy

def selectSortingAsc(nums, deepCopy = True):
    if deepCopy:
        cnums = copy.copy(nums)
    else:
        cnums = nums

    for i in range(len(cnums)-1):
        minIdx = i

        for j in range(i + 1, len(cnums)):
            if cnums[minIdx] > cnums[j]:
                minIdx = j

        cnums[i], cnums[minIdx] = cnums[minIdx], cnums[i]

    return cnums

def selectSortingDsc(nums, deepCopy = True):
    if deepCopy:
        cnums = copy.copy(nums)
    else:
        cnums = nums

    for i in range(len(cnums)-1):
        maxIdx = i

        for j in range(i + 1, len(cnums)):
            if cnums[maxIdx] < cnums[j]:
                maxIdx = j

        cnums[i], cnums[maxIdx] = cnums[maxIdx], cnums[i]

    return cnums

# 강의에서는 함수 매개변수를 하나 더 추가 (asc = True)
# if ~ else 로 오름, 내림차순을 구분하였음