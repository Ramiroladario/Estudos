# Sistema de Gerenciamento de Estoque

# Dicionário para armazenar os produtos e suas quantidades
estoque = {}

# Set para armazenar categorias únicas de produtos
categorias = set()

# Função para adicionar um produto ao estoque
def adicionar_produto():
    print("\nAdicionar Produto")

    # Solicita o nome do produto
    nome = input("Digite o nome do produto: ")

    # Solicita a categoria do produto
    categoria = input("Digite a categoria do produto: ")

    # Solicita a quantidade do produto
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("Quantidade inválida. Digite um número positivo.")
            else:
                break  # Sai do loop se a quantidade for válida
        except ValueError:
            print("Por favor, digite um número válido para a quantidade.")

    # Adiciona o produto ao dicionário de estoque
    estoque[nome] = {"categoria": categoria, "quantidade": quantidade}

    # Adiciona a categoria ao set de categorias
    categorias.add(categoria)

    print(f"Produto {nome} adicionado ao estoque com sucesso!")

# Função para atualizar a quantidade de um produto no estoque
def atualizar_quantidade():
    print("\nAtualizar Quantidade do Produto")

    # Solicita o nome do produto
    nome = input("Digite o nome do produto: ")

    # Verifica se o produto existe no estoque
    if nome in estoque:
        # Solicita a nova quantidade do produto
        while True:
            try:
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                if nova_quantidade < 0:
                    print("Quantidade inválida. Digite um número positivo.")
                else:
                    break  # Sai do loop se a quantidade for válida
            except ValueError:
                print("Por favor, digite um número válido para a quantidade.")

        # Atualiza a quantidade do produto no dicionário de estoque
        estoque[nome]["quantidade"] = nova_quantidade
        print(f"Quantidade do produto {nome} atualizada com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

# Função para remover um produto do estoque
def remover_produto():
    print("\nRemover Produto")

    # Solicita o nome do produto
    nome = input("Digite o nome do produto: ")

    # Verifica se o produto existe no estoque
    if nome in estoque:
        # Remove o produto do dicionário de estoque
        del estoque[nome]
        print(f"Produto {nome} removido do estoque com sucesso!")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

# Função para listar todos os produtos no estoque
def listar_produtos():
    print("\nLista de Produtos no Estoque:")

    # Verifica se há produtos no estoque
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
    else:
        # Usa um loop for para percorrer e exibir todos os produtos
        for nome, produto in estoque.items():
            print(f"Nome: {nome}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']} unidades")

# Função para listar todas as categorias de produtos
def listar_categorias():
    print("\nLista de Categorias de Produtos:")

    # Verifica se há categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada.")
    else:
        # Usa um loop for para percorrer e exibir todas as categorias
        for categoria in categorias:
            print(f"Categoria: {categoria}")

# Loop principal do sistema
while True:
    # Menu de opções
    print("\n--- Menu ---")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade do Produto")
    print("3. Remover Produto")
    print("4. Listar Produtos")
    print("5. Listar Categorias")
    print("6. Sair")

    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção (1, 2, 3, 4, 5 ou 6): ")

    # Opção 1: Adicionar Produto
    if opcao == "1":
        adicionar_produto()

    # Opção 2: Atualizar Quantidade do Produto
    elif opcao == "2":
        atualizar_quantidade()

    # Opção 3: Remover Produto
    elif opcao == "3":
        remover_produto()

    # Opção 4: Listar Produtos
    elif opcao == "4":
        listar_produtos()

    # Opção 5: Listar Categorias
    elif opcao == "5":
        listar_categorias()

    # Opção 6: Sair do sistema
    elif opcao == "6":
        print("\nSaindo do sistema...")
        break  # Sai do loop principal e encerra o programa

    # Opção inválida
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, 3, 4, 5 ou 6.")

# Mensagem final
print("\nObrigado por utilizar o Sistema de Gerenciamento de Estoque!")