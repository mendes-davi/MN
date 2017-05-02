def f(x):
    return (x**4 - 10*x**3 - x**2 + 5*x)/(x**4 + 1)

x0 = float(input("a: "))
x1 = float(input("b: "))

f0 , f1 = f(x0), f(x1)
if f0 < f1:
    xa, xb = x0, x1
    ga, gb = f0, f1
else:
    xa, xb = x1, x0
    ga, gb = f1, f0

count = 0
while True:
    xmed = (xa + xb)/2
    fmed = f(xmed)
    print('%.6f' % xmed)
    if fmed < 0:
        xa, ga = xmed, fmed
    elif fmed > 0:
        xb, gb = xmed, fmed
    count+=1
    if count >= 10:
        break

if abs(f(xmed)) > 1e-2:
    print("Intervalo invalido")