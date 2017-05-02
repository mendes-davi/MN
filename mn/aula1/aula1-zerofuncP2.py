import matplotlib.pyplot as plt
import numpy as np

#Ponto definido para a pesquisa de valores
y0 = 42

def g(x):
    return f(x) -y0

def f(x):
    return x * x + 2 * x + 1


# Limites do intervalo para a pesquisa dos pontos.
x0, x1 = 0, 10

g0, g1 = g(x0), g(x1)

# Verificamos o comportamento da função no intervalo definido (Crescente ou ).
if g0 < g1:
    xa ,xb = x0, x1
    ga, gb = g0, g1
else:
    xa, xb = x1, x0
    ga, gb = g1, g0

# Plotando o gráfico da função e a reta.
X = np.linspace(0, 10)  # cria uma sequência de números começando em zero e terminando em 10
Y = f(X)
plt.plot(X, Y, 'k-', label='func')
#plt.plot([xa,xb], [0,0], 'ko-')
plt.show()

# Agora vamos dividir o intervalo na metade para definir o novo intervalo
xmed = (xa + xb)/2
gmed = g(xmed)
print(gmed)

# Temos que gmed é igual a -6. Deste modo sabemos que o zero de g(x) deve estar
# entre -6 e xb.
# Atualizando as var e plotamos o novo graph
xa = xmed
ga = gmed

plt.plot(X, Y - y0, 'k-', label='func')
plt.plot([xa,xb], [0,0], 'ko-')
plt.show()

'''É interessante notar que a cada iteração deste processo, reduziremos o intervalo
pela metade e temos de avaliar o intervalo remanejando xa ou xb dependendo do valor
da função no ponto esperado'''


def bissect(g, x0, x1, x_tol=1e-6, y_tol=1e-6):
    """
    Calcula o zero de g(x) dentro do intervalo (x0, x1).

    Args:
        g: uma função de uma única variável
        x0, x1: intervalo inicial para a busca do zero de g(x)
        x_tol: tolerância em x (retorna quando intervalo for menor que x_tol)
        y_tol: tolerância em y (retorna quando |g(x)| < y_tol)

    Retuns:
        Retorna um zero de g(x) (valor de x em que g(x) = 0).
    """

    # Calcula xa/ga e xb/gb
    g0, g1 = g(x0), g(x1)
    if g0 < g1:
        xa, xb = x0, x1
        ga, gb = g0, g1
    else:
        xa, xb = x1, x0
        ga, gb = g1, g0

    # Atualiza o intervalo até atingir o critério de parada
    n_iter = 0
    while True:
        n_iter += 1
        xmed = (xa + xb) / 2
        gmed = g(xmed)
        if gmed < 0:
            xa, ga = xmed, gmed
        elif gmed > 0:
            xb, gb = xmed, gmed
        else:
            return xmed

        if abs(xb - xa) < x_tol or abs(gmed) < y_tol:
            break
    if abs(ga) < abs(gb):
        return xa
    else:
        return xb

# Utilizando a função
v = bissect(g, 0, 10)
print(v)
# v =~ 5.48

def pos_falsa(g, x0, x1, x_tol=1e-6, y_tol=1e-6, illinois=True):
    """
    Calcula o zero de g(x) dentro do intervalo (x0, x1) utilizando o método da posição falsa.

    Args:
        g: uma função de uma única variável
        x0, x1: intervalo inicial para a busca do zero de g(x)
        x_tol: tolerância em x (retorna quando intervalo for menor que x_tol)
        y_tol: tolerância em y (retorna quando |g(x)| < y_tol)
        illinois: se verdadeiro, usa correção de Illinois

    Retuns:
        Retorna um zero de g(x) (valor de x em que g(x) = 0).
    """

    # Calcula xa/ga e xb/gb
    g0, g1 = g(x0), g(x1)
    if g0 < g1:
        xa, xb = x0, x1
        ga, gb = g0, g1
    else:
        xa, xb = x1, x0
        ga, gb = g1, g0

    # Atualiza o intervalo até atingir o critério de parada
    n_iter = 0
    use_illinois = False
    ponto = -1

    while True:
        n_iter += 1

        if use_illinois:
            x_falsa = (0.5 * gb * xa - ga * xb) / (0.5 * gb - ga)
            use_illinois = False
        else:
            x_falsa = (gb * xa - ga * xb) / (gb - ga)
        g_falsa = g(x_falsa)

        if g_falsa < 0:
            xa, ga = x_falsa, g_falsa
            use_illinois = illinois and ponto == 0
            ultimo_ponto = 0
        elif g_falsa > 0:
            xb, gb, = x_falsa, g_falsa
            use_illinois = illinois and ponto == 1
            ultimo_ponto = 1
        else:
            return x_falsa

        if abs(xb - xa) < x_tol or abs(g_falsa) < y_tol:
            break

    # Resultado
    if abs(ga) < abs(gb):
        return xa
    else:
        return xb

k1 = pos_falsa(g, 0, 10)
k2 = bissect(g, 0, 10)
print("Comparando os métodos: ",k1,k2)







