import recursion
import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 100))

asc = recursion.mSort(nums)
dsc = recursion.mSort(nums, asc = False)

print('Unsorted Nums: {}'.format(nums))
print('merge sorted Nums by ASC: {}'.format(asc))
print('merge sorted Nums by DSC: {}'.format(dsc))

