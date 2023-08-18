import random as rd
import sortingInsert as si

nums = []

for i in range(100):
    nums.append(rd.randint(1, 1000))

print(f'Unsorted number: {nums}')
si.minmax(nums)