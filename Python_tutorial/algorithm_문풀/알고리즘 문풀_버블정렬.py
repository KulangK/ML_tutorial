import random as rd

def ASCbubble(nums):
    print(f'unsorted numbers: {nums}', 'i', 'j', 'length - i')

    length = len(nums) - 1
    for i in range(length):                         # i는 밑줄에서 어느자리까지 비교할 것인지 기준 제공
        for j in range(length - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] # 두 값의 자리를 바꾸는 파이썬의 방법
            print('sorting process: ', nums, i, j, length - i)
        print()

    print(f'sorted numbers: {nums}')

def DSCbubble(nums):
    print(f'unsorted numbers: {nums}', 'i', 'j', 'length - i')

    length = len(nums) - 1
    for i in range(length):                         # i는 밑줄에서 어느자리까지 비교할 것인지 기준 제공
        for j in range(length - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 두 값의 자리를 바꾸는 파이썬의 방법
            print('sorting process: ', nums, i, j, length - i)
        print()

    print(f'sorted numbers: {nums}')

nums = rd.sample(range(1, 21), 10)
ASCbubble(nums)
DSCbubble(nums)