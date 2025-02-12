# main.py
# Script Python para manipular um arquivo de texto (dados.txt)

# Função para ler o conteúdo do arquivo
def ler_arquivo():
    try:
        # Abre o arquivo em modo de leitura ('r')
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            # Lê todas as linhas do arquivo
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo 'dados.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Função para adicionar uma nova linha ao arquivo
def adicionar_linha():
    try:
        # Solicita ao usuário a nova linha a ser adicionada
        nova_linha = input("\nDigite a nova linha a ser adicionada: ")

        # Abre o arquivo em modo de adição ('a')
        with open("dados.txt", "a", encoding="utf-8") as arquivo:
            # Adiciona a nova linha ao final do arquivo
            arquivo.write("\n" + nova_linha)
        print("Linha adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar linha: {e}")

# Função para sobrescrever o conteúdo do arquivo
def sobrescrever_arquivo():
    try:
        # Solicita ao usuário o novo conteúdo do arquivo
        print("\nDigite o novo conteúdo do arquivo (digite 'fim' para encerrar):")
        linhas = []
        while True:
            linha = input()
            if linha.lower() == "fim":
                break
            linhas.append(linha)

        # Abre o arquivo em modo de escrita ('w')
        with open("dados.txt", "w", encoding="utf-8") as arquivo:
            # Escreve as novas linhas no arquivo
            arquivo.write("\n".join(linhas))
        print("Arquivo sobrescrito com sucesso!")
    except Exception as e:
        print(f"Erro ao sobrescrever o arquivo: {e}")

# Função principal do sistema
def main():
    while True:
        # Menu de opções
        print("\n--- Menu ---")
        print("1. Ler conteúdo do arquivo")
        print("2. Adicionar linha ao arquivo")
        print("3. Sobrescrever o arquivo")
        print("4. Sair")

        # Solicita ao usuário que escolha uma opção
        try:
            opcao = int(input("Escolha uma opção (1, 2, 3 ou 4): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue  # Volta ao início do loop

        # Opção 1: Ler conteúdo do arquivo
        if opcao == 1:
            ler_arquivo()

        # Opção 2: Adicionar linha ao arquivo
        elif opcao == 2:
            adicionar_linha()

        # Opção 3: Sobrescrever o arquivo
        elif opcao == 3:
            sobrescrever_arquivo()

        # Opção 4: Sair do sistema
        elif opcao == 4:
            print("\nSaindo do sistema...")
            break  # Sai do loop principal e encerra o programa

        # Opção inválida
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")

    # Mensagem final
    print("\nObrigado por utilizar o sistema de manipulação de arquivos!")

# Executa o sistema
if __name__ == "__main__":
    main()