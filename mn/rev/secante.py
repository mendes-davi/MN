def g(x):
    return x**4 - 10*x**3 + 8*x

x0 = float(input("a: "))
x1 = float(input("b: "))

xa, xb = x0, x1
ga, gb = g(x0), g(x1)

for i in range(0,10):
    xa, xb = xb, (xa * gb - xb * ga) / (gb - ga)
    ga, gb = gb, g(xb)
    print("f(%.6f) = %.6f" % (xb,gb))
