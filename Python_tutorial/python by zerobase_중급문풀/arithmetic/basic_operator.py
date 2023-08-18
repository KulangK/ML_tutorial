def addcal(n1, n2):
    return n1 + n2

def subcal(n1, n2):
    return n1 - n2

def mulcal(n1, n2):
    return n1 * n2

def divcal(n1, n2):
    return n1 / n2

def bopercal(n1, n2):
    print(f'{n1} + {n2} = {addcal(n1, n2)}')
    print(f'{n1} - {n2} = {subcal(n1, n2)}')
    print(f'{n1} * {n2} = {mulcal(n1, n2)}')
    print(f'{n1} / {n2} = {divcal(n1, n2)}')