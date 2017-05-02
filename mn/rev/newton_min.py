from math import cos, sin, exp


def f(x):
    return cos(x) * exp(-x)


def f_(x):
    return -sin(x) * exp(-x) - cos(x) * exp(-x)


def f__(x):
    return 2 * exp(-x) * sin(x)


xtol = float(input("xtol: "))
x0 = float(input("x0: "))
# verificar entrada
# Realizando o método de Newton para minimos
x = x0
while True:
    dx = x - f_(x) / f__(x)
    print('f(%.4f) = %.4f' % (x, f(x)))
    if abs(dx) <= xtol:
        break 