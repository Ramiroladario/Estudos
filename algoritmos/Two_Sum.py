from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Encontra dois números em 'nums' que somam 'target' e retorna seus índices.

        Parâmetros:
        - nums (List[int]): Lista de números inteiros.
        - target (int): Valor alvo da soma.

        Retorna:
        - List[int]: Lista com os dois índices dos números que somam 'target'.
        """
        hash_map = {}  # Dicionário para armazenar valores e índices
        
        # Percorre a lista para encontrar os pares
        for i, num in enumerate(nums):
            complemento = target - num  # Calcula o complemento necessário
            
            if complemento in hash_map:
                return [hash_map[complemento], i]  # Retorna os índices do par
            
            hash_map[num] = i  # Adiciona o número e seu índice ao dicionário
        
        return []  # Retorna lista vazia se não encontrar solução (não esperado pelo problema)

# Testes
if __name__ == "__main__":
    solucao = Solution()  # Criando uma instância da classe Solution

    # Teste 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(solucao.twoSum(nums1, target1))  # Esperado: [0, 1]

    # Teste 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(solucao.twoSum(nums2, target2))  # Esperado: [1, 2]

    # Teste 3
    nums3 = [3, 3]
    target3 = 6
    print(solucao.twoSum(nums3, target3))  # Esperado: [0, 1]
