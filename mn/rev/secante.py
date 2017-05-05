from scipy.optimize import minimize
import numpy as np

def g(x):
    return x**4 - 10*x**3 + 8*x

x0 = float(input("a: "))
x1 = float(input("b: "))

xa, xb = x0, x1
ga, gb = g(x0), g(x1)

for i in range(0,8):
    xc = (xa * gb - xb * ga) / (gb - ga)
    xa = xb
    ga = g(xa)
    xb = xc
    gb = g(xb)
    print("xa f(%.6f) = %.6f" % (xa,ga))
    print("xb f(%.6f) = %.6f" % (xa, ga))
