from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove todas as ocorrências de 'val' do array 'nums' in-place.

        Parâmetros:
        - nums (List[int]): Lista de números inteiros.
        - val (int): Valor a ser removido.

        Retorna:
        - int: Número de elementos restantes após a remoção.
        """
        k = 0  # Contador para elementos que não são 'val'

        # Percorre a lista e mantém apenas os valores diferentes de 'val'
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move o elemento para a posição correta
                k += 1  # Incrementa o contador dos elementos restantes

        return k  # Retorna o número de elementos restantes

# Testes
if __name__ == "__main__":
    solucao = Solution()  # Criando uma instância da classe Solution

    # Teste 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solucao.removeElement(nums1, val1)
    print(f"Output: {k1}, nums = {nums1[:k1]}")  # Esperado: 2, nums = [2, 2]

    # Teste 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solucao.removeElement(nums2, val2)
    print(f"Output: {k2}, nums = {nums2[:k2]}")  # Esperado: 5, nums = [0, 1, 0, 4, 3]
