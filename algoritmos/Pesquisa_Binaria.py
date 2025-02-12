# Algoritmo de Pesquisa Binária em Python
# Este algoritmo é usado para encontrar um elemento em uma lista ORDENADA de forma eficiente.

def pesquisa_binaria(lista, elemento):
    """
    Função que implementa o algoritmo de pesquisa binária.
    
    :param lista: Lista ORDENADA onde a pesquisa será realizada.
    :param elemento: Elemento que estamos procurando na lista.
    :return: Retorna o índice do elemento se ele estiver na lista, caso contrário retorna -1.
    """
    
    # Definindo os índices inicial e final da lista
    inicio = 0
    fim = len(lista) - 1
    
    # Enquanto o índice inicial for menor ou igual ao índice final
    while inicio <= fim:
        # Calculando o índice do meio da lista
        meio = (inicio + fim) // 2
        
        # Verificando se o elemento do meio é o que estamos procurando
        if lista[meio] == elemento:
            return meio  # Retorna o índice do elemento encontrado
        
        # Se o elemento do meio for maior que o elemento procurado,
        # descartamos a metade superior da lista
        elif lista[meio] > elemento:
            fim = meio - 1
        
        # Se o elemento do meio for menor que o elemento procurado,
        # descartamos a metade inferior da lista
        else:
            inicio = meio + 1
    
    # Se o elemento não for encontrado, retornamos -1
    return -1

# Exemplo de uso do algoritmo de pesquisa binária
if __name__ == "__main__":
    # Lista ORDENADA de números
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Elemento que queremos encontrar
    elemento = 7
    
    # Chamando a função de pesquisa binária
    resultado = pesquisa_binaria(lista, elemento)
    
    # Verificando o resultado da pesquisa
    if resultado != -1:
        print(f"Elemento {elemento} encontrado no índice {resultado}.")
    else:
        print(f"Elemento {elemento} não encontrado na lista.")