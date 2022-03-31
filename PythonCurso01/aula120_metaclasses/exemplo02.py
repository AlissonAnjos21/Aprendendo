# Não quero que uma classe filha sobrescreva um atributo/método da classe Pai
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Pai':
            return type.__new__(mcs, name, bases, namespace)

        # Só funcionará na classe Filha02, caso não houvesse tal restrição, o "atributo" presente na classe Pai não poderia ser modificado por nenhuma classe descendente da classe Pai (filhas, netas, etc...)
        if name == 'Filha02' and 'atributo' in namespace:
            del namespace['atributo']

        return type.__new__(mcs, name, bases, namespace)

class Pai(metaclass=Meta):
    atributo = 'Genética do Pai'

class Filha01(Pai):
    atributo = 'Genética da Filha01'

class Filha02(Pai):
    pass

pai = Pai()
filha_1 = Filha01()
filha_2 = Filha02()

print(pai.atributo)  # atributo = 'Genética do Pai'
print(filha_1.atributo)  # atributo = 'Genética da Filha01'
print(filha_2.atributo)  # # atributo = 'Genética do Pai'
