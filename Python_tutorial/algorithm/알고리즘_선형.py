# 선형 검색 알고리즘

data = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {data}')
print(f'data length: {len(data)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchDataIdx = -1

n = 0
while 1:
    if n == len(data):
        searchDataIdx = -1
        break

    elif data[n] == searchData:
        searchDataIdx = n
        break

    n += 1

print(f'searchDataIdx = {searchDataIdx}')