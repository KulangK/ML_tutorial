cl1stu = int(input('학생 수 입력: ')) # 반 해당 전체 학생

cl1grp = int(input('한 모둠의 학생 수 입력: ')) # 반에서 운용할 모둠 수

cl1stugrp = divmod(cl1stu, cl1grp) # 결과는 tuple, (모둠 수, 남은 학생)

print('전체 학생 수: {}\n한 모둠 당 학생 수: {}'.format(cl1stu,cl1grp))
print('전체 모둠 수: {}\n남은 학생수: {}'.format(cl1stugrp[0],cl1stugrp[1]))

