import numpy as np

def vand_pol(x,y):
    X = np.vander(x, x.shape[0])
    return np.linalg.solve(X,y)

def pol_inter(x,x0):
    l = len(x)
    pol = 0
    for i in range(0,l):
        pol += x[i]*x0**(l-i-1)
    return pol

n = int(input("N: "))

x = np.zeros(n)
for i in range(1,n+1):
    x[i-1]=i
y = np.zeros(n)
for i in range(0,n):
    y[i] = float(input("y%d: " % i))

sol = vand_pol(x,y)
print("f(1.5) = %.4f" % pol_inter(sol,1.5))
print("f(%.1f) = %.4f" % (n-0.5, pol_inter(sol,n - 0.5)))

