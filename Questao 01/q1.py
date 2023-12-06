def decomposicao(S, p, r, piv):
    q1, q2 = particao(S, p, r, piv)
    
    print("Índices Q1:", q1)
    print("Índices Q2:", q2)
    
def particao(S, p, r, piv):
    q1 = p - 1
    q2 = r + 1
    i = p

    while i < q2:
        if S[i] < piv:
            S[i], S[q1 + 1] = S[q1 + 1], S[i]
            q1 += 1
            i += 1
        elif S[i] == piv:
            i += 1
        else:
            S[i], S[q2 - 1] = S[q2 - 1], S[i]
            q2 -= 1

    return q1 + 1, q2 - 1


vetor = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
pivote = 4
p, r = 0, len(vetor) - 1

decomposicao(vetor, p, r, pivote)
print("Vetor rearranjado:", vetor)