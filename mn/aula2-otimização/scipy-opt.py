import numpy as np

pi=np.pi

def newton(f,x0,e=1e-6,derivada=None):
    """
    Encontra extremo de funções
    """

    if derivada is None:
        def f_(x):
            return (f(x+e) - f(x)) / e
    else:
        f_ = derivada

    def f__(x):
        return (f_(x+e) - f_(x)) / e

    x=x0
    for i in range (20):
        x = x - f_(x) / f__(x)

    return x

#criar o args da 2a derivada para casa
r = newton(np.sin,1,derivada=np.cos)
print("r = ",r)