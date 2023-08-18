def modcal(n1, n2):
    return n1 % n2

def fldivcal(n1, n2):
    return n1 // n2

def powcal(n1, n2):
    return n1 ** n2

def dopercal(n1, n2):
    print(f'{n1} % {n2} = {modcal(n1, n2)}')
    print(f'{n1} // {n2} = {fldivcal(n1, n2)}')
    print(f'{n1} ** {n2} = {powcal(n1, n2)}')
