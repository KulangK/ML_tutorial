import random as rd

nums = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
deviation = list(range(len(nums)))

sum = 0
max = 0

for num in nums:
    if max < num:
        max = num
    sum += num

avg = sum / len(nums)

for i in deviation:
    deviation[i] = round((nums[i] - avg), 1)

print(f'max result: {max}')
print(f'avg result: {avg}')
print(nums)
print(deviation)
