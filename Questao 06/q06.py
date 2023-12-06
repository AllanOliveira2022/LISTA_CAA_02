def subsequencia_palindroma_maxima(S):
    n = len(S)
    

    tabela = [[0] * n for _ in range(n)]


    for i in range(n):
        tabela[i][i] = 1

    inicio_max = 0
    comprimento_max = 1


    for tamanho_subsequencia in range(2, n + 1):
        for i in range(n - tamanho_subsequencia + 1):
            j = i + tamanho_subsequencia - 1

            if tamanho_subsequencia == 2 and S[i] == S[j]:
                tabela[i][j] = 2
            elif S[i] == S[j]:
                tabela[i][j] = tabela[i + 1][j - 1] + 2

            if tabela[i][j] > comprimento_max:
                comprimento_max = tabela[i][j]
                inicio_max = i

    return S[inicio_max:inicio_max + comprimento_max]


sequencia_exemplo = "OVORIRRIDERCROSS"
resultado = subsequencia_palindroma_maxima(sequencia_exemplo)
print("Subsequência Palíndroma Máxima:", resultado)