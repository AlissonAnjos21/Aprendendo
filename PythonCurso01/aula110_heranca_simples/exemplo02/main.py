class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.nome_classe = self.__class__.__name__


    def andar(self):
        print(f'{self.nome_classe} Está Andando')


class Moto(Veiculo):
    def dar_grau(self):
        print(f'{self.nome_classe} Está Dando Grau')


class Carro(Veiculo):
    def ligar_radio(self):
        print(f'O Rádio de {self.nome_classe} Está Ligado')


moto = Moto(185)
moto.andar()
moto.dar_grau()

print('\n=============================================\n')

carro = Carro(260)
carro.andar()
carro.ligar_radio()
