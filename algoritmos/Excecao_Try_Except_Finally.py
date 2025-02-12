# Sistema de Gerenciamento de Contas Bancárias

# Dicionário para armazenar as contas bancárias
contas = {}

# Função para criar uma nova conta
def criar_conta():
    print("\nCriar Nova Conta")

    # Solicita o número da conta
    while True:
        try:
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta in contas:
                print("Conta já existente. Tente outro número.")
            else:
                break  # Sai do loop se o número da conta for válido
        except ValueError:
            print("Por favor, digite um número válido para a conta.")

    # Solicita o nome do titular da conta
    nome_titular = input("Digite o nome do titular da conta: ")

    # Solicita o saldo inicial da conta
    while True:
        try:
            saldo_inicial = float(input("Digite o saldo inicial da conta: "))
            if saldo_inicial < 0:
                print("Saldo inválido. Digite um valor positivo.")
            else:
                break  # Sai do loop se o saldo for válido
        except ValueError:
            print("Por favor, digite um número válido para o saldo.")

    # Adiciona a conta ao dicionário de contas
    contas[numero_conta] = {"titular": nome_titular, "saldo": saldo_inicial}
    print(f"Conta {numero_conta} criada com sucesso!")

# Função para depositar dinheiro em uma conta
def depositar():
    print("\nDepositar Dinheiro")

    # Solicita o número da conta
    while True:
        try:
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta not in contas:
                print("Conta não encontrada. Tente novamente.")
            else:
                break  # Sai do loop se a conta for válida
        except ValueError:
            print("Por favor, digite um número válido para a conta.")

    # Solicita o valor do depósito
    while True:
        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
            if valor_deposito < 0:
                print("Valor inválido. Digite um valor positivo.")
            else:
                break  # Sai do loop se o valor for válido
        except ValueError:
            print("Por favor, digite um número válido para o valor.")

    # Realiza o depósito
    contas[numero_conta]["saldo"] += valor_deposito
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")

# Função para sacar dinheiro de uma conta
def sacar():
    print("\nSacar Dinheiro")

    # Solicita o número da conta
    while True:
        try:
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta not in contas:
                print("Conta não encontrada. Tente novamente.")
            else:
                break  # Sai do loop se a conta for válida
        except ValueError:
            print("Por favor, digite um número válido para a conta.")

    # Solicita o valor do saque
    while True:
        try:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque < 0:
                print("Valor inválido. Digite um valor positivo.")
            elif valor_saque > contas[numero_conta]["saldo"]:
                print("Saldo insuficiente. Tente um valor menor.")
            else:
                break  # Sai do loop se o valor for válido
        except ValueError:
            print("Por favor, digite um número válido para o valor.")

    # Realiza o saque
    contas[numero_conta]["saldo"] -= valor_saque
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")

# Função para verificar o saldo de uma conta
def verificar_saldo():
    print("\nVerificar Saldo")

    # Solicita o número da conta
    while True:
        try:
            numero_conta = int(input("Digite o número da conta: "))
            if numero_conta not in contas:
                print("Conta não encontrada. Tente novamente.")
            else:
                break  # Sai do loop se a conta for válida
        except ValueError:
            print("Por favor, digite um número válido para a conta.")

    # Exibe o saldo da conta
    saldo = contas[numero_conta]["saldo"]
    print(f"Saldo da conta {numero_conta}: R${saldo:.2f}")

# Função principal do sistema
def main():
    while True:
        # Menu de opções
        print("\n--- Menu ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Verificar Saldo")
        print("5. Sair")

        # Solicita ao usuário que escolha uma opção
        try:
            opcao = int(input("Escolha uma opção (1, 2, 3, 4 ou 5): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue  # Volta ao início do loop

        # Opção 1: Criar Conta
        if opcao == 1:
            criar_conta()

        # Opção 2: Depositar
        elif opcao == 2:
            depositar()

        # Opção 3: Sacar
        elif opcao == 3:
            sacar()

        # Opção 4: Verificar Saldo
        elif opcao == 4:
            verificar_saldo()

        # Opção 5: Sair do sistema
        elif opcao == 5:
            print("\nSaindo do sistema...")
            break  # Sai do loop principal e encerra o programa

        # Opção inválida
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")

    # Mensagem final (substitui o finally, que não é necessário aqui)
    print("\nObrigado por utilizar o Sistema de Gerenciamento de Contas Bancárias!")

# Executa o sistema
if __name__ == "__main__":
    main()