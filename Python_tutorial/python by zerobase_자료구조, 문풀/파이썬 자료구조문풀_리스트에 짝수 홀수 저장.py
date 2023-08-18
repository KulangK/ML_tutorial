import random as rd

even = []
odd = []

for x in rd.sample(range(1, 101), 10):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(f'짝수: {even} 짝수 개수: {len(even)}')
print(f'홀수: {odd} 홀수 개수: {len(odd)}')