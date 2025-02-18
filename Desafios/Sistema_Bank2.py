import textwrap

def menu ():
    menu = """ \n
    ========MENU======= 
    
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair
    
    => """
    return input(textwrap.dedent(menu))

def Depositar(saldo, valor, extrato, /):
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: \n'))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: \t R$ {valor: .2f}\n'
            print("\n ---- Depósito realizado com sucesso ----")
        else :
            print("\n **** Operação falhou! O valor informado é inválido. ****")
        return saldo, extrato

def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("\n **** Operação falhou! Você não tem saldo suficiente. ****")

    elif excedeu_limite:
            print("\n **** Operação falhou! O valor do saque excede o limite. ****")

    elif excedeu_saques:
            print("\n **** Operação falhou! Número máximo de saques excedido. ****")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n ---- Saque realizado com sucesso! ----")  

    else:
            print("\n **** Operação falhou! O valor informado é inválido. ****")
    
    return saldo, extrato

def Extrato(saldo, /, *, extrato  ):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
     

def criar_usuario(usuarios):
     
     

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")