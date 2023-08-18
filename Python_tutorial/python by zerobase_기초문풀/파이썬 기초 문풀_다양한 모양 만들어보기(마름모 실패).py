# *표로 다양한 모양 만들어보기
user = int(input('최대 별 갯수 입력: '))

# (1)_위가 좁은 삼각형
# for i in range(1, user+1):
#       print('*' * i)


# (2)_아래가 좁은 삼각형
# for i in range(user, 0, -1):
#       print('*' * i)


# (3)_(1) 의 좌우 반전
# for i1 in range(1, user+1):
#       for i2 in range(user-i1):     # max가 user - i1 이기 때문에, i1이 늘어남에 따라 점점 줄어듦
#             print(' ',end='')
#       for i3 in range(i1):
#             print('*', end='')
#       print()


# (4)_(2) 의 좌우반전
# for i1 in range(user, 0, -1):
#       for i2 in range(user-i1):     # max가 user - i1 이기 때문에, i1이 줄어듦에 따라 늘어남 (여기는 역순으로 진행)
#             print(' ',end='')
#       for i3 in range(i1):
#             print('*', end='')
#       print()


# (5) 우 하향 별똥별
# for i in range(1, user+1):
#       for j in range(1, user+1):
#             if j == i:
#                   print('*', end='')
#             else:
#                   print(' ', end='')
#       print()


# (6) 좌 하향 별똥별
# for i in range(user, 0, -1):
#       for j in range(1, user+1):
#             if j == i:
#                   print('*', end='')
#             else:
#                   print(' ', end='')
#       print()


# (7)_(1), (2)를 위 아래로 합친 이등변 삼각형
# for i in range(1, 2*user+1):
#       if i < user:
#             for j in range(i):
#                   print('*', end='')
#       else:
#             for j in range(2*user-i):
#                   print('*', end='')
#       print()


# (8) 마름모 모양