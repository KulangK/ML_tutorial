import copy

def ascending(nums):

    cnums = copy.copy(nums)

    for i1 in range(1, len(cnums)):
        i2 = i1 - 1
        cNum = cnums[i1]

        while cnums[i2] > cNum and i2 >= 0:
            cnums[i2 + 1] = cnums[i2]
            i2 -= 1

        cnums[i2 + 1] = cNum
    return(cnums)

def descending(nums):

    cnums = copy.copy(nums)

    for i1 in range(1, len(cnums)):
        i2 = i1 - 1
        cNum = cnums[i1]

        while cnums[i2] < cNum and i2 >= 0:
            cnums[i2 + 1] = cnums[i2]
            i2 -= 1

        cnums[i2 + 1] = cNum
    return(cnums)

def minmax(nums):
    print('sorted number by ASC:', ascending(nums))
    print('sorted number by DSC:', descending(nums))
    print(f'minNumber \t : \t {ascending(nums)[0]}\nmaxNumber \t : \t {ascending(nums)[-1]}')