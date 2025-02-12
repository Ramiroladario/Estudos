# Classe Livro: Representa um livro na biblioteca
class Livro:
    def __init__(self, titulo: str, autor: str):
        """
        Construtor da classe Livro.
        :param titulo: Título do livro.
        :param autor: Autor do livro.
        """
        self.titulo = titulo  # Atributo: Título do livro
        self.autor = autor    # Atributo: Autor do livro
        self.disponivel = True  # Atributo: Status do livro (inicialmente disponível)

    def __str__(self):
        """
        Método especial para representar o livro como uma string.
        :return: String formatada com informações do livro.
        """
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} - {status}"

    def emprestar(self):
        """
        Método para emprestar o livro.
        :return: True se o livro foi emprestado com sucesso, False caso contrário.
        """
        if self.disponivel:
            self.disponivel = False  # Marca o livro como emprestado
            return True
        else:
            return False  # Livro já está emprestado

    def devolver(self):
        """
        Método para devolver o livro.
        :return: True se o livro foi devolvido com sucesso, False caso contrário.
        """
        if not self.disponivel:
            self.disponivel = True  # Marca o livro como disponível
            return True
        else:
            return False  # Livro já está disponível


# Classe Biblioteca: Gerencia uma coleção de livros
class Biblioteca:
    def __init__(self):
        """
        Construtor da classe Biblioteca.
        Inicializa uma lista vazia de livros.
        """
        self.livros = []  # Atributo: Lista de livros na biblioteca

    def adicionar_livro(self, livro: Livro):
        """
        Adiciona um livro à biblioteca.
        :param livro: Objeto da classe Livro a ser adicionado.
        """
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        """
        Lista todos os livros da biblioteca.
        """
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                print(livro)

    def emprestar_livro(self, titulo: str):
        """
        Empresta um livro pelo título.
        :param titulo: Título do livro a ser emprestado.
        """
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.emprestar():
                    print(f"Livro '{titulo}' emprestado com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está emprestado.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def devolver_livro(self, titulo: str):
        """
        Devolve um livro pelo título.
        :param titulo: Título do livro a ser devolvido.
        """
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.devolver():
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"Livro '{titulo}' já está disponível.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")


# Função principal para interação com o usuário
def main():
    # Cria uma instância da biblioteca
    biblioteca = Biblioteca()

    while True:
        # Menu de opções
        print("\n--- Sistema de Gerenciamento de Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adicionar livro
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            biblioteca.adicionar_livro(livro)

        elif opcao == "2":
            # Listar livros
            biblioteca.listar_livros()

        elif opcao == "3":
            # Emprestar livro
            titulo = input("Digite o título do livro a ser emprestado: ")
            biblioteca.emprestar_livro(titulo)

        elif opcao == "4":
            # Devolver livro
            titulo = input("Digite o título do livro a ser devolvido: ")
            biblioteca.devolver_livro(titulo)

        elif opcao == "5":
            # Sair do programa
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()