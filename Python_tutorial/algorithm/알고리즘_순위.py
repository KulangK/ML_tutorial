import random as rd

nums = rd.sample(range(50,101), 20)
ranks = [0 for i in range(20)]

print(f'nums: {nums}')
print(f'ranks: {ranks}')

for idx, num1 in enumerate(nums):       # random으로 뽑힌 20개의 숫자를 enumerate()
    for num2 in nums:                   # nums의 num1이라는 숫자와 그 인덱스를 참조하면서
        if num1 < num2:                 # nums의 모든 숫자들과 비교
            ranks[idx] += 1             # num1보다 큰 숫자의 갯수에 따라 랭크를 정하는 것임

print(f'nums: {nums}')
print(f'ranks: {ranks}')

for idx, num in enumerate(nums):
    print(f'num: {num} \t rank: {ranks[idx] + 1}')