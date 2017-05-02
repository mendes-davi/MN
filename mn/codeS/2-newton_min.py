from math import cos, sin

def f(x):
    return x-cos(x)-4

def f_(x):
    return sin(x)+1

x0 = float(input("x: "))
n_iter = int(input("n: "))
count=0

# Realizando o método de Newton para minimos
x = x0
while True and n_iter != 0:
    dx = -f(x)/f_(x)
    x+=dx
    print('%.4f'%x)
    count+=1
    if count>=n_iter:
        break


