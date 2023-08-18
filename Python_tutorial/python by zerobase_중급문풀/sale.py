def itemSale(items):
        if len(items) >= 5:
                return 25
        elif len(items) == 4:
                return 20
        elif len(items) == 3:
                return 15
        elif len(items) == 2:
                return 10
        else:
                return 5