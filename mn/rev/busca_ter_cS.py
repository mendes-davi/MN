def f(x):
    return (x**2 - 1)*(x**2 + 1) + x

x1 = float(input("a: "))
x2 = float(input("b:"))


for i in range(0,10):
    print("%.6f %.6f" % (x1,x2))
    xa, xb = x1 + (x2 - x1) / 3, x1 + (x2 - x1) * 2 / 3
    fa, fb = f(xa), f(xb)
    if fa > fb:
        x1 = xa
    else:
        x2 = xb