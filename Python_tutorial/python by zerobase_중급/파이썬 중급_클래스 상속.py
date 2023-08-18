class CalAddSub:
    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

class CalMulDiv(CalAddSub):
    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

cal = CalMulDiv()

userInput1 = int(input('산술할 첫 번째 숫자 입력: '))
userInput2 = int(input('산술할 두 번째 숫자 입력: '))

print(f'cal.add : {cal.add(userInput1, userInput2)}')
print(f'cal.sub : {cal.sub(userInput1, userInput2)}')
print(f'cal.mul : {cal.mul(userInput1, userInput2)}')
print(f'cal.div : {cal.div(userInput1, userInput2)}')
