# 보초법 선형검색 알고리즘

data = [3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
print(f'datas: {data}')
print(f'data length: {len(data)}')

searchData = int(input('찾으려는 숫자 입력: '))
searchDataIdx = -1

data.append(searchData)

n = 0
while 1:

    if data[n] == searchData:
        if n != len(data)-1:
            searchDataIdx = n
        break

    n += 1

print(f'searchDataIdx = {searchDataIdx}')