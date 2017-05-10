import numpy as np

n = int(input("N: "))

X = np.zeros(n)
for i in range(1,n+1):
    X[i-1]=i
Y = np.zeros(n)
for i in range(0,n):
    k = i+1
    Y[i] = float(input("y%d: " %k))

xm = X.mean()
ym = Y.mean()
xym = (X * Y).mean()
#aaaa
#aa
#aaa
xxm = (X * X).mean()
yym=(Y*Y).mean()
am = (xxm * ym - xm *xym) / (xxm - xm * xm)
bm = (xym - xm * ym) / (xxm - xm * xm)

print("y = %.6f + %.6f * x" % (am,bm))