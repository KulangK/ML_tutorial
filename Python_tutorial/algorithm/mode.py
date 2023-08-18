class ModeAlgorithm:
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0

    def getMaxIdxandNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0

        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i

    def getMaxNum(self):
        return self.maxNum

    def getMaxNumIdx(self):
        return self.maxNumIdx

    def indexing(self):
        indexes = [0 for i in range(self.maxNum + 1)]
        for n in self.nums:
            indexes[n] = indexes[n] + 1
        return indexes

nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
print('nums:', nums)

maxAlo = ModeAlgorithm(nums)                # 분석 데이터로 모드 객체 형성
maxAlo.getMaxIdxandNum()                    # 모드 객체에서 분석 데이터 최댓값과 인덱스 구함
maxNum = maxAlo.getMaxNum()                 # 최댓값 반환
maxNumIdx = maxAlo.getMaxNumIdx()           # 최댓값의 인덱스 반환

print(f'maxNum = {maxNum}, maxNumIdx = {maxNumIdx}')

indexes = maxAlo.indexing()             # 인덱스 리스트 형성
print('index list:', indexes)

modeAlo = ModeAlgorithm(indexes)        # 인덱스 리스트로 모드 객체 형성
modeAlo.getMaxIdxandNum()               # 모드 객체에서 최빈값과 빈도수 구함
modeMax = modeAlo.getMaxNum()           # 빈도수 반환
modeMaxIdx = modeAlo.getMaxNumIdx()     # 최빈값 반환
print(f'mode frequency = {modeMax}, modeValue = {modeMaxIdx}')

# class내에서 위와 같은 순서로 메서드 하나를 짜면 최댓값, 인덱스, 최빈값, 빈도수 모두 구할 수 있음