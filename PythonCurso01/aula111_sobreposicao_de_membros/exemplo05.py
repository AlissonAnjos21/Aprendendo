class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__


    def respirar(self):
        print(f'{self.nome_classe} Está Respirando...')


class Professor(Pessoa):
    def __init__(self, nome, sobrenome, idade):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def ensinar(self):
        print(f'{self.nome_classe} Está Ensinando...')


    def respirar(self):
        print(f'{self.nome_classe} Está Respirando Como um Professor...')


class ProfessorMestre(Professor):
    # Caso eu queria que o ProfessorMestre recebe algum atributo além dos que existem na classe Pessoa e além dos que existem em Professor:
    def __init__(self, nome, sobrenome, idade, lugar_mestrado):
        Professor.__init__(self, nome, sobrenome, idade)
        self.lugar_mestrado = lugar_mestrado


p1 = ProfessorMestre('Maria', 'da Silva', 34, 'RJ')
print(p1.nome)
print(p1.sobrenome)
print(p1.idade)
print(p1.lugar_mestrado)
