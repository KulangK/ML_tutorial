import random as rd
import primeexception as pm

primeNumbers = []
n = 0                                   # 소수가 10개 될 때까지 생성하라는 것으로 문제르 잘못 읽었음.
while n < 10:
    rn = rd.randint(1, 1000)
    if rn not in primeNumbers:
        try:
            pm.isPrime(rn)

        except pm.NotPrimeException as e:
            print(e)
            continue

        except pm.PrimeException as e:
            print(e)
            primeNumbers.append(rn)

    else:
        print(f'{rn} is overlap number.')
        continue

    n += 1
print(sorted(primeNumbers))