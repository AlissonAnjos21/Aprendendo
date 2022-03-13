from abc import ABC, abstractmethod
from msilib.schema import Class

# A classe abstrata é uma como qualquer outra, sua única diferença é a impossibilidade de ser intanciada, ou seja, é impossível criar um objeto diretamente ligado a classe abstrata 
class ClasseAbstrata(ABC):

    # Nos métodos abstratos você não implementa nada, ele existe apenas para lembrar que as outras classes também precisam criar um
    @abstractmethod
    def existir(self):
        pass

    # Também é possível criar métodos que não são abstratos, esse tipo de método será herdado normalmente pelas classes filhas
    def respirar(self):
        print('Estou respirando')

class ClasseFilha(ClasseAbstrata):
    # É obrigatório que os métodos abstratos que existam na classe pai sejam criadas aqui na classe filha
    def existir(self):
        print('Eu existo e sou uma filha')


# Não é possível instanciar uma classe abstrata
# c1 = ClasseAbstrata()

c1 = ClasseFilha()
c1.existir()
c1.respirar()
