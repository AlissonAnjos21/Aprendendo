from veiculo import Veiculo
from log import LogMixin

class Carro(Veiculo, LogMixin):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.andando = False

    def andar(self):
        if not self.ligado:
            erro = f'{self.modelo} NÃO ESTÁ LIGADO!'
            print(erro)
            self.log_erro(erro)
            return
        if self.andando:
            erro = f'{self.modelo} JÁ ESTÁ ANDANDO!'
            print(erro)
            self.log_erro(erro)
            return
        self.andando = True
        info = f'{self.modelo} ESTÁ ANDANDO...'
        print(info)
        self.log_info(info)

    def parar(self):
        if not self.andando:
            erro = f'{self.modelo} JÁ ESTÁ PARADO!'
            print(erro)
            self.log_erro(erro)
            return
        self.andando = False
        info = f'{self.modelo} ESTÁ PARADO.'
        print(info)
        self.log_info(info)
