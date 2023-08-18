import random as rd
import sortMod as sm

height = []

for n in range(20):
    height.append(rd.randint(170, 185))

print(f'Unsorted heights: {height}')

sortedH = sm.bubbleSort(height)

print(f'Sorted heights: {sortedH}')

# 원본까지 바꾸길 원하면
# sm.bubbleSort(height, deepCopy = False) 사용하면 됨.