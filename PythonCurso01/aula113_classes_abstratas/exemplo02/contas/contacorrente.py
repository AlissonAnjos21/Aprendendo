from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, nome, numero, saldo, limite=210):
        super().__init__(nome, numero, saldo)
        self.limite = limite
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def retirar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('Formato de quantia inválido!!!')
            return
        if quantia > (self.saldo + self.limite):
            print('A quantia a ser retirada excede o limite da conta!!!')
            self.informacoes()
            return
        self.saldo -= quantia
        self.informacoes()
