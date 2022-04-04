from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.validacao = False

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def informar_saldo(self):
        print(f'O saldo da conta é de: R${self.saldo}')

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite):
        Conta.__init__(self, agencia, numero_conta, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def sacar(self, valor):
        if self.validacao:
            if valor <= (self.limite + self.saldo):
                self.saldo -= valor
            else:
                print('Limite indisponível')
            self.validacao = False
        else:
            print('Operação inválidada!')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.validacao:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                print('Saldo insuficiente')
            self.validacao = False
        else:
            print('Operação inválidada!')
            