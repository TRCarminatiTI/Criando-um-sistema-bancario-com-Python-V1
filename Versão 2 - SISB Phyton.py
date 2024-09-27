from datetime import datetime

# Função para exibir o cabeçalho
def exibir_cabecalho(mensagem, largura=40):
    linha = '=' * largura
    print(linha)
    print('{:^40}'.format(mensagem))
    print(linha)

# Exibe cabeçalho
exibir_cabecalho('Seja Bem Vindo ao Banco TRC Digital', 40)

# Informações do cliente e da conta
cliente = "Ana Maria de Souza Albuquerque"
conta_corrente = "001 12345-6"
data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(f"Cliente: {cliente}")
print(f"Conta Corrente: {conta_corrente}")
print(f"{data_hora_atual}")
print('=' * 40)
print()  # Linha em branco

# Função para selecionar tipo de conta
def selecionar_conta():
    while True:  # Inicia um loop que só será interrompido com uma escolha válida
        print("Escolha o tipo de conta:")
        print("1. Conta Corrente")
        print("2. Conta Poupança")
        escolha = input("Selecione:_ ")
        
        if escolha == "1":
            return "Conta Corrente"
        elif escolha == "2":
            return "Conta Poupança"
        else:
            print("Opção inválida! Tente novamente.")
            print()  # Linha em branco

# Seleção do tipo de conta
tipo_conta = selecionar_conta()
print(f"Tipo de Conta Selecionada: {tipo_conta}")

# Inicializa as variáveis para o controle da conta
saldo = 0  # Saldo inicial da conta
limite_de_valor_por_saque = 500  # Limite máximo para um saque
quantidade_de_transacoes_realizadas = 0  # Contador de transações realizadas
extrato = ""  # Extrato da conta (histórico de transações)
LIMITE_DE_TRANSACOES_DIARIAS = 10  # Limite máximo de transações diárias

# Loop principal do sistema bancário
while True:
    # Exibe o menu de opções para o usuário
    print('\n--- Menu ---')
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Selecione:_ ")

    # Opção de depósito
    if opcao == "1":
        while True:
            if quantidade_de_transacoes_realizadas >= LIMITE_DE_TRANSACOES_DIARIAS:
                print("Limite de transações diárias permitidas excedido.")
                break

            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                    quantidade_de_transacoes_realizadas += 1
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
                    print()  # Linha em branco
                    break
                else:
                    print("Falha na operação! O valor informado não é válido.")
            except ValueError:
                print("Valor inválido! Informe um número.")
                           
        # Pergunta se deseja voltar ao menu ou sair
        while True:
                repetir = input("Selecione: \n1. Voltar ao menu\n2. Sair do sistema\n:_ ")
                if repetir == '1':
                        break  # Volta ao menu
                elif repetir == '2':
                    print("Finalizando o sistema...")
                    exit()  # Finaliza o sistema
                else:
                    print("Opção inválida! Escolha 1 para voltar ao menu ou 2 para finalizar o sistema.")
                    break  # Sai do loop de saque   
              
    # Opção de saque    
    elif opcao == "2":
        while True:
            if quantidade_de_transacoes_realizadas >= LIMITE_DE_TRANSACOES_DIARIAS:
                print("Limite de transações diárias permitidas excedido.")
                print()  # Linha em branco
                break
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                # Verifica se o saque excede o saldo, o limite de saque ou a quantidade de saques permitidos
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite_de_valor_por_saque

                if excedeu_saldo:
                    print("Falha na operação! Saldo insuficiente.")
                    print()  # Linha em branco
                    # Pergunta se deseja voltar ao menu ou sair
                    while True:
                        repetir = input("Selecione: \n1. Voltar ao menu\n2. Sair do sistema\n:_ ")
                        if repetir == '1':
                            break  # Volta ao menu
                        elif repetir == '2':
                            print("Finalizando o sistema...")
                            exit()  # Finaliza o sistema
                        else:
                            print("Opção inválida! Escolha 1 para voltar ao menu ou 2 para finalizar o sistema.")
                    break  # Sai do loop de saque
                
                elif excedeu_limite:
                    print("Falha na operação! Limite de valor para saque excedido.")
                    print()  # Linha em branco
                    # Pergunta se deseja voltar ao menu ou sair
                    while True:
                        repetir = input("Selecione: \n1. Voltar ao menu\n2. Sair do sistema\n:_ ")
                        if repetir == '1':
                            break  # Volta ao menu
                        elif repetir == '2':
                            print("Finalizando o sistema...")
                            exit()  # Finaliza o sistema
                        else:
                            print("Opção inválida! Escolha 1 para voltar ao menu ou 2 para finalizar o sistema.")
                    break  # Sai do loop de saque
               
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                    quantidade_de_transacoes_realizadas += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                    break
                else:
                    print("Falha na operação! O valor informado não é válido.")
                    print()  # Linha em branco
                    
                    # Pergunta se deseja voltar ao menu ou sair                 
                    while True:
                        repetir = input("Selecione: \n1. Voltar ao menu\n2. Sair do sistema\n:_ ")
                        if repetir == '1':
                            break  # Volta ao menu
                        elif repetir == '2':
                            print("Finalizando o sistema...")
                            exit()  # Finaliza o sistema
                        else:
                            print("Opção inválida! Escolha 1 para voltar ao menu ou 2 para finalizar o sistema.")
                            print()  # Linha em branco
                    break  # Sai do loop de saque            
            except ValueError:
                print("Valor inválido!")
                print() # Linha em branco   

            # Pergunta se deseja voltar ao menu ou sair 
            while True:
                repetir = input("Você deseja:\n1. Tentar novamente\n2. Sair do sistema\n:_ ")
                if repetir == '1':
                    break  # Tenta novamente
                elif repetir == '2':
                    print("Finalizando o sistema...")
                    exit()  # Finaliza o sistema
                else:
                    print("Opção inválida! Escolha 1 para tentar novamente ou 2 para finalizar o sistema.")
                               
    # Opção de extrato
    elif opcao == "3":
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        # Pergunta se deseja voltar ao menu ou sair
        while True:
                repetir = input("Selecione: \n1. Voltar ao menu\n2. Sair do sistema\n:_ ")
                if repetir == '1':
                        break  # Volta ao menu
                elif repetir == '2':
                    print("Finalizando o sistema...")
                    exit()  # Finaliza o sistema
                else:
                    print("Opção inválida! Escolha 1 para voltar ao menu ou 2 para finalizar o sistema.")
                    break  # Sai do loop de saque

    # Opção para sair do sistema
    elif opcao == "4":
        print("Finalizando a operação...")
        break