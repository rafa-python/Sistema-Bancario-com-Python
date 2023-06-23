contas = [
    {
        'cpf': "04785236951",
        'conta': '3',
        'agencia': '0001',
        'nome': 'carlos', 
        'senha': "1234",
        'saldo': 'saldo',
        'extrato': 'extrato'
    },
    {   
        'cpf': "57852145639",
        'conta': '4',
        'agencia': '0001',
        'nome': 'Jorge', 
        'senha': "12345",
        'saldo': '100.00',
        'extrato': '========Extrato========\n'
    }
    ]
# forma de pegar o maior numero em contas
# maior = max(contas, key=lambda x: int(x['conta']))
# print(maior['conta'])

# verifica se conta existe
def verifica_se_existe(oque_busco, onde_busco):
    global contas
    for conta in contas:
        if conta[oque_busco] == onde_busco:
            return True
        
    return False
    

# menu do usuario
def menu_usuario():
    menu = """\n
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """
    return input(menu)


def login_adm():
    ...

def menu_login_ou_criar_conta_e_adm():
    menu = """
    ================ MENU ================
    [1] Acessar conta
    [2] Criar conta
    [3] Sair
    --------------------------------------
    [4] Para administradores
    --------------------------------------
    => """
    return input(menu)

# depositar
def depositar(valor, cpf):
    for conta in contas:
        if conta['cpf'] == cpf:
            saldo = float(conta['saldo'])
            novo_saldo = saldo + valor
            conta['saldo'] = novo_saldo
            conta['extrato'] += f"Deposito de R${valor:.2f}\n"
            print("=================================================")
            print(f"Deposito de R${valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R${novo_saldo:.2f}")
            print("=================================================\n")
            break


if __name__ == "__main__":
    while True:
        op = menu_usuario()
        if op == "1":
            valor = float(input("Informe o valor do deposito: R$ ")) 
            depositar(valor, "57852145639")