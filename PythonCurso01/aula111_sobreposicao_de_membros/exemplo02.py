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


class ProfessorMestre(Professor):
    def ensinar(self):
        # Caso eu queira acessar o método ensinar da classe superior
        super().ensinar()
        print(f'{self.nome_classe} Está Ensinando Como um Mestre')


p1 = ProfessorMestre('Maria', 34)
p1.ensinar()
