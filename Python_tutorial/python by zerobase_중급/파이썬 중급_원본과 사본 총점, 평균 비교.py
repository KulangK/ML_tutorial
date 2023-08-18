plaOrSco = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
plaCopSco = plaOrSco.copy()

plaOrSco.sort() # list 내 값 순서대로 정렬
plaCopSco.sort()

plaCopSco.pop(0) # list 내 첫번째 인덱스 값 제거
plaCopSco.pop() # list 내 마지막 인덱스 값 제거

print(f'plaOrSco: {plaOrSco}')
print(f'plaCopSco: {plaCopSco}')

oriTot = round(sum(plaOrSco), 2)
oriAvg = round(oriTot / len(plaOrSco), 2)
print(f'Original Total: {oriTot}')
print(f'Original Average: {oriAvg}')

copTot = round(sum(plaCopSco), 2)
copAvg = round(copTot / len(plaCopSco), 2)
print(f'Copy Total: {copTot}')
print(f'Copy Average: {copAvg}')

print(f'oriAvg - copAvg: {oriAvg - copAvg}')
