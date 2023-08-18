nums = [4, 2, 5, 1, 3]

for i in range(len(nums)-1):                # 모든 숫자를 비교 대상 군(1)에 넣음
    minIdx = i

    for j in range(i + 1, len(nums)):       # i를 제외한 나머지 모든 숫자를 비교 대상 군 (2)에 넣음
        if nums[minIdx] > nums[j]:          # 비교할 때마다 가장 작은 숫자의 인덱스를 minIdx에 초기화
            minIdx = j
        print('processing inside for', nums, f'i: {i}, j: {j}, minIdx: {minIdx}')
    nums[i], nums[minIdx] = nums[minIdx], nums[i]   # 내부 for문 종료 후 index i에 최소 값 적용
    print('end of cycle', nums)
print(nums)