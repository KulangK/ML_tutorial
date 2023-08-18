import unitConv as uc

if __name__ == '__main__':
    userInput = float(input('길이 입력(cm): '))

    print(f'{userInput}cm = {uc.cmToMm(userInput)}mm')
    print(f'{userInput}cm = {uc.cmToInch(userInput)}inch')
    print(f'{userInput}cm = {uc.cmToM(userInput)}m')
    print(f'{userInput}cm = {uc.cmToFt(userInput)}ft')