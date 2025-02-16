from models import Conta, engine, Status, Bancos, Historico, Tipos
from sqlmodel import Session, select
from datetime import date
import matplotlib.pyplot as plt

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco==conta.banco)
        result = session.exec(statement).all()
        print(result)

        if result:
            print('Já existe uma conta neste banco!')
            return
        
        # Garantir que nova conta seja criada como ativa
        conta.status = Status.ATIVO
        session.add(conta)
        session.commit()
        return conta
    
def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        result = session.exec(statement).all()
        return result

def verificar_status_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if conta:
            return {
                "banco": conta.banco,
                "status": conta.status,
                "valor": conta.valor
            }
        return None

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if not conta:
            raise ValueError('Conta não encontrada!')
        if conta.valor > 0:
            raise ValueError('Conta com saldo positivo não pode ser desativada!')
        conta.status = Status.INATIVO
        session.commit()
        return conta

def reativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==id)
        conta = session.exec(statement).first()
        if not conta:
            raise ValueError('Conta não encontrada!')
        conta.status = Status.ATIVO
        session.commit()
        return conta

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    with Session(engine) as session:
        # Verifica conta de saída
        statement = select(Conta).where(Conta.id==id_conta_saida)
        conta_saida = session.exec(statement).first()
        if not conta_saida:
            raise ValueError('Conta de origem não encontrada!')
        if conta_saida.status == Status.INATIVO:
            raise ValueError('Conta de origem está inativa!')
        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente!')
        
        # Verifica conta de entrada
        statement = select(Conta).where(Conta.id==id_conta_entrada)
        conta_entrada = session.exec(statement).first()
        if not conta_entrada:
            raise ValueError('Conta de destino não encontrada!')
        if conta_entrada.status == Status.INATIVO:
            raise ValueError('Conta de destino está inativa!')
        
        conta_saida.valor -= valor
        conta_entrada.valor += valor
        
        # Registra o histórico da transferência
        historico_saida = Historico(
            id_conta=id_conta_saida,
            tipo=Tipos.Saida,
            valor=valor,
            data=date.today(),
            descricao=f"Transferência para conta {id_conta_entrada}"
        )
        historico_entrada = Historico(
            id_conta=id_conta_entrada,
            tipo=Tipos.Entrada,
            valor=valor,
            data=date.today(),
            descricao=f"Transferência da conta {id_conta_saida}"
        )
        
        session.add(historico_saida)
        session.add(historico_entrada)
        session.commit()

def movimentar_dinheiro(historico: Historico):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==historico.id_conta)
        conta = session.exec(statement).first()
        
        if not conta:
            raise ValueError('Conta não encontrada!')
        if conta.status == Status.INATIVO:
            raise ValueError('Esta conta está inativa!')

        if historico.tipo == Tipos.Entrada:
            conta.valor += historico.valor
        else:
            if conta.valor < historico.valor:
                raise ValueError('Saldo insuficiente!')
            conta.valor -= historico.valor
        
        session.add(historico)
        session.commit()
        return historico

def total_contas(apenas_ativas=True):
    with Session(engine) as session:
        if apenas_ativas:
            statement = select(Conta).where(Conta.status==Status.ATIVO)
        else:
            statement = select(Conta)
            
        contas = session.exec(statement).all()

        total = 0
        print("\nRelatório de Contas:")
        print("-" * 50)
        for conta in contas:
            status_texto = "ATIVA" if conta.status == Status.ATIVO else "INATIVA"
            print(f"Banco: {conta.banco.value}")
            print(f"Status: {status_texto}")
            print(f"Valor: R$ {conta.valor:.2f}")
            print("-" * 50)
            if conta.status == Status.ATIVO or not apenas_ativas:
                total += conta.valor
        
        print(f"\nTotal {'em contas ativas' if apenas_ativas else 'em todas as contas'}: R$ {total:.2f}")
        return total
    
def buscar_historicos_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data >= data_inicio,
            Historico.data <= data_fim
        ).order_by(Historico.data)
        
        resultados = session.exec(statement).all()
        
        if not resultados:
            print("Nenhum histórico encontrado no período especificado")
            return []
        
        print("\nHistórico de Movimentações:")
        print("-" * 50)
        for hist in resultados:
            print(f"Data: {hist.data}")
            print(f"Tipo: {hist.tipo.value}")
            print(f"Valor: R$ {hist.valor:.2f}")
            if hasattr(hist, 'descricao') and hist.descricao:
                print(f"Descrição: {hist.descricao}")
            print("-" * 50)
            
        return resultados

def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status==Status.ATIVO)
        contas = session.exec(statement).all()
        
        if not contas:
            print("Não há contas ativas para gerar o gráfico")
            return
        
        bancos = [i.banco.value for i in contas]
        total = [i.valor for i in contas]
        
        plt.figure(figsize=(10, 6))
        plt.bar(bancos, total)
        plt.title('Saldo por Conta Bancária')
        plt.xlabel('Bancos')
        plt.ylabel('Saldo (R$)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Exemplos de uso (todos indentados corretamente)
    criar_grafico_por_conta()
    
    # Outros exemplos (mantidos como comentários)
    # conta = Conta(valor=1000, banco=Bancos.BANCO_DO_BRASIL)
    # criar_conta(conta)
    # status = verificar_status_conta(1)
    # print(status)
    # total_contas(apenas_ativas=True)
    # historicos = buscar_historicos_entre_datas(date(2024, 1, 1), date(2024, 12, 31))