# 알파벳 문자와 정수 아이템의 순위 출력
# 알파벳은 아스키 코드 값 이용

import random as rd

nums = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']
ascIIdata = []

for i, num in enumerate(nums):
    if type(num) == str:
        ascIIdata.append(ord(num))
    else:
        ascIIdata.append(num)

print(ascIIdata)

ranks = [1 for i in range(len(ascIIdata))]   # 0으로 대상 데이터 갯수만큼 리스트 만들어줌

for idx, num1 in enumerate(ascIIdata):       # random으로 뽑힌 20개의 숫자를 enumerate()
    for num2 in ascIIdata:                   # nums의 num1이라는 숫자와 그 인덱스를 참조하면서
        if num1 < num2:                 # nums의 모든 숫자들과 비교
            ranks[idx] += 1             # num1보다 큰 숫자의 갯수에 따라 랭크를 정하는 것임

print(nums)
print(ranks)
