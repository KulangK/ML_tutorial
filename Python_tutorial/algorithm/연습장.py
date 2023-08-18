# 문제 2번

def data_type(n):
    if type(n) == int or type(n) == float or type(n) == str:
        print(types(n))

    elif type(n) == list or types(n) == tuple:
        if len(n) > 1:
            print(f'{types(n)}, <', end='')
            listType(n)
        else:
            print(types(n))

# dict일 경우에 대한 수 만들어야함 (key:value)

def listType(n):
    for idx, val in enumerate(n):
        if type(val) == list or type(val) == tuple:
            if len(val) > 1:
                print(f'{types(val)}', end='')
                listType(val)
                print(', ', end='')
            else:
                print(f', {types(val)}, ', end='')
                print(f'<{types(val[0])}>, ', end='')
        elif idx == 0:
            print(f', <{types(val)} ', end='')

        elif idx == len(n)-1:
            print(f', {types(val)}>', end='')

        else:
            print(f'{types(val)}', end='')
    print('', end='')



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
data_type(w)
# 해결 안된 경우의 수 (a) 리스트가 첫번째 올 때, (b) 리스트 원소가 1개일 때