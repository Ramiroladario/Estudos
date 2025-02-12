class IdadeCalculator:
    def _init_(self):
        self.ano_atual = 0
        self.ano_nasc = 0
    
    def obter_dados(self):
        self.ano_atual = int(input("Em que ano estamos? "))
        self.ano_nasc = int(input("Em que ano você nasceu? "))
    
    def calcular_idade(self):
        return self.ano_atual - self.ano_nasc
    
    def exibir_idade(self):
        idade = self.calcular_idade()
        print(f"Minha idade será {idade}")

if __name__ == "__main__":
    calculadora = IdadeCalculator()
    calculadora.obter_dados()
    calculadora.exibir_idade()