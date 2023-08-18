nums = [10, 2, 7, 21, 0]

print(f'unsorted numbers: {nums}', 'i', 'j', 'length - i')

length = len(nums) - 1
for i in range(length):
    for j in range(length - i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j] # 두 값의 자리를 바꾸는 파이썬의 방법
        print('sorting process: ', nums, i, j, length - i)
    print()

print(f'sorted numbers: {nums}')