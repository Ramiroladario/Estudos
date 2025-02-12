# Solicita ao usuário que insira sua idade
idade = int(input("Quantos anos você tem? "))

# Exibe a idade informada pelo usuário
print(f"Você tem {idade} anos.")

# Verifica se o usuário é maior ou menor de idade
if idade >= 18:
    print("Logo, você é maior de idade.")
else:
    print("Logo, você é menor de idade.")