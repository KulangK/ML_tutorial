class MinAlgorithm:
    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0

    def getMaxNum(self):
        self.minNum = self.nums[0]

        for n in self.nums:
            if self.minNum > n:
                self.minNum = n

        return self.minNum
