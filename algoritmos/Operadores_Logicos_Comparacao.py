# Sistema de Verificação de Elegibilidade para um Concurso Público

# Solicita ao usuário que insira sua idade
idade = int(input("Quantos anos você tem? "))

# Solicita ao usuário que insira seu nível de escolaridade
print("\nEscolha seu nível de escolaridade:")
print("1 - Ensino Médio")
print("2 - Graduação")
print("3 - Pós-Graduação")
escolaridade = int(input("Digite o número correspondente: "))

# Solicita ao usuário que insira seus anos de experiência profissional
experiencia = int(input("Quantos anos de experiência profissional você tem? "))

# Exibe os dados fornecidos pelo usuário
print("\nDados fornecidos:")
print(f"Idade: {idade} anos")
print(f"Escolaridade: {escolaridade}")
print(f"Experiência profissional: {experiencia} anos")

# Verifica a elegibilidade do candidato
print("\nVerificando elegibilidade...")

# Regras de elegibilidade:
# 1. Idade mínima: 18 anos
# 2. Escolaridade mínima: Ensino Médio (1)
# 3. Experiência mínima: 2 anos para Ensino Médio, 1 ano para Graduação, 0 anos para Pós-Graduação

# Usando operadores de comparação e lógicos para verificar as condições
if idade >= 18:  # Verifica se o candidato tem pelo menos 18 anos
    if escolaridade == 1:  # Ensino Médio
        if experiencia >= 2:  # Precisa de pelo menos 2 anos de experiência
            print("\nParabéns! Você é elegível para o concurso.")
        else:
            print("\nVocê não atende ao requisito de experiência mínima para Ensino Médio (2 anos).")
    elif escolaridade == 2:  # Graduação
        if experiencia >= 1:  # Precisa de pelo menos 1 ano de experiência
            print("\nParabéns! Você é elegível para o concurso.")
        else:
            print("\nVocê não atende ao requisito de experiência mínima para Graduação (1 ano).")
    elif escolaridade == 3:  # Pós-Graduação
        if experiencia >= 0:  # Não precisa de experiência
            print("\nParabéns! Você é elegível para o concurso.")
        else:
            print("\nAlgo deu errado. Verifique seus dados.")
    else:
        print("\nEscolaridade inválida. Por favor, insira um número entre 1 e 3.")
else:
    print("\nVocê não atende ao requisito de idade mínima (18 anos).")

# Mensagem final
print("\nObrigado por usar o sistema de verificação de elegibilidade!")