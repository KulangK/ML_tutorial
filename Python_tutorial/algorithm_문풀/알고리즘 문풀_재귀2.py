# 사용자가 정수 두개 입력시, 작은 정수와 큰 정수 사이의 모든 정수의 합을 구하는 프로그램

class NumsSum:
    def __init__(self, num1, num2):
        self.bigNum = 0
        self.smallNum = 0
        self.setN1N2(num1, num2)

    def setN1N2(self, num1, num2):
        self.bigNum = num1
        self.smallNum = num2

        if num1 < num2:
            self.bigNum = num2
            self.smallNum = num1

    def addNum(self, n):
        if n <= 1:
            return n

        return n + self.addNum(n-1)

    def sumBetweenNums(self):
        return self.addNum(self.bigNum -1) - self.addNum(self.smallNum)



num1 = int(input('input number1: '))
num2 = int(input('input number2: '))

ns = NumsSum(num1, num2)
result = ns.sumBetweenNums()
print(result)