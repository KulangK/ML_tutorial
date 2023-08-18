import random as rd

nums = [rd.randint(1, 50) for n in range(30)]

print(nums)

min = nums[0]
for num in nums:
    if min > num:
        min = num

print(f'min num: {min}')
print(f'min num cnt: {nums.count(min)}')
