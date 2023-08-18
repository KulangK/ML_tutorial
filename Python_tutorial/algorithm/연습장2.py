def data_type(n):
    if type(n) == int or type(n) == float or type(n) == str:
        print(types(n))

    elif type(n) == list or types(n) == tuple:
        if len(n) > 1:
            print(f'{types(n)}, ', end='')
            listType(n)
        else:
            print(types(n))

    elif type(n) == dict:
        print(f'{types(n)}, ', end='')
        dictType(n)
def listType(n):
    print('<', end='')
    for idx, val in enumerate(n):
        if idx == len(n)-1:
            print(types(val), end='')
            continue

        print(types(val), end=', ')

        if type(val) == list or type(val) == tuple:
            listType(val)
            print(', ', end= '')

    print('>', end='')

def dictType(n):
    print('<', end='')
    for idx, key in enumerate(list(n.keys())):
        if idx == len(n)-1:
            print(f'{types(key)} : {types(n[key])}', end='')
            continue
        print(f'{types(key)} : {types(n[key])}, ', end='')
    print('>', end='')

def types(n):
    if type(n) == int:
        return 'int'
    elif type(n) == float:
        return 'float'
    elif type(n) == list:
        return 'list'
    elif type(n) == str:
        return 'string'
    elif type(n) == dict:
        return 'dict'
    elif type(n) == tuple:
        return 'tuple'


x = [2, 3, [2, 3], "Hello"]
y = {1:2, 3:4, 5:6, 7:[1, 2, 3]}
z = [[2, 3, 4], 1, [2], (2, 3), [4, 5, 6, 7], 'ABCaadadad']
w = [2, 3, [2, 3], [1, 2, 3, [123123,123], 4]]
a = {'a':2, 2:3, 3:4, 4:5}

data_type(a)