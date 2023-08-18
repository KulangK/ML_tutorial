nums = [19, 10, 3, 5, 13, 4, 12, 17, 8, 16]

for i1 in range(1, len(nums)):
    i2 = i1 - 1
    cNum = nums[i1]
    print(f'{nums}, i1 = {i1}, for start')

    while nums[i2] > cNum and i2 >= 0:
        nums[i2 + 1] = nums[i2]
        i2 -= 1
        print(nums, 'while')

    nums[i2 + 1] = cNum
    print(f'{nums}, i1 = {i1}, for end')
print(f'nums: {nums}')
