import numpy as np

def strassen_multiply(A, B):
    n = len(A)


    if n == 1:
        return np.array([[A[0, 0] * B[0, 0]]])


    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]


    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)


    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6


    result = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result

A = np.array([[10, 15], [50, 60]])
B = np.array([[8, 6], [6, 25]])

resultado = strassen_multiply(A, B)
print("Resultado da multiplicação de matrizes:")
print(resultado)