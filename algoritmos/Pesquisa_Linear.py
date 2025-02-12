# Algoritmo de Pesquisa Linear (Linear Search)
# Autor: [Ramiro Belard Ladario]
# Objetivo: Demonstrar como funciona a busca linear de forma didática

from typing import List, Any

class PesquisaLinear:
    """
    Classe que implementa e demonstra o Algoritmo de Pesquisa Linear.
    
    A Pesquisa Linear é um método simples de encontrar um elemento em uma lista,
    percorrendo cada elemento um por um até encontrar o valor desejado.
    """

    def __init__(self, lista: List[Any]):
        """
        Inicializa a classe com uma lista de elementos.

        Parâmetros:
        - lista (List[Any]): Lista de elementos para realizar a busca.
        """
        self.lista = lista

    def busca_linear(self, elemento: Any) -> int:
        """
        Realiza a busca linear para encontrar um elemento na lista.

        Parâmetros:
        - elemento (Any): Valor a ser procurado na lista.

        Retorna:
        - int: Índice do elemento se encontrado, -1 se não encontrado.
        """
        print(f"\n📍 Iniciando busca linear por: {elemento}")

        for indice, valor in enumerate(self.lista):
            print(f"   🔍 Verificando índice {indice}: {valor}")

            if valor == elemento:
                print(f"   ✅ Elemento {elemento} encontrado no índice {indice}")
                return indice

        print(f"   ❌ Elemento {elemento} não encontrado na lista")
        return -1

    def demonstrar_busca(self, elemento: Any) -> None:
        """
        Método para demonstrar a busca de forma visual e educativa.

        Parâmetros:
        - elemento (Any): Valor a ser procurado na lista.
        """
        print("\n🔢 Lista original:")
        print("   ", " | ".join(map(str, self.lista)))  # Formatação melhorada

        resultado = self.busca_linear(elemento)

        print("\n📊 Resumo da Busca:")
        if resultado != -1:
            print(f"   • Elemento {elemento} está na lista")
            print(f"   • Índice: {resultado}")
        else:
            print(f"   • Elemento {elemento} NÃO está na lista")

def main() -> None:
    """
    Função principal para demonstrar o algoritmo de pesquisa linear.
    """
    print("🔍 Exemplo 1: Busca em lista de números")
    numeros = [10, 25, 38, 45, 60, 72, 89]
    busca_numeros = PesquisaLinear(numeros)

    busca_numeros.demonstrar_busca(38)   # Elemento presente
    busca_numeros.demonstrar_busca(100)  # Elemento ausente

    print("\n🔍 Exemplo 2: Busca em lista de strings")
    frutas = ["maçã", "banana", "laranja", "uva", "morango"]
    busca_frutas = PesquisaLinear(frutas)

    busca_frutas.demonstrar_busca("uva")       # Elemento presente
    busca_frutas.demonstrar_busca("abacaxi")   # Elemento ausente

if __name__ == "__main__":
    main()
