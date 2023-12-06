def dois_soma_simples(nums, X):
    """
    Solução Simples: Complexidade O(n^2)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == X:
                return [i, j]

def dois_soma_melhorada(nums, X):
    """
    Solução Melhorada: Complexidade abaixo de O(n^2) (bonus 0.1)
    """
    num_indices = {}
    for i, num in enumerate(nums):
        complemento = X - num
        if complemento in num_indices:
            return [num_indices[complemento], i]
        num_indices[num] = i

def dois_soma_melhor_caso(nums, X):
    """
    Solução Melhor Caso: Complexidade O(n) (bonus 0.2)
    """
    num_indices = {}
    for i, num in enumerate(nums):
        complemento = X - num
        if complemento in num_indices:
            return [num_indices[complemento], i]
        num_indices[num] = i


numeros = [4, 8, 6, 2 , 1]
X = 10

resultado_simples = dois_soma_simples(numeros, X)
resultado_melhorada = dois_soma_melhorada(numeros, X)
resultado_melhor_caso = dois_soma_melhor_caso(numeros, X)

print("RESULTADOS:")
print("Solução Simples:", resultado_simples)
print("Solução Melhorada:", resultado_melhorada)
print("Solução Melhor Caso:", resultado_melhor_caso)