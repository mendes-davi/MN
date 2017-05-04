import  numpy as np

def vand_pol(x,y):
    X = np.vander(x, x.shape[0])
    return np.linalg.solve(X,y)

xp = np.array([0,1,2,3,4])
yp = np.zeros(5)

for i in range(0,5):
    yp[i] = float(input("y%d: " % i))

sol = vand_pol(xp,yp)

for i in  range(0,5):
    print("%.6f" % sol[i])

"""
from scipy import interpolate

def lagrange_polynomial(x, y):
    return interpolate.lagrange(x, y)

sol2 = lagrange_polynomial(xp,yp)
print("oi")
for i in  range(0,5):
    print("%.6f" % sol2[i])
"""