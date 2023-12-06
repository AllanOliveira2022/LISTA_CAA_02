#Resultado simples
def merge(nums1, m, nums2, n):
    nums1[:m] += nums2


    def mergesort(arr):
        if len(arr) > 1:
            meio = len(arr) // 2
            esquerda = arr[:meio]
            direita = arr[meio:]

            mergesort(esquerda)
            mergesort(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    arr[k] = esquerda[i]
                    i += 1
                else:
                    arr[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                arr[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                arr[k] = direita[j]
                j += 1
                k += 1


    mergesort(nums1)

nums1 = [5, 42, 47, 0, 0, 0]
m = 3
nums2 = [1, 8, 24]
n = 3

merge(nums1, m, nums2, n)

print("Resultado após a união com 'O((m + n)log(m + n))':", nums1)

# Resultado com O(m + n):

def merge(nums1, m, nums2, n):
    indice_nums1 = m - 1
    indice_nums2 = n - 1
    indice_final = m + n - 1

    while indice_nums1 >= 0 and indice_nums2 >= 0:
        if nums1[indice_nums1] > nums2[indice_nums2]:
            nums1[indice_final] = nums1[indice_nums1]
            indice_nums1 -= 1
        else:
            nums1[indice_final] = nums2[indice_nums2]
            indice_nums2 -= 1
        indice_final -= 1


    nums1[:indice_nums2 + 1] = nums2[:indice_nums2 + 1]

nums1 = [5, 42, 56, 0, 0, 0]
m = 3
nums2 = [3, 6, 8]
n = 3

merge(nums1, m, nums2, n)

print("Resultado após a junção com 'O(m + n)':", nums1)
