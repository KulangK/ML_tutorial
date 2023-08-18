def testpass(scores):
    tot = 0
    totAvg = 0
    n = 0
    for i, score in enumerate(scores):
        if scores[i] >= 60:
            print(f'{scores[i]}: Pass')
        elif scores[i] < 40:
            print(f'{scores[i]}: Fail')
            n += 1
        else:
            print(f'{scores[i]}: Pass')
        tot += scores[i]
    totAvg = tot / len(scores)
    print(f'총점: {tot}')
    print(f'평균: {totAvg}')
    if n == 0 and totAvg >= 60:
        print('Final Pass')
    else:
        print('Final Fail')
