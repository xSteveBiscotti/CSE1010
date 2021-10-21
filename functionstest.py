def outerfunction():
    num = 1
    y = num * 2
    x = 3
    z = 15
    return num, y, x, z


def innerfunction():
    test = outerfunction()
    print(test[-1])

innerfunction()
    
