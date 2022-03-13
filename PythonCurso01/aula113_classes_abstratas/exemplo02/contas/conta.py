from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError('Formato de saldo inválido!')
        self._saldo = saldo

    def informacoes(self):
        print(f'Nome do Usuário: {self.nome} | Número da Conta: {self.numero} | Saldo da Conta: {self.saldo}\n')

    def depositar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('Formato inválido!!! Insira em um formato válido!')
            return
        self.saldo += quantia
        self.informacoes()

    @abstractmethod
    def retirar(self, quantia):
        pass
