class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__


    def respirar(self):
        print(f'{self.nome_classe} Está Respirando...')


# Estou estendendo a classe Professor para que ela herde tudo que existe na classe Pessoa
class Professor(Pessoa):
    def ensinar(self):
        # Consigo usar os atributos e métodos de Pessoa
        print(f'{self.nome_classe} Está ensinando...')


# Estou estendendo a classe Estudante para que ela herde tudo que existe na classe Pessoa
class Estudante(Pessoa):
    def estudar(self):
        # Consigo usar os atributos e métodos de Pessoa
        print(f'{self.nome_classe} Está estudando...')


professor = Professor('Joilson', 27)

# Relembrando, é possível usar os métodos e atributos da classe pai Pessoa
print(professor.nome)
professor.respirar()

# Também é possível usar os métodos exclusivos do mesmo
professor.ensinar()

print('\n=====================================\n')

estudante = Estudante('Jonathan', 20)

estudante.respirar()
estudante.estudar()

print('\n=====================================\n')

pessoa = Pessoa('Enzo', 2)
pessoa.respirar()

# ERRO!!! A classe pai não herda nada das classes filhas. Apenas as classes filhas herdam os métodos e atributos da classe pai
# pessoa.ensinar()
# pessoa.estudar()
