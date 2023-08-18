# 선형 검색
# 1~20 정수 중 난수 10개
# 검색 과정 로그로 출력
# 검색 성공시 정수 인덱스 출력, 없으면 -1 출력 .find() 함수

import random as rd

rdList = rd.sample(range(1, 21), 10)

userFind = int(input('찾으려는 숫자 입력: '))

print(rdList)
print(f'Search Number: {userFind}')

searchIndex = -1
n = 0
while 1:
    if n == len(rdList):
        print('Search Fail')
        print(f'Search result Index: {searchIndex}')
        print(f'>>> Search Results <<<')
        print(f'Search result index: {searchIndex}')
        print(f'Search result number: {-1}')
        break

    elif rdList[n] == userFind:
        searchIndex = n
        print('Search Success')
        print(f'Search result Index: {searchIndex}')
        print(f'>>> Search Results <<<')
        print(f'Search result index: {searchIndex}')
        print(f'Search result number: {rdList[n]}')
        break

    n += 1