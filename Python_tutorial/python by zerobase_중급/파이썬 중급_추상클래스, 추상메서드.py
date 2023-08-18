from abc import ABCMeta
from abc import abstractmethod

class Calculator(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass

class NewCalculator(Calculator):

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

    def mod(self, n1, n2):
        return n1 % n2

    def flo(self, n1, n2):
        return n1 // n2

cal = NewCalculator()


print(cal.sub(10, 5))
print(cal.mul(10, 5))
print(cal.div(10, 5))
print(cal.mod(10, 5))
print(cal.flo(10, 5))