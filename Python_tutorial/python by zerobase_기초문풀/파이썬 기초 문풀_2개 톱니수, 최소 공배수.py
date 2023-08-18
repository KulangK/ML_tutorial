gearA = int(input('기어 A 톱니 수 입력: '))
gearB = int(input('기어 B 톱니 수 입력: '))
i = 0

while 1:
    i += 1
    if i % gearA == 0 and i % gearB == 0:
        gearDouble = i
        break

print('최초 만나는 톱니수 (최소 공배수): {}톱니'.format(gearDouble))
print('기어 A 회전수: {}회전'.format(int(gearDouble / gearA)))
print('기어 B 회전수: {}회전'.format(int(gearDouble / gearB)))

""" 해설
gearAcount = ~~ 톱니수
gearBcount = ~~ 톱니수

gearA = 0
gearB = 0
leastNum = 0
flag = True

while flag:
    if gearA != 0:
        if gearA != leastNum:
            gearA += gearAcount
        else:
            flag = False
    else:
        gearA += gearAcount
    if gearB != 0 and gearB % gearAcount == 0:
        leastNum = gearB
    else:
        gearB += gearBcount

print~~~~

"""