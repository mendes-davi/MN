import timeit
import matplotlib.pyplot as plt
import numpy as np

#Ponto definido para a pesquisa de valores
y0 = 42

def g1(x):
    return f(x) -y0

def g(x):
    return x * x + 2 * x + 1

def g_linha(x):
    return 2*x + 2

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
    ultimo_ponto = -1

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

def secante(g, x0, x1, x_tol=1e-6, y_tol=1e-6):
    """
    Calcula o zero de g(x) dentro do intervalo (x0, x1) utilizando o método da
    secante. O método não exige que a raiz de g(x) esteja neste intervalo e
    nem garante que o resultado estará entre x0 e x1.

    Args:
        g: uma função de uma única variável
        x0, x1: intervalo inicial para a busca do zero de g(x)
        x_tol: tolerância em x (retorna quando intervalo for menor que x_tol)
        y_tol: tolerância em y (retorna quando |g(x)| < y_tol)

    Retuns:
        Retorna um zero de g(x) (valor de x em que g(x) = 0).
    """

    xa, xb = x1, x2
    ga, gb = g(x1), g(x2)

    while True:
        xa, xb = xb, (xa * gb - xb * ga) / (gb - ga)
        ga, gb = gb, g(xb)
        if abs(xb - xa) < x_tol or abs(gb) < y_tol:
            break
    return xb


def newton(g, g_linha, x0=0, x_tol=1e-6, y_tol=1e-6):
    """
    Calcula o zero da função g(x) com derivada g_linha(x) partindo do valor inicial
    x0.

    Args:
        g: uma função de uma única variável
        g_linha: derivada de g(x)
        x0: valor inicial
        x_tol: tolerância em x (retorna quando intervalo for menor que x_tol)
        y_tol: tolerância em y (retorna quando |g(x)| < y_tol)

    Retuns:
        Retorna um zero de g(x) (valor de x em que g(x) = 0).
    """

    x = x0

    while True:
        value = g(x)
        diff = g_linha(x)
        x = x - value / diff
        if abs(value / diff) < x_tol or abs(value) < y_tol:
            break
    return x

def ponto_fixo(g, x0, k=1, x_tol=1e-6, y_tol=1e-6):
    """
    Calcula o zero da função g(x) usando o método do ponto fixo e iterando
    sobre a função h(x) = x + k * g(x)

    Args:
        g: uma função de uma única variável
        x0: valor inicial
        k: valor usado para criar h(x) = x + k * g(x)
        x_tol: tolerância em x (retorna quando intervalo for menor que x_tol)
        y_tol: tolerância em y (retorna quando |g(x)| < y_tol)

    Retuns:
        Retorna um zero de g(x) (valor de x em que g(x) = 0).
    """
    x = x0

    while True:
        value = g(x)
        x_new = x + k * value
        x, dx = x_new, x_new - x
        if abs(dx) < x_tol or abs(value) < y_tol:
            break
        x = x_new
    return x

# Plotando o gráfico da função e a reta.
X = np.linspace(0, 10)  # cria uma sequência de números começando em zero e terminando em 10
Y = g(X)

#Testamos a performance dos métodos para avaliarmos suas funcionalidades.

#Using a decorator to wrap a function with arguments into a function without args in order to pass it to timeit.timeit()
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args,**kwargs)
    return wrapped

print("bissect (g):",timeit.timeit(wrapper(bissect,g,0,10),number=1000))
print("newton (g):",timeit.timeit(wrapper(newton,g,g_linha,5),number=1000))







