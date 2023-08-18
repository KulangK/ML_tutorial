class RankDeviation:
    def __init__(self, mss, ess):
        self.midStuScors = mss              # list 받아옴
        self.endStuScors = ess              # list 받아옴
        self.midRanks = [0 for i in range(len(mss))]    # 위 list로 만들어지는 list
        self.endRanks = [0 for i in range(len(mss))]
        self.rankDeviation = [0 for i in range(len(mss))]

    def setRank(self, ss, rs):              # rank setting
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1

    def setMidRank(self):
        self.setRank(self.midStuScors, self.midRanks) # 생성자에서 만들어진 list를
                                                      # setRank에 집어넣는 역할
    def getMidRank(self):
        return self.midRanks

    def setEndRank(self):
        self.setRank(self.endStuScors, self.endRanks)

    def getEndRank(self):
        return self.endRanks

    def printRankDeviation(self):
        for idx, mRank in enumerate(self.midRanks):     # midRanks list 이용하여
            deviation = mRank - self.endRanks[idx]      # deviation 만드는 작업

            if deviation > 0:
                deviation = '↑' + str(abs(deviation))    # abs() >> absolute 값
            elif deviation < 0:
                deviation = '↓' + str(abs(deviation))
            else:
                deviation = '=' + str(abs(deviation))

            print(f'mid_rank: {mRank} \t end_rank: {self.endRanks[idx]} \t Deviation: {deviation}')
