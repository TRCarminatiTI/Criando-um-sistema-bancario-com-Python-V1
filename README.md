REDMI
# Criando um Sistema Bancário com Python - Versão 01 🪙

### Bootcamp Engenharia de Dados NTT Data e DIO 

#### 💻Tecnologias utilizadas:
- Python 3.12.5
- VS Code
- GitHub

# Objetivo do Projeto
Este projeto visa implementar um sistema bancário simplificado utilizando Python. O sistema permitirá ao usuário realizar operações básicas, como depósitos, saques, consulta de extrato e encerramento do sistema. Além disso, o sistema manterá o controle do saldo da conta, limitará saques e exibirá um extrato das transações realizadas.

### ⚙️Como Executar o Projeto
- Clone o Repositório: git clone TRCarminatiTI/Criando-um-sistema-bancario-com-Python-V1: Criando um sistema bancário com Python V1 (github.com)
- cd desafio-dio-criando-um-sistema-bancario-com-python 
- Execute o Script: Certifique-se de ter o Python 3 instalado e execute o script principal: python desafio.py

# VERSÃO 01

## Regras para Criação do Projeto:
**💰Depósito**
- Permite depósitos de valores positivos.
- Registra o valor do depósito no extrato.

**💶Saque**
- Permite até 3 saques diários.
- Limite de valor para saque: R$ 500,00.
- Verifica se o saldo é suficiente antes de realizar o saque.
- Registra o valor do saque no extrato.

**🧾Extrato**
- Exibe todas as operações realizadas (depósitos e saques).
- Mostra o saldo atual da conta.
- Valores são apresentados no formato R$ xxxx.xx.

## 💡Melhorias Implementadas
- **Cabeçalho de Boas-Vindas**: Adicionado com o nome do banco.
- **Identificação do cliente**: Nome do Cliente incluído para uma visualização do extrato mais próxima da realidade. Visto que o desafio trabalha com 1 usuário.
- **Identificação da Conta**: Número da conta incluído para uma visualização do extrato mais próxima da realidade.
- **Reconfiguração do Menu**: Melhorias na visibilidade e interação.
- **Entrada de Dados**: “Pergunta” para o cliente informar a opção desejada.
- **Formato Monetário**: Adicionado símbolo R$ para maior clareza.
- **Mensagem de Encerramento**: Adicionada frase "Saindo do sistema" ao finalizar.
- **Adição de Comentários**: Comentários adicionados para tornar o código mais fácil de entender e manter.

### ⚙️Uso do Sistema
Após executar o script, você verá um menu com as seguintes opções: 
1. **Depositar**: Adiciona um valor à conta. 
2. **Sacar**: Subtrai um valor da conta, se as condições permitirem. 
3. **Extrato**: Mostra o histórico de transações e o saldo atual. 
4. **Sair**: Finaliza o programa, exibindo uma mensagem de encerramento. 

# VERSÃO 02

### Regras para criação da segunda versão do projeto:

**💰Depósito** e **💶Saque**
- Estabelece limite de 10 transações diárias para uma conta
- Informar ao usuário que excedeu o limite de transações diária permitidas

**🧾Extrato**
- Mostra data e horas de todas as transações.

## 💡Melhorias Implementadas
- **Cabeçalho de Boas-Vindas**: Adicionado com o nome do banco.
- **Melhoria na função exibir cabeçalho**: Melhora a organização do código, tornando-o mais fácil de entender e visivelmente mais próximo de um extrato real.
-**Tipo de conta**: Inclusão da opção para selecionar conta corrente ou poupança.
- **Registro de Data e Hora**: Incluídos no cabeçalho (quando o cliente acessa a página inicial do BDN) além do solicitado em todas as transações de depósito e saque.
-** - Opção para o cliente voltar ao menu ou sair do sistema em várias etapas.
- **Validação de limites**: Realizado antes de permitir depósitos ou saques.
- **Mensagens**: Melhoria nas mensagens informativas de erro ao usuário.

### ⚙️Uso do Sistema
Após executar o script, você verá um menu com as seguintes opções: 
1. **Escolha o tipo de conta**: Seleciona a conta da operação.
2. **Depositar**: Adiciona um valor à conta. 
3. **Sacar**: Subtrai um valor da conta, se as condições permitirem. 
4. **Extrato**: Mostra o histórico de transações e o saldo atual. 
5. **Sair**: Finaliza o programa, exibindo uma mensagem de encerramento. 

## ✔️Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com melhorias ou novas funcionalidades.

## ✔️Contato
Para mais informações ou dúvidas, entre em contato:

- **Nome**: Tatiane Rodrigues Carminati
- **Email**: TRCarminatiTI@outlook.com
-**LinkedIn**: www.linkedin.com/in/tatianerodriguescarminati-facilitieadministrativofinanceiro



