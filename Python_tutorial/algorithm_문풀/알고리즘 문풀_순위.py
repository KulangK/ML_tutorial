# 숫자로 이루어진 리스트에서 아이템의 순위 출력, 순위에 따라 아이템을 정렬하는 프로그램
# 리스트는 50부터 100까지 난수 20개 이용

import random as rd

nums = rd.sample(range(50, 101), 20)

ranks = [0 for i in range(len(nums))]   # 0으로 대상 데이터 갯수만큼 리스트 만들어줌

for idx, num1 in enumerate(nums):       # random으로 뽑힌 20개의 숫자를 enumerate()
    for num2 in nums:                   # nums의 num1이라는 숫자와 그 인덱스를 참조하면서
        if num1 < num2:                 # nums의 모든 숫자들과 비교
            ranks[idx] += 1             # num1보다 큰 숫자의 갯수에 따라 랭크를 정하는 것임

print(nums)
print(ranks)

sortedNums = [0 for n in range(len(nums))]  # 0 value의 아이템을 원본 데이터 갯수만큼 만들어줌
                                            # idx 맞추려고 하는 것임
print(sortedNums)
for idx, num1 in enumerate(ranks):          # ranks num1 = 순위
    sortedNums[num1] = nums[idx]            # ranks idx = nums idx 참조
print(sortedNums)