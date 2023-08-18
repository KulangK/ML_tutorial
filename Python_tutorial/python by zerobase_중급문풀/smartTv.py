class NormalTv:
    def __init__(self, i=32, c='black', r='full-HD'):       # class의 속성 부분
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTv = 'off'
        self.aiTv = 'off'

    def turnOn(self):
        print('turn On')

    def turnOff(self):
        print('turn Off')

    def printTvInfo(self):
        print(f'inch = {self.inch}inch')
        print(f'color = {self.color}')
        print(f'resolution = {self.resolution}')
        print(f'smartTv = {self.smartTv}')
        print(f'aiTv = {self.aiTv}')


class Tv4K(NormalTv):
    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)                          # 상속받은 상위 class의 속성 초기화

    def setSmartTv(self, s):                               # NormalTv class를 상속했기에, 기본적으로 off 임
        self.smartTv = s                                   # setSmartTv('on')을 적어주면, on이라는 문자열이 들어가게 됨.


class Tv8k(NormalTv):
    def __init(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTv(self, s):
        self.smartTv = s

    def setAiTv(self, a):
        self.aiTv = a