class Comparador:
    # Correção dos asteriscos duplos na definição do método __init__
    def __init__(self, a, b, c):
        # Atribui os valores recebidos aos atributos do objeto
        self.a = a
        self.b = b
        self.c = c
    
    def comparar(self):
        # Método para comparar se todos os valores são iguais
        return self.a == self.b == self.c
    
    def mostrar_resultado(self):
        # Mostra o resultado da comparação
        print(self.comparar())

# Correção da indentação do bloco de uso
# Correção dos asteriscos duplos no __name__
if __name__ == '__main__':
    # Cria uma instância do Comparador com valores iguais
    comp = Comparador(1, 1, 1)
    # Chama o método para mostrar o resultado
    comp.mostrar_resultado()  # Imprimirá True