name = []

while len(name) < 5:
    x = input('친구 이름 입력: ')
    name.append(x)

print(f'친구들: {name}')
name.sort()
print(f'오름차순: {name}')
name.sort(reverse=True)
print(f'내림차순: {name}')