# 197개의 빵, 152개의 우유, 17명의 학생
# 학생 1명 당 받게 되는 빵과, 우유 개수 확인
# 남는 빵과 우유 개수도 확인

stu = 17
bread = 197
milk = 152

stuB = divmod(197, 17)
stuM = divmod(152, 17)

print('학생 1명 당 갖게 되는 빵의 개수: {}'.format(stuB[0]))
print('학생 1명 당 갖게 되는 우유 개수: {}'.format(stuM[0]))

print('남는 빵 개수: {}'.format(stuB[1]))
print('남는 우유 개수: {}'.format(stuM[1]))
