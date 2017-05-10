def f(x):
    return {
        0:0,
        1:1.5,
        2:1.1754,
        3:-0.0468,
        4:0.08825,
        5:3.3291,
    }.get(x, -1)

x0 = float(input())
if f(x0) == -1:
    if round(x0) < x0:
        limInf = round(x0)
        limSup = round(x0 + 0.5)
    else:
        limSup = round(x0)
        limInf = round(x0 - 0.5)
    y = f(limInf) + (x0 - limInf)*(f(limSup) - f(limInf))/(limSup - limInf)
    print("%.6f" % y)
else:
    print("%.6f"% f(x0))

