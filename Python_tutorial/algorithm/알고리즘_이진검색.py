nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f'datas: {nums}')
print(f'data length: {len(nums)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchDataIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchData <= nums[len(nums)-1] and searchData >= nums[0]:
    if searchData == nums[len(nums)-1]:
        print(f'endIdx: {endIdx}')
        print(f'endVal: {nums[len(nums)-1]}')
        break

    if searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')

    elif searchData == midVal:
        searchDataIdx = midIdx
        break