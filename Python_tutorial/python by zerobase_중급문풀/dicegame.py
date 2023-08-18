import random as rd

class Dice:
    def __init__(self):
        self.dice = {}

    def setCnum(self):
        print('[Dice] setCnum()')
        x = rd.randint(1, 6)
        self.dice['com'] = x

    def setUnum(self):
        print('[Dice] setUnum()')
        x = rd.randint(1, 6)
        self.dice['user'] = x

    def startGame(self):
        print('[Dice] startGame')
        self.setCnum()
        self.setUnum()
        self.printResult()

    def printResult(self):
        print('[Dice] printResult')
        com = self.dice['com']
        user = self.dice['user']
        if com == user:
            print(f'컴퓨터 vs 유저 : {com} vs {user} >> 무승부!!')
        elif com > user:
            print(f'컴퓨터 vs 유저 : {com} vs {user} >> 컴퓨터 승!!')
        else:
            print(f'컴퓨터 vs 유저 : {com} vs {user} >> 유저 승!!')

