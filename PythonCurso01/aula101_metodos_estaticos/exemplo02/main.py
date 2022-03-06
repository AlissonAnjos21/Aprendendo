from random import randint

class Mundo:
    def __init__(self, nome, anos):
        self.nome = nome
        self.idade = anos

    
    @staticmethod
    def gerar_cor_ceu():
        rand = randint(0, 2)
        if rand == 0:
            return 'Céu Azul'
        if rand == 1:
            return 'Céu Vermelho'
        if rand == 2:
            return 'Céu Amarelo'


mundo1 = Mundo('Nether', 4000000000)  # 4 bilhões
print(mundo1.gerar_cor_ceu())
