scores = []

def addScore(*s):
    scores.extend(s)

def getTotScore():
    tot = 0
    for i in scores:
        tot += i
    return tot

def getAvgScore():
    avg = getTotScore() / len(scores)
    return round(avg, 2)
