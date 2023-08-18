def triArea(n1, n2):
    area = n1 * n2 * 0.5
    return round(area, 1)

def recArea(n1, n2):
    area = n1 * n2
    return round(area, 1)

def area(n1, n2):
    tri = triArea(n1, n2)
    rec = recArea(n1, n2)

    print(f'삼각형 넓이: {tri}')
    print(f'사각형 넓이: {rec}')
