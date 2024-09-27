## Sistema Bancário em Python 

# Exibe uma saudação de boas-vindas ao usuário
print('=' * 40)
print('{:^40}'.format('Seja Bem Vindo ao Banco TRC Digital'))
print('=' * 40)

# Informações do cliente e da conta
cliente = "Ana Maria de Souza Albuquerque"
print(f"Cliente: {cliente}")
conta_corrente = "001 12345-6"
print(f"Conta Corrente: {conta_corrente}")

# Inicializa as variáveis para o controle da conta
saldo = 0  # Saldo inicial da conta
limite_de_valor_por_saque = 500  # Limite máximo para um saque
QUANTIDADE_DE_SAQUES_PERMITIDOS = 3  # Limite máximo de saques permitidos
quantidade_de_saques_realizados = 0  # Contador de saques realizados
extrato = ""  # Extrato da conta (histórico de transações)

# Loop principal do sistema bancário
while True:
    # Exibe o menu de opções para o usuário
    print('\n--- Menu ---')
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Informe a opção desejada: ")

    # Opção de depósito
    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            # Verifica se o valor do depósito é positivo
            if valor > 0:
                saldo += valor  # Atualiza o saldo com o valor do depósito
                extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona o depósito ao extrato
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Falha na operação! O valor informado não é válido.")
        except ValueError:
            print("Falha na operação! Informe um número válido.")

    # Opção de saque    
    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            # Verifica se o saque excede o saldo, o limite de saque ou a quantidade de saques permitidos
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite_de_valor_por_saque
            excedeu_saques = quantidade_de_saques_realizados >= QUANTIDADE_DE_SAQUES_PERMITIDOS

            # Mensagens de erro para cada condição de falha
            if excedeu_saldo:
                print("Falha na operação! Saldo insuficiente")
            elif excedeu_limite:
                print("Falha na operação! Limite de valor para saque excedido")
            elif excedeu_saques:
                print("Falha na operação! Quantidade de saques permitidos excedida") 
            elif valor > 0:
                saldo -= valor  # Atualiza o saldo com o valor do saque
                extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona o saque ao extrato
                quantidade_de_saques_realizados += 1  # Incrementa o contador de saques
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Falha na operação! O valor informado não é válido")
        except ValueError:
            print("Falha na operação! Informe um número válido.")  
    
    # Opção de extrato
    elif opcao == "3":
        # Exibe o extrato, ou uma mensagem caso não haja movimentações
        print("\n================ Extrato ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção para sair do sistema
    elif opcao == "4":
        print("Finalizando a operação...")
        break

    # Caso a opção informada não seja válida    
    else:
        print("Opção inválida! Selecione novamente a operação desejada.")



