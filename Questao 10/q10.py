def busca_insercao(nums, alvo):
    esquerda, direita = 0, len(nums) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if nums[meio] == alvo:
            return meio
        elif nums[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return esquerda


array_ordenado = [10, 5, 6, 7]
alvo1 = 10
alvo2 = 6

indice1 = busca_insercao(array_ordenado, alvo1)
indice2 = busca_insercao(array_ordenado, alvo2)

print("Índice do alvo 1 ou posição de inserção:", indice1)
print("Índice do alvo 2 ou posição de inserção:", indice2)