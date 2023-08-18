employee = [25, 27, 27, 24, 31, 34, 33, 31, 29, 25, 45, 37, 38, 46, 47, 22, 24,
            29, 33, 35, 27, 34, 37, 40, 42, 29, 27, 25, 26, 27, 31, 31, 32, 38,
            25, 27, 28, 40, 41, 34]

print(f'employee count: {len(employee)}')

min = employee[0]
max = 0

for i in employee:
    if min > i:
        min = i
    if max < i:
        max = i

freq = [0 for n in range(min, max+1)]

for n in employee:
    freq[n-min] += 1

print(f'max age: {max}세')
print(f'min age: {min}세')

n = '1'

while 1:
    max = 0
    maxIdx = 0
    for idx, num in enumerate(freq):
        if max < num:
            max = num
            maxIdx = idx
    if max == 0:
        break
    print(f'[{n.zfill(3)}] {maxIdx+min}세 빈도수: {max}', end=' ')

    n = int(n); n += 1; n = str(n)

    print('+' * max)

    freq[maxIdx] = 0

