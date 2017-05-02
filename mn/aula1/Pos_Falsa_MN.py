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

    ###########################################################################

