from math import cos, sin, exp, sqrt
import timeit

def f(x):
    #return sin(x)*exp(-x)
    return  x**2 -4*x

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args,**kwargs)
    return wrapped

xtol = float(input("xtol: "))
x1 = float(input("x1: "))
x2 = float(input("x2: "))

# Realizando o método da busca ternária:
while True:

    xa, xb = x1 + (x2 - x1) / 3, x1 + (x2 - x1) * 2 / 3
    fa, fb = f(xa), f(xb)

    if fa > fb:
        x1 = xa
    else:
        x2 = xb

    print('xa: %.4f xb: %.4f' % (xa, xb))
    if abs(x1 -x2) <= xtol:
        break

#print("ter:",timeit.timeit(wrapper(ter,f,x1,x2,xtol),number=1000))



