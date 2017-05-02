import  math

def g(x):
    return x*((x**2 + 3*x - 3)/(x**2 + 1))

x0 = float(input("a: "))
x1 = float(input("b: "))

g0, g1 = g(x0), g(x1)
if g0 < g1:
    xa, xb = x0, x1
    ga, gb = g0, g1
else:
    xa, xb = x1, x0
    ga, gb = g1, g0

for i in range (0,5):
    #start meth
    x_falsa = (gb * xa - ga * xb) / (gb - ga)
    print("%.6f" % (x_falsa))
    g_falsa = g(x_falsa)
    if g_falsa < 0:
        xa, ga = x_falsa, g_falsa
    else:
        xb, gb, = x_falsa, g_falsa