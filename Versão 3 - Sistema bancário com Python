import random  # Importa a biblioteca para gerar números aleatórios
from datetime import datetime, date  # Importa classes para trabalhar com data e hora
import sqlite3  # Importa a biblioteca para trabalhar com SQLite

# Configuração do banco de dados
def inicializar_banco():
    conn = sqlite3.connect('banco.db')  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    # Cria a tabela de clientes se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
        cpf TEXT PRIMARY KEY,
        nome TEXT,
        data_nascimento TEXT,
        endereco TEXT,
        numero TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        cep TEXT,
        telefone TEXT,
        email TEXT
    )''')
    # Cria a tabela de contas se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_cpf TEXT,
        numero INTEGER UNIQUE,
        agencia TEXT,
        tipo TEXT,
        saldo REAL,
        FOREIGN KEY(cliente_cpf) REFERENCES clientes(cpf)
    )''')
    conn.commit()  # Salva as mudanças no banco de dados
    return conn  # Retorna a conexão

class Cliente:
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, telefone: str, email: str):
        # Inicializa os atributos do cliente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.email = email

class Conta:
    def __init__(self, cliente_cpf: str, numero: int, agencia: str, tipo: str, saldo: float):
        # Inicializa os atributos da conta
        self.cliente_cpf = cliente_cpf
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        self.saldo = saldo
        self.historico = []  # Lista para armazenar o histórico de transações
        self.limite_saque = 500.00  # Limite de saque
        self.limite_transacoes = 10  # Limite de transações diárias
        self.transacoes_realizadas = 0  # Contador de transações

    def depositar(self, valor: float) -> bool:
        # Método para depositar dinheiro na conta
        if valor > 0:  # Verifica se o valor é positivo
            if self.transacoes_realizadas < self.limite_transacoes:  # Verifica o limite de transações
                self.saldo += valor  # Atualiza o saldo
                # Adiciona o depósito ao histórico
                self.historico.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Depósito ({self.tipo}): R$ {valor:.2f}")
                self.transacoes_realizadas += 1  # Incrementa o contador de transações
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {self.tipo}.")
                return True  # Operação bem-sucedida
            print("Limite de transações diárias excedido.")  
            return False
        print("Falha na operação! O valor informado não é válido.")  
        return False

    def sacar(self, valor: float) -> bool:
        # Método para sacar dinheiro da conta
        if valor <= 0:
            print("Falha na operação! O valor informado não é válido.")
            return False
        if valor > self.saldo:
            print("Falha na operação! Saldo insuficiente.")
            return False
        if valor > self.limite_saque:
            print(f"Falha na operação! O limite de saque é R$ {self.limite_saque:.2f}.")
            return False
        if self.transacoes_realizadas >= self.limite_transacoes:
            print("Limite de transações diárias excedido.")
            return False

        self.saldo -= valor  # Deduz o valor do saldo
        # Adiciona o saque ao histórico
        self.historico.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Saque ({self.tipo}): R$ {valor:.2f}")
        self.transacoes_realizadas += 1  # Incrementa o contador de transações
        print(f"Saque de R$ {valor:.2f} realizado com sucesso da conta {self.tipo}.")
        return True

    def exibir_extrato(self):
        # Método para exibir o extrato da conta
        print("\n================ Extrato ================")
        print("\n".join(self.historico) if self.historico else "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self, conn):
        self.conn = conn  # Guarda a conexão do banco de dados
        self.clientes = self.carregar_clientes()  # Carrega os clientes do banco

    def carregar_clientes(self):
        cursor = self.conn.cursor()  # Cria um cursor para executar comandos SQL
        cursor.execute("SELECT * FROM clientes")  # Seleciona todos os clientes
        rows = cursor.fetchall()  # Busca todos os resultados
        clientes = {}  # Dicionário para armazenar os clientes
        for row in rows:
            # Converte a data de nascimento e cria um objeto Cliente
            data_nascimento = datetime.strptime(row[2], '%Y-%m-%d').date()
            cliente = Cliente(row[1], row[0], data_nascimento, row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            clientes[cliente.cpf] = cliente  # Adiciona o cliente ao dicionário
        return clientes  # Retorna o dicionário de clientes

    def cadastrar_cliente(self, nome: str, cpf: str, data_nascimento: date, endereco: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, telefone: str, email: str):
        # Método para cadastrar um novo cliente
        if cpf not in self.clientes:  # Verifica se o CPF já está cadastrado
            cliente = Cliente(nome, cpf, data_nascimento, endereco, numero, bairro, cidade, estado, cep, telefone, email)
            self.clientes[cpf] = cliente  # Adiciona o cliente ao dicionário

            cursor = self.conn.cursor()  # Cria um cursor
            # Insere os dados do cliente na tabela
            cursor.execute("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                           (cpf, nome, data_nascimento.strftime('%Y-%m-%d'), endereco, numero, bairro, cidade, estado, cep, telefone, email))
            self.conn.commit()  # Salva as mudanças

            # Criar conta padrão (corrente)
            numero_conta = self.gerar_numero_conta()  # Gera um número de conta único
            agencia = "0001"  
            tipo = "corrente"  
            deposito_inicial = 0  
            nova_conta = Conta(cpf, numero_conta, agencia, tipo, deposito_inicial)  # Cria a nova conta
            self.adicionar_conta(nova_conta)  # Adiciona a conta ao banco de dados

            print("Cliente e conta cadastrados com sucesso!")  
            return cliente  # Retorna o cliente cadastrado
        print("CPF já cadastrado!")  
        return self.clientes[cpf]  # Retorna o cliente existente

    def adicionar_conta(self, conta: Conta):
        cursor = self.conn.cursor()  # Cria um cursor
        # Insere os dados da conta na tabela
        cursor.execute("INSERT INTO contas (cliente_cpf, numero, agencia, tipo, saldo) VALUES (?, ?, ?, ?, ?)",
                       (conta.cliente_cpf, conta.numero, conta.agencia, conta.tipo, conta.saldo))
        self.conn.commit()  # Salva as mudanças

    def gerar_numero_conta(self) -> int:
        while True:
            numero = random.randint(10000, 99999)  # Gera um número de conta 
            cursor = self.conn.cursor()  # Cria um cursor
            # Verifica se o número já existe
            cursor.execute("SELECT COUNT(*) FROM contas WHERE numero = ?", (numero,))
            if cursor.fetchone()[0] == 0:  # Se não existe, retorna o número
                return numero

    def buscar_cliente(self, cpf: str):
        # Busca um cliente pelo CPF
        return self.clientes.get(cpf)  # Retorna o cliente se encontrado

    def listar_contas(self, cpf: str):
        cursor = self.conn.cursor()  # Cria um cursor
        # Seleciona as contas do cliente
        cursor.execute("SELECT c.numero, c.agencia, c.tipo, c.saldo, cl.nome, cl.cpf FROM contas c JOIN clientes cl ON c.cliente_cpf = cl.cpf WHERE c.cliente_cpf = ?", (cpf,))
        return cursor.fetchall()  # Retorna todas as contas

def main():
    conn = inicializar_banco()  # Inicializa o banco de dados
    banco = Banco(conn)  # Cria um objeto Banco

    now = datetime.now()  # Obtém a data e hora atuais
    print(f"\n{now.strftime('%d-%m-%Y %H:%M:%S')}".center(40))  # Exibe a data e hora

    print("=" * 40)
    print("{:^40}".format("Seja Bem Vindo ao Banco TRC Digital"))  # Mensagem de boas-vindas
    print("=" * 40)

    while True:
        entrada = input("Insira o cartão ou digite o CPF: ")  

        cliente = banco.buscar_cliente(entrada)  # Busca o cliente pelo CPF

        if not cliente:
            print("CPF não cadastrado!")  # Mensagem de erro
            print("Digite: \n1 - para realizar o cadastro \n2 - para finalizar a operação")  # Opções
            opcao = input("Escolha uma opção: ")  

            if opcao == "1":  # Se optar por cadastrar
                # Solicita os dados do cliente
                nome = input("Informe seu nome: ")
                cpf = input("Informe seu CPF: ")
                endereco = input("Informe seu endereço: ")
                numero = input("Informe seu número: ")
                bairro = input("Informe seu bairro: ")
                cidade = input("Informe sua cidade: ")
                estado = input("Informe seu estado: ")
                cep = input("Informe seu CEP: ")
                telefone = input("Informe seu telefone: ")
                email = input("Informe seu e-mail: ")
                data_nascimento = input("Informe sua data de nascimento (DD-MM-AAAA): ")
                data_nascimento = datetime.strptime(data_nascimento, '%d-%m-%Y').date()  # Converte a data
                cliente = banco.cadastrar_cliente(nome, cpf, data_nascimento, endereco, numero, bairro, cidade, estado, cep, telefone, email)  # Cadastra o cliente

                voltar_menu = input("Deseja voltar ao menu? (s/n): ") 
                if voltar_menu.lower() != 's':
                    break  # Sai do loop se não quiser voltar
            else:
                break  # Sai do loop se optar por finalizar
        else:
            print(f"\nDados do Cliente:\nCPF: {cliente.cpf}\nNome: {cliente.nome}")  # Exibe dados do cliente
            
            while True:
                print("\nMenu:")  # Exibe o menu
                print("[1] Depositar")
                print("[2] Sacar")
                print("[3] Extrato")
                print("[4] Nova conta")
                print("[5] Listar contas")
                print("[6] Novo usuário")
                print("[7] Sair")

                opcao = input("Selecione a opção desejada: ")  

                if opcao == "1":  # Se optar por depositar
                    conta_tipo = input("Informe o tipo de conta (corrente ou poupança): ").lower()  # Tipo de conta
                    contas = banco.listar_contas(cliente.cpf)  # Lista as contas do cliente
                    conta_encontrada = next((c for c in contas if c[2] == conta_tipo), None)  # Busca a conta pelo tipo
                    if conta_encontrada:  # Se a conta for encontrada
                        valor = float(input("Informe o valor do depósito: R$ "))  
                        conta = Conta(cliente.cpf, conta_encontrada[0], conta_encontrada[1], conta_encontrada[2], conta_encontrada[3])  # Cria um objeto Conta
                        conta.depositar(valor)  # Realiza o depósito
                        banco.adicionar_conta(conta)  # Atualiza o saldo no banco
                    else:
                        print("Conta não encontrada!")  

                elif opcao == "2":  # Se optar por sacar
                    conta_tipo = input("Informe o tipo de conta (corrente ou poupança): ").lower()  # Tipo de conta
                    contas = banco.listar_contas(cliente.cpf)  # Lista as contas do cliente
                    conta_encontrada = next((c for c in contas if c[2] == conta_tipo), None)  # Busca a conta pelo tipo
                    if conta_encontrada:  # Se a conta for encontrada
                        valor = float(input("Informe o valor do saque: R$ "))  
                        conta = Conta(cliente.cpf, conta_encontrada[0], conta_encontrada[1], conta_encontrada[2], conta_encontrada[3])  # Cria um objeto Conta
                        conta.sacar(valor)  # Realiza o saque
                        banco.adicionar_conta(conta)  # Atualiza o saldo no banco
                    else:
                        print("Conta não encontrada!") 

                elif opcao == "3":  # Se optar por extrato
                    conta_tipo = input("Informe o tipo de conta (corrente ou poupança): ").lower()  # Tipo de conta
                    contas = banco.listar_contas(cliente.cpf)  # Lista as contas do cliente
                    conta_encontrada = next((c for c in contas if c[2] == conta_tipo), None)  # Busca a conta pelo tipo
                    if conta_encontrada:  # Se a conta for encontrada
                        conta = Conta(cliente.cpf, conta_encontrada[0], conta_encontrada[1], conta_encontrada[2], conta_encontrada[3])  # Cria um objeto Conta
                        conta.exibir_extrato()  # Exibe o extrato
                    else:
                        print("Conta não encontrada!")  

                elif opcao == "4":  # Se optar por criar nova conta
                    numero = banco.gerar_numero_conta()  # Gera um número de conta único
                    agencia = input("Informe a agência: ")  
                    tipo = input("Informe o tipo de conta (corrente ou poupança): ").lower()  # Tipo de conta
                    deposito_inicial = float(input("Informe o valor do depósito inicial: R$ "))  # Depósito inicial
                    nova_conta = Conta(cliente.cpf, numero, agencia, tipo, deposito_inicial)  # Cria a nova conta
                    banco.adicionar_conta(nova_conta)  # Adiciona a conta ao banco de dados
                    print("Nova conta criada com sucesso!")  

                elif opcao == "5":  # Se optar por listar contas
                    contas = banco.listar_contas(cliente.cpf)  # Lista as contas do cliente
                    if contas:
                        print("\nContas do Cliente:")  # Exibe as contas
                        for conta in contas:
                            print(f"Nome: {conta[4]}, CPF: {conta[5]}, Tipo: {conta[2]}, Saldo: R$ {conta[3]:.2f}, Agência: {conta[1]}, Número da Conta: {conta[0]}")
                    else:
                        print("Nenhuma conta encontrada!")  # Mensagem de erro

                elif opcao == "6":  # Se optar por cadastrar novo usuário
                    nome = input("Informe seu nome: ")  
                    cpf = input("Informe seu CPF: ")
                    endereco = input("Informe seu endereço: ")
                    numero = input("Informe seu número: ")
                    bairro = input("Informe seu bairro: ")
                    cidade = input("Informe sua cidade: ")
                    estado = input("Informe seu estado: ")
                    cep = input("Informe seu CEP: ")
                    telefone = input("Informe seu telefone: ")
                    email = input("Informe seu e-mail: ")
                    data_nascimento = input("Informe sua data de nascimento (DD-MM-AAAA): ")
                    data_nascimento = datetime.strptime(data_nascimento, '%d-%m-%Y').date()  # Converte a data
                    cliente = banco.cadastrar_cliente(nome, cpf, data_nascimento, endereco, numero, bairro, cidade, estado, cep, telefone, email)  # Cadastra o cliente

                    voltar_menu = input("Deseja voltar ao menu? (s/n): ")  # Pergunta se deseja voltar ao menu
                    if voltar_menu.lower() != 's':
                        break  # Sai do loop se não quiser voltar

                elif opcao == "7":  # Se optar por sair
                    print()
                    print("Saindo do sistema...")  
                    print()
                    break  # Sai do loop

                else:
                    print("Opção inválida! Selecione novamente.")  # Mensagem de erro para opção inválida

    conn.close()  # Fecha a conexão com o banco

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal


