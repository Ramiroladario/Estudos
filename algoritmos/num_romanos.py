class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converte um número romano para um inteiro.

        Parâmetros:
        - s (str): String representando um número em algarismos romanos.

        Retorna:
        - int: Valor inteiro correspondente ao número romano.
        """

        # Dicionário com os valores dos números romanos
        valores_romanos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        anterior = 0

        # Percorre a string de trás para frente
        for letra in reversed(s):
            valor = valores_romanos[letra]

            # Se o valor atual for menor do que o anterior, subtrai
            if valor < anterior:
                total -= valor
            else:
                total += valor

            anterior = valor  # Atualiza o último valor verificado

        return total

# Testando a solução
if __name__ == "__main__":
    # Criando uma instância da classe Solution
    solucao = Solution()
    
    # Testes com números romanos
    exemplos = ["III", "LVIII", "MCMXCIV"]
    
    for numero_romano in exemplos:
        resultado = solucao.romanToInt(numero_romano)
        print(f"{numero_romano} → {resultado}")
