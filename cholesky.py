import numpy as np

def cholesky(A):
    K_11 = A
    n = len(K_11)
# Create zero matrix for L
    L = [[0.0] * n for i in range(n)]
# Perform the Cholesky decomposition
    result="stable"

    for j in range(n):
        for i in np.arange(j, n, 1):
        #   determine the temporary summation
            sumTmp = 0
            for t in np.arange(0, j, 1):
                sumTmp = sumTmp + (L[i][t]) * (L[j][t])

            L[i][j] = K_11[i][j] - sumTmp

            if (i == j):
                if L[i][j]  <10e-7:
                    result ="unstable"
                    break
        if result=="unstable":
            break

        squareTmp = np.sqrt(L[j][j])
        for i in np.arange(j, n, 1):
             L[i][j] = L[i][j] / squareTmp
    print(L,"L")
    print(result)
    return result