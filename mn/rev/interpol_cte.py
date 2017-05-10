def f(x):
    return {
        0:1,
        1:-3,
        2:7,
        3:2,
        4:0,
    }.get(x,None)

x0 = float(input("x: "))

print('%.6f' % f(round(x0,0)))