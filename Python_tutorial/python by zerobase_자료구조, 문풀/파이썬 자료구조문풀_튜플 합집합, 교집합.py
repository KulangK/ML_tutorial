tuple1 = (1, 3, 2, 6, 12, 5, 7, 8)
tuple2 = (0, 5, 2, 9, 8, 6, 17, 3)

inter = []
uni = []

for x in tuple1:
    if x in tuple2:
        inter.append(x)

for x in tuple1:
    uni.append(x)

for x in tuple2:
    if x not in uni:
        uni.append(x)

print(f'합집합: {sorted(uni)}')
print(f'교집합: {sorted(inter)}')