'''DESAFIO:
Para a primeira versão será necessario que ocorra 3 operações: Depósito, Saque e Extrato
Depósito: Depositar valores Positivos, Apenas um usuario, Dados armazenado em uma variavel para extrato
Saques: 3 Saques diarios no maximo, de 500 reais por saque
Extrato: deve listar todas as operações e mostrar saldo no final 
'''
menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
""" #Aqui estamos Criando um Menu

saldo = 0 #variavel global saldo, que sempre inicia no valor 0
limite = 500 # limite de saque de 500 reais por transação 
extrato = "" # Extrato das opreçãoes
numero_saques = 0 # Numeros de saque durante a utilização do programa
LIMITE_SAQUES = 3 # limite de saques diarios 

def validar_valor(mensagem): #Função que vai receber e validar (apenas números positivos) o valor digitado pelo cliente 
    while True: # Estrutura de repetição para caso o valor digitado seja incorreto
        try: #Previnimos exceções
            valor = float(input(mensagem))
            if valor > 0: # aqui verificamos se o valor é positivo
                return valor
            else:
                print("Digíte apenas Números Positivos")
        except ValueError: # Ocorre quando o tipo de dado recebido não era esperado 
            print("Entrada inválida, digíte apenas Números") # Damos a "Dica" do tratamento

def deposito():
    global saldo 
    global extrato 

    valor = validar_valor("Quanto você deseja Depositar?") # Chamamos a função acima, e colocamos o valor na variavel local "valor"

    saldo += valor # Adicionamos na variavel saldo o valor depositado
    extrato += f"Depósito : {valor} \n" # Adicionamos o tipo e o valor da transação no extrato concatenando Strings
    return saldo

def saque():
    global saldo
    global numero_saques
    global LIMITE_SAQUES
    global extrato

    if numero_saques < LIMITE_SAQUES: # Aqui checamos se o limite de saques diario foi excedido

        valor = validar_valor("Quanto você deseja sacar?")

        if valor <= 500 and valor <= saldo: # Checamos se o limite de 500R$ por saque esta sendo respeitado
            saldo -= valor
            numero_saques += 1
            print(f"""
    Saque efetuado com Sucesso!
    Seu saldo agora é de {saldo}""",end="R$ \n" )
            extrato += f"Saque : {valor} \n"# Caso sim adicionamos a transação no extrato

        elif valor > 500 and valor <= saldo: # Caso o limite não seja respeitado o cliente recebe este aviso 
            print("Limite De 500R$ por saque excedido")
        
        elif valor > saldo: # Caso o Valor de saque seja maior que o saldo, recebe este aviso 
            print("Saldo insuficiente")

    else:
        print("Limite de Saque diario excedido, Volte Amanhã") # Caso o limite de 3 saques diarios sera excedido

def extrato_bancario():

    global extrato
    global saldo
    print(extrato,f"Saldo : {saldo} " ) 
    # Trazemos as variaveis globais e imprimimos o extrato e o saldo

while True:
    try: # Implementamos novamente 
        opcao = input(menu) # Menu e as opções disponiveis

        if opcao == "1":
            print("Depósito")
            deposito()
            print(f"Seu saldo agora é de {saldo}", end= "R$")

        elif opcao == "2":
            print("Saque")
            saque()

        elif opcao == "3":
            extrato_texto = "Extrato"
            print(extrato_texto.center(50,"*"), end="\n")
            extrato_bancario()
            print("\n**************************************************")

        elif opcao == "4":
            print("Obrigado por utilizar os nosso Serviços!")
            break

        else:
            print("Opção inválida, Selecione uma opção válida!")
    except(ValueError):
        print("Digíte apenas Números")