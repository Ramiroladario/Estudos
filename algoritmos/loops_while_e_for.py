# Sistema de Cadastro de Usuários

# Lista para armazenar os usuários cadastrados
usuarios = []

# Loop principal do sistema
while True:
    # Menu de opções
    print("\n--- Menu ---")
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários cadastrados")
    print("3. Sair")

    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    # Opção 1: Cadastrar novo usuário
    if opcao == "1":
        print("\nCadastro de novo usuário")

        # Solicita o nome do usuário
        nome = input("Digite o nome do usuário: ")

        # Solicita a idade do usuário
        while True:
            try:
                idade = int(input("Digite a idade do usuário: "))
                if idade < 0:
                    print("Idade inválida. Digite um número positivo.")
                else:
                    break  # Sai do loop se a idade for válida
            except ValueError:
                print("Por favor, digite um número válido para a idade.")

        # Adiciona o usuário à lista de usuários
        usuarios.append({"nome": nome, "idade": idade})
        print(f"Usuário {nome} cadastrado com sucesso!")

    # Opção 2: Listar usuários cadastrados
    elif opcao == "2":
        print("\nLista de usuários cadastrados:")

        # Verifica se há usuários cadastrados
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            # Usa um loop for para percorrer e exibir todos os usuários
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']} anos")

    # Opção 3: Sair do sistema
    elif opcao == "3":
        print("\nSaindo do sistema...")
        break  # Sai do loop principal e encerra o programa

    # Opção inválida
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

# Mensagem final
print("Obrigado por usar o sistema de cadastro de usuários!")