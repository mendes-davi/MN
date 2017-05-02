
#Método de demonstrção do uso de minimos quadrados para um exercicio de interpolação

import numpy as np
import matplotlib.pyplot as plt

a, b= 1,2
e=10
X= np.linspace(0,10,N)
Y= a + b*X + np.random.normal(size=N, scale=1.37)
# .mean() média, .std() standard deviation (DP)
xm = X.mean()
ym = Y.mean()
xym = (X * Y).mean()
xxm = (X * X).mean()
yym=(Y*Y).mean()

#x_std=np.sqrt(xxm-xm**2) calculo topeira, usar método .std()!!!
#y_std=np.sqrt(yym-ym**2)
#cov=xym-xm*ym covariancia
#corr=cov/(y_std*x_std) correlação linear


am = (xxm * ym - xm *xym) / (xxm - xm * xm)
bm = (xym - xm * ym) / (xxm - xm * xm)

plt.plot(X,Y,'ko')
plt.plot(X, am + bm * X,'r')
plt.show()