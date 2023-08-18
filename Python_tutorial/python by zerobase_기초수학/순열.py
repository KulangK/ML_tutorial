#nPr 의 경우, n! / (n-r)! 이므로, 결과는 n~n-r 까지 곱한 수임

inputN = int(input('순열의 n 입력: '))
inputR = int(input('순열의 r 입력: '))

n = 1
for i in range(inputN, (inputN-inputR), -1):
    n *= i

print('{}P{} = {}'.format(inputN, inputR, n))


# 원순열: 시작과 끝의 구분이 없는 순열 (조합과 비슷해보이지만, 원으로 나열했을때 같은것을 제외하는 순열)
# 공식: n! / n  = (n-1)!
# e.g. n명의 인원이 원탁 테이블에 앉는 순서 계산  >>  팩토리얼 응용하면 easy