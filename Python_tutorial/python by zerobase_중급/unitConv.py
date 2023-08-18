def cmToMm(x):
    return(round(x * 10, 2))

def cmToInch(x):
    return(round(x * .393, 3))

def cmToM(x):
    return(round(x / 100, 4))

def cmToFt(x):
    return(round(x * 0.032, 3))

if __name__ == '__main__':
    print(f'10cm: {cmToMm(10)}mm')
    print(f'10cm: {cmToInch(10)}inch')
    print(f'10cm: {cmToM(10)}m')
    print(f'10cm: {cmToFt(10)}ft')
