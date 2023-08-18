import random
from time import sleep

class Car:
    def __init__(self, n = 'fire car', c = 'red', s = 200):
        self.cName = n
        self.cColor = c
        self.cSpeed = s
        self.distance = 0

    def printCarInfo(self):                       
        print(f'name: {self.cName}, color: {self.cColor}, speed: {self.cSpeed}')

    def controlSpeed(self):                       
        return random.randint(0, self.cSpeed)

    def getDistanceForHour(self):                 
        return self.controlSpeed() * 1            # 10초가 아니라 1시간으로 정정

class CarRacing:
    def __init__(self):
        self.cars = []
        self.rankings = []

    def startRacing(self):                        # 10바퀴를 상정하고 진행
        for i in range(10):
            print(f'Racing: {i + 1}바퀴')
            for car in self.cars:
                car.distance += car.getDistanceForHour()

            sleep(1)                              # 일부러 결과 출력을 늦추기 위함
            self.printCurrentCarDistance()

    def printCurrentCarDistance(self):
        for car in self.cars:
            print(f'{car.cName}: {car.distance}\t\t', end = '')
        print()

    def addCar(self, c):
        self.cars.append(c)

