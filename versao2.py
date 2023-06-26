cpf = ""
senha = ""
contas = [
    {
        "cpf": "04785236951",
        "conta": "3",
        "agencia": "0001",
        "nome": "carlos",
        "senha": "1234",
        "saldo": "1500",
        "extrato": "extrato",
    },
    {
        "cpf": "57852145639",
        "conta": "4",
        "agencia": "0001",
        "nome": "Jorge",
        "senha": "12345",
        "saldo": "100",
        "extrato": "========Extrato========\n\tSaldo inicial: R$100.00\n",
    },
]


# verifica se conta existe
def verifica_se_existe(oque_busco, onde_busco):
    global contas
    for conta in contas:
        if conta[onde_busco] == oque_busco:
            return True

    return False


def while_menu_usuario():
    global cpf
    while True:
        op = menu_usuario()
        if op == "1":
            valor = float(input("Informe o valor do deposito: R$ "))
            depositar(valor, cpf)

        elif op == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            sacar(cpf, valor)

        elif op == "3":
            exibe_extrato(cpf)

        elif op == "4":
            exibe_saldo(cpf)

        elif op == "5":
            print("\t=>Saindo...")
            quit()
        else:
            print("Nenhuma opção valida.")


# menu do usuario
def menu_usuario():
    menu = """
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Exibe saldo
    [5] Sair
    => """
    return input(menu)


# depositar
def depositar(valor, cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            saldo = float(conta["saldo"])
            novo_saldo = saldo + valor
            conta["saldo"] = novo_saldo
            conta["extrato"] += f"\tDeposito de R${valor:.2f}\n"
            print("=================================================")
            print(f"Deposito de R${valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R${novo_saldo:.2f}")
            print("=================================================\n")
            input()
            break


def exibe_extrato(cpf: str):
    for conta in contas:
        if conta["cpf"] == cpf:
            saldo = float(conta["saldo"])
            print(f"\t{conta['extrato']}")
            print(f"\t=>Saldo atual: R${saldo:.2f}")
            input()
            break


def exibe_saldo(cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            saldo = float(conta["saldo"])
            print(f"\t=>Saldo atual: R${saldo:.2f}")
            input()
            break


def sacar(cpf, valor: float):
    for conta in contas:
        if conta["cpf"] == cpf:
            saldo = float(conta["saldo"])
            if valor <= saldo and valor > 0 and valor != "":
                novo_saldo = saldo - valor
                conta["saldo"] = novo_saldo
                conta["extrato"] += f"\tSaque de R${valor:.2f}\n"
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
                input()
                break
            else:
                print("Valor invalido ou saldo insuficiente.")
                input()
                break


def acessar_conta():
    global cpf, senha
    cpf = input("Informe o cpf do titular: ")
    senha = input("Informe a senha de acesso: ")

    if verifica_se_existe(cpf, "cpf") and verifica_se_existe(senha, "senha"):
        print("Carregando menu do usuario... tecle enter para ir")
        input()
        while_menu_usuario()
    else:
        print("=================================")
        print("Senha ou CPF invalido.")
        print("Retornando ao menu principal...")
        print("=================================")
        # menu_login_ou_criar_conta_e_adm()


def criar_conta():
    global cpf, senha, contas

    cpf = input("Informe o cpf: ")
    if verifica_se_existe(cpf, "cpf"):
        print("Usuario ja cadastrado, redirecionando para login.")

        while True:
            senha = input("Informe a senha de acesso: ")
            if verifica_se_existe(senha, "senha"):
                print("Carregando menu do usuario... tecle enter para ir")
                input()
                while_menu_usuario()

            else:
                print("Senha invalida, tente novamente.")
    else:
        while True:
            nome = input("Informe nome completo: ")
            if len(nome) < 3:
                print("Nome invalido")
            else:
                break

        while True:
            senha = input("Informe uma senha com mais de 6 digitos: ")
            if len(senha) < 6:
                print("Senha invalida, tente outra senha")
            else:
                break

        while True:
            saldo = input(
                "Informe o valor do deposito inicial ou enter para nao depositar: R$ "
            )
            if float(saldo) > 0 or saldo == "":
                saldo = float(saldo)
                break
            else:
                print("Informe uma opção valida")

        # forma de pegar o maior numero em contas
        maior = max(contas, key=lambda x: int(x["conta"]))
        nova_conta = int(maior["conta"]) + 1

        contas.append(
            {
                "cpf": cpf,
                "conta": nova_conta,
                "agencia": "0001",
                "nome": nome,
                "senha": senha,
                "saldo": saldo,
                "extrato": f"========Extrato========\n\tSaldo inicial: R${saldo:.2f}\n",
            }
        )
        print("Conta criada com sucesso.")
        print("Seus dados bancarios são:")
        ultimo_dicionario = contas[-1]
        print("============================")
        for c, v in ultimo_dicionario.items():
            if c == "extrato":
                break
            print(f"{c}: {v}")
        print("============================")


def menu_login_ou_criar_conta_e_adm():
    menu = """
    ================ MENU ================
    [1] Acessar conta
    [2] Criar conta
    [3] Sair
    => """
    return input(menu)


if __name__ == "__main__":
    while True:
        op = menu_login_ou_criar_conta_e_adm()

        if op == "1":
            acessar_conta()
        elif op == "2":
            criar_conta()
        elif op == "3":
            quit()
        else:
            print("Opção invalida.")
