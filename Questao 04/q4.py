def elemento_majoritario(nums):
    majoritario = nums[0]
    contagem = 1

    for num in nums[1:]:
        if contagem == 0:
            majoritario = num
            contagem = 1
        elif num == majoritario:
            contagem += 1
        else:
            contagem -= 1

    return majoritario

# Exemplo de uso:
array_exemplo = [5,6,3,4,8,10, 4, 3, 5, 9, 8, 8, 7, 8]
resultado = elemento_majoritario(array_exemplo)
print("Elemento Majoritário:", resultado)