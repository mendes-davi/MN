import math as mt

def f(x):
    return x-mt.cos(x)-4

n=int(input("n: "))

x0, x1 = 0, 10
f0 , f1 = f(x0), f(x1)
if f0 < f1:
    xa, xb = x0, x1
    ga, gb = f0, f1
else:
    xa, xb = x1, x0
    ga, gb = f1, f0

n_iter = 0
while n>0:
    n_iter += 1
    xmed = (xa + xb) / 2
    fmed = f(xmed)
    if fmed < 0:
        xa, ga = xmed, fmed
    elif fmed > 0:
        xb, gb = xmed, fmed
    print('%.3f, %.3f' % (xa, xb))
    if n_iter >= n:
        break

def ponto_movel(g, x0, k=1, x_tol=1e-6, y_tol=1e-6)
    x=x0

    while True:
        value = g(x)
        x_new = x + k*value
        x, dx = x_new, x_new - x
        if abs(dx) < x_tol or abs(value) < y_tol:
            break
        x = x_new
    return  x