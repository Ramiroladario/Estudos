# Função original que imprime "sanduiche big mac"
#def big_mac():
#    print("sanduiche big mac")

# Código original que chama a função big_mac várias vezes
#print("inicio")
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#print("fim")

# Função para criar um Big Mac personalizado com o nome do cliente
def fazer_big_mac(nome):
    print(f"Sanduiche big mac {nome}")

# Exemplos de chamadas da função fazer_big_mac (comentados)
# fazer_big_mac("Ramiro")
# fazer_big_mac("Leticia")
# fazer_big_mac("Melissa")

# Função para preparar batatas de um tamanho específico
def fazer_batata(tamanho):
    print(f"Batata {tamanho}")

# Função para preparar refrigerantes com tipo, tamanho e sabor
def preparar_refrigerante(tipo, tamanho, sabor):
    print(f"{tipo} {tamanho} {sabor}")

# Função para criar um combo Big Mac
def fazer_combo_big_mac(nome, tamanho_batata, tipo_refrigerante, tamanho_refrigerante, sabor_refrigerante):
    # Chama a função para fazer o Big Mac com o nome do cliente
    fazer_big_mac(nome)
    # Chama a função para fazer a batata com o tamanho especificado
    fazer_batata(tamanho_batata)
    # Chama a função para preparar o refrigerante com tipo, tamanho e sabor
    preparar_refrigerante(tipo_refrigerante, tamanho_refrigerante, sabor_refrigerante)

# Chamada da função fazer_combo_big_mac com os parâmetros necessários
fazer_combo_big_mac("Ramiro", "Grande", "Coca-cola", "Lata", "Zero")