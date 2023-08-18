import random as rd

list = rd.sample(range(1,10), 4)
result = []

for n1 in list:
    for n2 in list:
        if n1 == n2:
            continue

        result.append([n1, n2])

print(f'numbers: {list}')
print(f'combination of two different numbers: {result}')