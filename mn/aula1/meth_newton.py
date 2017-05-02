import matplotlib.pyplot as plt
import numpy as np

#Ponto definido para a pesquisa de valores
y0 = 42

def g(x):
    return x * x + 2 * x + 1


def g_linha(x):
    return 2 * x + 2


X = np.linspace(0, 10)
Y = g(X)
x = 5

for i in range(6):
    # Propriedades da reta aproximadora para desenhar no gráfico
    m = g_linha(x)
    Y_reta = g(x) + m * (X - x)
    x_zero = x - g(x) / m

    plt.plot(X, Y, 'b-', label='função')
    plt.plot(X, Y_reta, 'k-', label='aproximação linear')
    plt.plot([x], [g(x)], 'ko')
    plt.plot([x_zero, x_zero], [0, g(x_zero)], 'ro--')
    plt.legend(loc='best')
    plt.show()
    print('%s) g(x): %.2e' % (i, g(x)))

    # Regra de atualização
    x = x - g(x) / g_linha(x)