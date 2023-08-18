import lotto as lt

lottoNum = []

while 1:
        userInput = int(input('번호(1~45) 입력: '))
        if userInput > 45 or userInput == 0:
                print('입력한 숫자가 잘못되었습니다. 다시 입력하세요.')
                continue
        lottoNum.append(userInput)
        if len(lottoNum) == 6:
                break

lt.lottoCom(lottoNum)