# Solicita a quantidade de reais ao usuário
reais = float(input("Quantos Reais eu tenho? R$ "))

# Converte reais para dólares (taxa de câmbio: 5.85)
dolares = reais / 5.85

# Exibe o resultado
print(f"Logo, eu tenho U$$ {dolares:.2f}")