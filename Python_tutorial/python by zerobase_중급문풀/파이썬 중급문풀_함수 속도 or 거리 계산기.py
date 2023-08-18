def getDistances(x, y, z):
    return round(x * (y + z/60), 1)

def getTime(x, y):
    hr = int(x // y)
    min = int(((x / y) - hr) * 60)
    return [hr, min]


# print('-' * 60)
# s = float(input('속도(km/h) 입력: '))
# h = float(input('시간(h) 입력: '))
# m = float(input('시간(m) 입력: '))
# d = getDistances(s, h, m)
# print(f'{s}(km/h)속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리: {d}(km)')
# print('-' * 60)

print('-' * 60)
d = float(input('이동한 거리(km) 입력: '))
s = float(input('속도(km/h) 입력: '))
t = getTime(d, s)
print(f'{s}(km/h)속도로 {d}(km)만큼 이동하는데 걸리는 시간: {t[0]}시간 {t[1]}분')
print('-' * 60)

