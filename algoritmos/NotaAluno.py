class CalculadoraNotas:
    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0
        self.media = 0

    def obter_notas(self):
        self.nota1 = float(input("Primeira Nota: "))
        self.nota2 = float(input("Segunda Nota: "))

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def verificar_situacao(self):
        self.media = self.calcular_media()
        print(f"A média do aluno foi {self.media:.2f}")
        
        if self.media >= 7:
            print("Aluno APROVADO")
        elif self.media >= 5:
            print("Aluno RECUPERACAO")
        else:
            print("Aluno REPROVADO")

if __name__ == "__main__":
    calculadora = CalculadoraNotas()
    calculadora.obter_notas()
    calculadora.verificar_situacao()