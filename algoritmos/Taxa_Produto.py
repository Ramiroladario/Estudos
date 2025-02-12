try:
    # Solicita o preço do produto ao usuário
    preco = float(input("Qual o preco do produto? US$ "))
    
    # Verifica se o preço é positivo
    if preco < 0:
        print("O preço não pode ser negativo!")
    else:
        # Calcula o imposto (60% do preço)
        imposto = (preco * 60) / 100

        # Exibe o preço e o imposto formatados com duas casas decimais
        print(f"Preço do produto: US$ {preco:.2f}")
        print(f"O imposto sera de US$ {imposto:.2f}")

except ValueError:
    print("Por favor, digite um valor numérico válido!")