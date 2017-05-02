from math import cos, sin, exp, sqrt

def f(x):
    return cos(x)*exp(-x)

def f_(x):
    return -sin(x)*exp(-x) - cos(x)*exp(-x)

xtol = float(input("xtol: "))
x0 = float(input("x0: "))

# Realizando o método de Newton
x = x0
while True:
    dx = -f(x)/f_(x)
    x+=dx
    print('f(%.4f) = %.4f' % (x,f(x)))
    if abs(dx) <= xtol:
        break
