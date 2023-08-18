sales = [12000, 13000, 12500, 11000, 10500,
         98000, 91000, 91500, 10500, 11500, 12000, 12500]

def difference(list):
    if len(list) <2:
        return
    print(f'sales: {list}')
    x = list[1] - list[0]
    if x > 0:
        x = '+' + str(x)
    del list[0]
    print(f'매출 증감액: {x}')
    difference(list)

difference(sales)