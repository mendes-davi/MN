# Definimos a nossa função de teste e o valor de y
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * x + 2 * x + 1


# Queremos encontrar o valor de x para o qual f(x) = y0
y0 = 42

X = np.linspace(0, 10)  # cria uma sequência de números começando em zero e terminando em 10
Y = f(X)

#print('X:', X)
#print('Y:', Y)

plt.plot(X, Y, 'k-', label='f(x)')
plt.plot([0, 10], [y0, y0])
plt.title('Busca de zero de funções')  # define um título
plt.xlabel('argumento')                # nome para eixo x
plt.ylabel('valor de f(x)')            # nome para eixo y
plt.show()

for i in range(25):
    x = 5 + i / 25
    print('%2d) x: %.2f;   f(x)-y0 = %6.3f' % (i, x, f(x) - y0))
