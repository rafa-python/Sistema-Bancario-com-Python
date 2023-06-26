LIMITE_POR_SAQUE = 500
LIMITE_SAQUE = 3
saques_feitos = 0
extrato = ""
saldo = 0
menu = """
     -=Banco Dio=-
    ===============
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair
    ===============
    """


def saque():
    global LIMITE_POR_SAQUE, LIMITE_SAQUE, saques_feitos, extrato, saldo
    valor = float(input("Informe o valor que deseja sacar: R$ "))

    if saques_feitos <= LIMITE_SAQUE:
        if valor <= saldo and valor <= LIMITE_POR_SAQUE:
            saques_feitos += 1
            extrato += f"Saque realizado no valor de R${valor:.2f}\n"
            print("Saque realizado com sucesso")
        else:
            print("Valor maior que o limite permitido ou saldo inferior ao saque desejado.")
    else:
        print("Limite de saques atingido.")

def deposito():
    global LIMITE_POR_SAQUE, LIMITE_SAQUE, saques_feitos, extrato, saldo
    valor = float(input("Informe o valor do deposito: R$ "))

    saldo += valor
    extrato += f"Deposito de R${valor:.2f} feito com sucesso.\n"
    print(f"Deposito realizado com sucesso, novo saldo: R${saldo:.2f}")

def exibe_extrato():
    global extrato
    print(extrato)


while True:
    
    print(menu)
    op = input("Escolha uma opção: ")

    if op == "1":
        saque()

    elif op == "2":
        deposito()
    elif op == "3":
        exibe_extrato()
    elif op == "4":
        break
    else:
        print("Opção invalida")




