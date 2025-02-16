from models import *
from view import *
from datetime import datetime
from typing import Optional
import sys
from decimal import Decimal
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('banco.log'),
        logging.StreamHandler()
    ]
)

class BankingError(Exception):
    """Classe base para exceções personalizadas do sistema bancário"""
    pass

class InsufficientFundsError(BankingError):
    """Exceção para quando não há saldo suficiente"""
    pass

class UI:
    def __init__(self):
        self.menu_options = {
            1: ("Criar conta", self._criar_conta),
            2: ("Desativar conta", self._desativar_conta),
            3: ("Transferir dinheiro", self._transferir_saldo),
            4: ("Movimentar dinheiro", self._movimentar_dinheiro),
            5: ("Total contas", self._total_contas),
            6: ("Filtrar histórico", self._filtrar_movimentacoes),
            7: ("Gráfico", self._criar_grafico),
            8: ("Sair", self._sair)
        }

    def start(self):
        """Inicia a interface do usuário"""
        logging.info("Sistema iniciado")
        while True:
            try:
                self._mostrar_menu()
                choice = self._get_menu_choice()
                if choice in self.menu_options:
                    self.menu_options[choice][1]()
                else:
                    print("\nOpção inválida. Por favor, tente novamente.")
            except KeyboardInterrupt:
                self._sair()
            except Exception as e:
                logging.error(f"Erro não esperado: {str(e)}")
                print(f"\nOcorreu um erro: {str(e)}")

    def _mostrar_menu(self):
        """Exibe o menu principal"""
        print("\n=== Sistema Bancário ===")
        for key, (description, _) in self.menu_options.items():
            print(f"[{key}] -> {description}")
        print("=" * 23)

    def _get_menu_choice(self) -> int:
        """Obtém a escolha do usuário no menu principal"""
        while True:
            try:
                return int(input("\nEscolha uma opção: "))
            except ValueError:
                print("Por favor, digite um número válido.")

    def _get_decimal_input(self, prompt: str) -> Decimal:
        """Obtém um valor decimal do usuário"""
        while True:
            try:
                valor = Decimal(input(prompt))
                if valor < 0:
                    print("O valor não pode ser negativo.")
                    continue
                return valor
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

    def _selecionar_conta(self, prompt: str, excluir_id: Optional[int] = None) -> int:
        """Permite ao usuário selecionar uma conta"""
        contas = listar_contas()
        if not contas:
            raise BankingError("Não há contas cadastradas.")

        print(f"\n{prompt}")
        for conta in contas:
            if excluir_id is None or conta.id != excluir_id:
                print(f"ID: {conta.id} | Banco: {conta.banco.value} | Saldo: R$ {conta.valor:.2f}")

        while True:
            try:
                id_conta = int(input("\nDigite o ID da conta: "))
                if any(conta.id == id_conta for conta in contas):
                    if excluir_id is not None and id_conta == excluir_id:
                        print("Não é possível selecionar a mesma conta.")
                        continue
                    return id_conta
                print("ID de conta inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

    def _criar_conta(self):
        """Cria uma nova conta bancária"""
        try:
            print("\nBancos disponíveis:")
            for banco in Bancos:
                print(f"- {banco.value}")

            while True:
                banco = input("\nDigite o nome do banco: ").title()
                try:
                    banco_enum = Bancos(banco)
                    break
                except ValueError:
                    print("Banco inválido. Tente novamente.")

            valor = self._get_decimal_input("Digite o valor inicial: ")
            conta = Conta(banco=banco_enum, valor=valor)
            criar_conta(conta)
            logging.info(f"Conta criada no banco {banco} com valor inicial de R$ {valor}")
            print("\nConta criada com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao criar conta: {str(e)}")
            print(f"\nErro ao criar conta: {str(e)}")

    def _desativar_conta(self):
        """Desativa uma conta existente"""
        try:
            id_conta = self._selecionar_conta("Selecione a conta para desativar:")
            desativar_conta(id_conta)
            logging.info(f"Conta {id_conta} desativada")
            print("\nConta desativada com sucesso!")
        except ValueError as e:
            print(f"\nErro: {str(e)}")
        except Exception as e:
            logging.error(f"Erro ao desativar conta: {str(e)}")
            print(f"\nErro ao desativar conta: {str(e)}")

    def _transferir_saldo(self):
        """Realiza transferência entre contas"""
        try:
            origem_id = self._selecionar_conta("Selecione a conta de origem:")
            destino_id = self._selecionar_conta("Selecione a conta de destino:", origem_id)
            valor = self._get_decimal_input("Digite o valor a transferir: ")
            
            transferir_saldo(origem_id, destino_id, valor)
            logging.info(f"Transferência realizada: R$ {valor} da conta {origem_id} para {destino_id}")
            print("\nTransferência realizada com sucesso!")
        except Exception as e:
            logging.error(f"Erro na transferência: {str(e)}")
            print(f"\nErro na transferência: {str(e)}")

    def _movimentar_dinheiro(self):
        """Registra uma movimentação em uma conta"""
        try:
            conta_id = self._selecionar_conta("Selecione a conta:")
            
            print("\nTipos de movimentação:")
            for tipo in Tipos:
                print(f"- {tipo.value}")

            while True:
                tipo = input("\nDigite o tipo da movimentação: ").title()
                try:
                    tipo_enum = Tipos(tipo)
                    break
                except ValueError:
                    print("Tipo inválido. Tente novamente.")

            valor = self._get_decimal_input("Digite o valor: ")
            
            historico = Historico(
                conta_id=conta_id,
                tipo=tipo_enum,
                valor=valor,
                data=date.today()
            )
            
            movimentar_dinheiro(historico)
            logging.info(f"Movimentação registrada: {tipo} de R$ {valor} na conta {conta_id}")
            print("\nMovimentação registrada com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao registrar movimentação: {str(e)}")
            print(f"\nErro ao registrar movimentação: {str(e)}")

    def _total_contas(self):
        """Mostra o total em todas as contas"""
        try:
            total = total_contas()
            print(f"\nTotal em todas as contas: R$ {total:.2f}")
        except Exception as e:
            logging.error(f"Erro ao calcular total: {str(e)}")
            print(f"\nErro ao calcular total: {str(e)}")

    def _filtrar_movimentacoes(self):
        """Filtra movimentações por período"""
        try:
            while True:
                try:
                    data_inicio = input("Digite a data de início (dd/mm/aaaa): ")
                    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
                    break
                except ValueError:
                    print("Formato de data inválido. Use dd/mm/aaaa")

            while True:
                try:
                    data_fim = input("Digite a data final (dd/mm/aaaa): ")
                    data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
                    if data_fim < data_inicio:
                        print("Data final deve ser posterior à data inicial.")
                        continue
                    break
                except ValueError:
                    print("Formato de data inválido. Use dd/mm/aaaa")

            movimentacoes = buscar_historicos_entre_datas(data_inicio, data_fim)
            
            if not movimentacoes:
                print("\nNenhuma movimentação encontrada no período.")
                return

            print("\nMovimentações encontradas:")
            for mov in movimentacoes:
                print(f"Data: {mov.data} | Tipo: {mov.tipo.value} | Valor: R$ {mov.valor:.2f}")
        
        except Exception as e:
            logging.error(f"Erro ao filtrar movimentações: {str(e)}")
            print(f"\nErro ao filtrar movimentações: {str(e)}")

    def _criar_grafico(self):
        """Cria gráfico de movimentações"""
        try:
            criar_grafico_por_conta()
            print("\nGráfico gerado com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao criar gráfico: {str(e)}")
            print(f"\nErro ao criar gráfico: {str(e)}")

    def _sair(self):
        """Finaliza o programa"""
        print("\nFinalizando o sistema...")
        logging.info("Sistema encerrado")
        sys.exit(0)

if __name__ == "__main__":
    UI().start()