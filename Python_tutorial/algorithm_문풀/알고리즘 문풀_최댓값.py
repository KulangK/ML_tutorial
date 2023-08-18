import random as rd

nums = [rd.randint(1, 50) for n in range(30)]

print(nums)

max = 0
for num in nums:
    if max < num:
        max = num

print(f'max num: {max}')
print(f'max num cnt: {nums.count(max)}')
