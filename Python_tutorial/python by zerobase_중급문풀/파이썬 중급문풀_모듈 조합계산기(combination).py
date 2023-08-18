# 조합 = combination

# 순열은 n개 중 r개를 뽑아 나열하는 것으로 순서가 중요
# 조합은 n개 중 r개를 뽑는 그 자체의 조합 (순서 x)
# nCr = nPr / r! = n! / (n-r)!r!

import combination as co

nums = co.setCombination()

co.getCombination(nums)

co.getCombinationGroups(nums)