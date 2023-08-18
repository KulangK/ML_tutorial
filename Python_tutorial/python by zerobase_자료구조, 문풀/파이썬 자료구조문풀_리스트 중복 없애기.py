import random as rd

list = []

for n in range(1, 100):
    list.append(rd.randint(1, 10))

print(list)

x = 0
while x < len(list):
    if list.count(list[x]) >= 2:
        del list[x]
        continue
    x += 1

print(list)