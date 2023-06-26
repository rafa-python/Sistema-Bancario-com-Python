from datetime import datetime

class Historico:
    def __init__(self, tipo: str, valor: float):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def __str__(self):
        barra = "\n================================"
        txt = f"{barra}\nTipo de transação: {self.tipo}\nValor: R${self.valor}\nData: {self.data}{barra}"
        return txt
    

class Cliente:
    def __init__(self, nome, cpf, fone, endereco):
        self._nome = nome
        self._cpf = cpf
        self._fone = fone
        self._endereco = endereco

class ContaVip:
    contas = 0
    def __init__(self, cliente: Cliente, saldo = 0):
        self._saldo = saldo
        self._numero = ContaVip.contas + 1
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = []
        ContaVip.contas += 1


    @property
    def saldo(self):
        return self._saldo    
    
    def sacar(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.append(f"{Historico('Saque', valor)}\nSaldo atual: R${self.saldo}")
            return True
        else:
            print("Saldo insuficiente")
            return False
    
    def depositar(self, valor):
        self._saldo += valor
        self._historico.append(Historico("Deposito", valor))
        return True

cliente1 = Cliente("Rafael M B", "04739383322", "85989481445", "Rua Matadouro 157")
conta1 = ContaVip(cliente1, 1000)
conta1.depositar(1000)
conta1.sacar(100)
for i in conta1._historico:
    print(i)