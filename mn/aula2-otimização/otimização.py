import timeit
import matplotlib.pyplot as plt
import numpy as np

#Using a decorator to wrap a function with arguments into a function without args in order to pass it to timeit.timeit()
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args,**kwargs)
    return wrapped

''' Retirado do notebook zero de funções, produzido na uala 
# Define função para testar o método da biseção
def g(x):
    return np.cos(x/2)

N = 10  # Número de iterações
x0, x1 = 3, 4  # Intervalo inicial
y0, y1 = g(x0), g(x1)

# Decide qual dos dois pontos corresponde a (xa, ya)
# onde xa, ya representa o ponto abaixo de zero e
# xb, yb representa o ponto acima de zero.
if y0 < y1:
    xa, ya = x0, y0
    xb, yb = x1, y1
else:
    xa, ya = x1, y1
    xb, yb = x0, y0

for i in range(N):
    # Calcula novo valor dentro do intervalo
    x_med = (xa + xb) / 2
    y_med = g(x_med)

    # Determina se o novo valor corresponde a xa ou a xb
    if y_med < 0:
        xa, ya = x_med, y_med
    elif y_med > 0:
        xb, yb = x_med, y_med
    else:
        break

# Decide qual é o melhor valor
if abs(ya) < abs(yb):
    resposta = xa
else:
    resposta = xb9

print('   x:', resposta)
print('g(x):', g(resposta))
'''

#Seguindo para a aula 2 de MN. Busca ternária...