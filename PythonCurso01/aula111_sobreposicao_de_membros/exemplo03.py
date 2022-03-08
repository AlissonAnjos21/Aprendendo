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


    def respirar(self):
        print(f'{self.nome_classe} Está Respirando Como um Professor...')


class ProfessorMestre(Professor):
    def ensinar(self):
        print(f'{self.nome_classe} Está Ensinando Como um Mestre')


    def respirar(self):
        # Caso eu queira acessar o método respirar da classe Pessoa
        Pessoa.respirar(self)  # Se eu escrevesse super().respirar() eu só conseguiria o respirar de Professor
        # Também consigo acessar o respirar de Professor desta maneira:
        Professor.respirar(self)
        print(f'{self.nome_classe} Está Respirando Como um Mestre...')


p1 = ProfessorMestre('Maria', 34)
p1.respirar()
