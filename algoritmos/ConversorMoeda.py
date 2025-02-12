class ConversorMoeda:
    def __init__(self):
        # Taxa de câmbio fixa (pode ser atualizada facilmente)
        self.taxacambio = 5.85
        # Valor em reais iniciado com zero
        self.reais = 0

    def pedir_valor_em_reais(self):
        # Método para solicitar valor em reais
        self.reais = float(input("Quantos Reais eu tenho? R$"))

    def converter_para_dolares(self):
        # Calcula os dólares dividindo reais pela taxa de câmbio
        return self.reais / self.taxacambio

    def mostrar_resultado(self):
        # Método para mostrar o resultado da conversão
        dolares = self.converter_para_dolares()
        print(f"Você tem U$ {dolares:.2f}")

# Uso correto fora da definição da classe
if __name__ == '__main__':
    # Cria uma instância do conversor
    conv = ConversorMoeda()
    # Solicita o valor em reais
    conv.pedir_valor_em_reais()
    # Mostra o resultado da conversão
    conv.mostrar_resultado()