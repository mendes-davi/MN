import  numpy as np

M = np.array([[2,1],
              [3,1]])
y = np.array([0,1])
#np.hstack([M,y]) #Last IN First OUT
# matrix.transpose() method

y_col = y[:, None]
MM = np.hstack([M,y_col])
MM = MM.astype(float)

l0 = MM[0] #matrix first line
l1 = MM[1] #matrix second line
 # Vamos iterar usando a eliminação gaussiana
MM[1] = l0 - MM[0,0]/MM[1,0] * l1

print(MM)

#implementando como método
"""
Eliminação de Gauss.

1 - Criar a matriz aumentada
2 - Torna-la triangular superior 
3 - Pivos em 1
4 - Resolver a matriz

"""
def solve(matrix,y):
    """
    Resolve um sistema linear dado por uma matriz
    extender matriz
    upper triangular
    normalize pivot
    """

    M = extended_matrix(matrix,y).astype(float)

    def extended_matrix(matrix, y):
        """
        :param matrix: matrix
        :param y: vetor
        :return: extended matrix
        """
        return np.hstack([matrix, y[:, None]])

    def upper_triangular(M):
        """
        :param M: Matriz a ser triangularizada 
        :return: matriz triangular
        """
        L0, L1 = M[0], M[1]
        pivot = M[0, 0]
        m10 = M[1,0]
        M[1] = L0 - pivot/m10 * L1
        return M

    def normaliza_pivot(M):
        """
        :param M: Matriz triangular superior 
        :return: matriz com pivos normalizados
        """
        M[0] /= M[0,0]
        M[1] /= M[1,1]
        return M;

    def solve_upper(matrix, y):
        """
        :param matrix: matriz dos coeficientes 
        :param y: vetor das variaveis
        :return: matriz resolvida
        """
        return np.array(y[0] - matrix[0,1]*y[1], y[1])
    return solve_upper(M[:, : -1], M[:,-1])
