class NotPrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 소수가 아닙니다.')   # super().__init__() 이 아니라 print()를 쓰면 숫자가 한 번 더 출력됨.

class PrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 소수입니다.')       # super().__init__() 이 아니라 print()를 쓰면 숫자가 한 번 더 출력됨.

def isPrime(number):
    flag = True
    for i in range (2, number):                    # number + 1을 끝으로 하게 되면, 자기 자신으로 나눠서 나머지가 0 이므로
                                                   # 모든 숫자가 소수가 아닌 것으로 됨.
        if number % i == 0:
            flag = False
            raise NotPrimeException(number)        # raise Exception 은 저절로 break를 하게됨.

    if flag:
       raise PrimeException(number)
