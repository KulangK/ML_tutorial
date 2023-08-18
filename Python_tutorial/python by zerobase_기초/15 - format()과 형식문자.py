radius = float(input('반지름 입력 : '))
pi = float(input('원주율 입력 : '))

r = 'radius'
p = 'pi'
print('{0} : %.1f\n{1} : %.6f\n{0} : %.1f, {1} : %.6f'.format(r, p) %(radius, pi, radius, pi))
print('{0} : %.6f, {1} : %.6f\n{0} : %.2f, {1} : %.2f'.format(r, p) %(radius, pi, radius, pi))

circArea = radius**2 * pi
circCircum = radius*2 * pi

print('원의 넓이: %.3f, 원의 둘레: %.3f' %(circArea, circCircum))