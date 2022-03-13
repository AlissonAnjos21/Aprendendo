from contas.conta import Conta

class ContaPoupanca(Conta):
    def retirar(self, quantia):
        if not isinstance(quantia, (int, float)):
            print('Formato de quantia inválido!!!')
            return
        if quantia > self.saldo:
            print('A quantia a ser retirada excede o limite de saldo!!!')
            self.informacoes()
            return
        self.saldo -= quantia
        self.informacoes()
