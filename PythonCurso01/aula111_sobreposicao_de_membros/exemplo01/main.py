class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__


    def respirar(self):
        print(f'{self.nome_classe} Está Respirando...')


class Professor(Pessoa):
    def ensinar(self):
        print(f'{self.nome_classe} Está Ensinando...')


# Estou herdando a classe Professor diretamente e herdando a classe Pessoa por tabela
class ProfessorMestre(Professor):
    
    def ensinar(self):
        print(f'{self.nome_classe} Está Ensinando')