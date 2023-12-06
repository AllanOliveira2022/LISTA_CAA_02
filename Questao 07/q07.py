def quadrados_em_ordem(nums):
    n = len(nums)
    resultado = [0] * n
    esquerda, direita = 0, n - 1
    indice = n - 1

    while esquerda <= direita:
        quadrado_esquerda, quadrado_direita = nums[esquerda] ** 2, nums[direita] ** 2

        if quadrado_esquerda > quadrado_direita:
            resultado[indice] = quadrado_esquerda
            esquerda += 1
        else:
            resultado[indice] = quadrado_direita
            direita -= 1

        indice -= 1

    return resultado

nums_ordenados = [4, 6, 10, 15, 20]
resultado = quadrados_em_ordem(nums_ordenados)
print("Quadrados em Ordem:", resultado)

#Essa abordagem tem complexidade O(n), pois percorre o array uma vez, preenchendo o array de resultado em ordem não decrescente dos quadrados.




