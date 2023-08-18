nums = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 20, 21, 23, 24, 27, 28]

searchData = int(input('input search number: '))
searchDataIdx = -1

staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

print(f'staIdx: {staIdx}, endIdx: {endIdx}\nmidIdx: {midIdx}, midVal: {midVal}')

while searchData <= nums[len(nums)-1] and searchData >= nums[0]:
    if searchData == nums[len(nums)-1]:
        searchDataIdx = len(nums) - 1
        break

    if staIdx + 1 == endIdx:
        if nums[staIdx] != searchData and nums[endIdx] != searchData:
            searchData = -1
            break

    elif searchData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'+staIdx: {staIdx}, endIdx: {endIdx}\n+midIdx: {midIdx}, midVal: {midVal}')

    elif searchData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'-staIdx: {staIdx}, endIdx: {endIdx}\n-midIdx: {midIdx}, midVal: {midVal}')

    elif searchData == midVal:
        searchDataIdx = midIdx
        break

print(f'nums: {nums}')
print('>>> Search Results <<<')
print(f'Search result index: {searchDataIdx}')

if searchDataIdx == -1:
    print(f'Search result number: none')
else:
    print(f'Search result number: {nums[searchDataIdx]}')

