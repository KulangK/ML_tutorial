class midExam:
    def __init__(self, t1, t2, t3):
        self.midKor = t1
        self.midEng = t2
        self.midMat = t3

    def printScores(self):
        print(f'midKor: {self.midKor}')
        print(f'midEng: {self.midEng}')
        print(f'midMat: {self.midMat}')

    def printInfo(self):
        tot = self.midKor + self.midEng + self.midMat
        avg = round(tot / 3, 2)
        print(f'Total Mid score: {tot}')
        print(f'Average Mid score: {avg}')

class endExam(midExam):
    def __init__(self, t1, t2, t3, t4, t5, t6):

        super().__init__(t1, t2, t3)

        self.endKor = t4
        self.endEng = t5
        self.endMat = t6

    def printScores(self):
        super().printScores()
        print(f'endKor: {self.endKor}')
        print(f'endEng: {self.endEng}')
        print(f'endMat: {self.endMat}')

    def printInfo(self):
        tot = self.endKor + self.endEng + self.endMat
        avg = round(tot / 3, 2)
        super().printInfo()
        print(f'Total End score: {tot}')
        print(f'Average End score: {avg}')

kate = endExam(51, 46, 78, 81, 87, 95)

kate.printScores()

kate.printInfo()

