def f(x):
    return x**3 - 10*x**2 + 8*x

def f_(x):
    return 3*x**2 - 20*x + 8

x0 = float(input("x0: "))
x=x0
count = 0
while True:
    print("%.6f" % x)
    dx = -f(x)/f_(x)
    x+= dx
    count+=1
    if count >= 10:
        break