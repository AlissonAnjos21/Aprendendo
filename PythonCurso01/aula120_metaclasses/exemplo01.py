# Tudo em Python é um objeto, inclusive as classes
# Metaclasses são classes utilizadas para criarem outras classes
# O type() é um tipo de metaclasses

# Vou informar que uma classe precisa ter um método, seria semelhante à utilidade dos métodos abstratos.

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # mcs > metaclasse
        # name > nome da classe (pode ser tanto a classe que herda diretamente da metaclasse quanto seus filhos)
        # bases > refere-se a todas as classes pai (ancestrais) da classe instanciada
        # namespace > referente à todos os atributos e métodos da classe instanciada

        # Neste caso, não quero modificar o funcionamento da classe Pai, apenas das filhas
        if name == 'Pai':
            return type.__new__(mcs, name, bases, namespace)

        # print(namespace, end='\n\n')
        if 'metodo_necessario' not in namespace:
            print(f'Você precisa criar o metodo_necessário na classe {name}\n')
            # Porém por enquanto ele apenas verificou se ele existe em namespace. Entretanto, ele pode tanto um método quanto um atributo
        else:
            # callable retorna true quando passa-se objetos que podem ser chamados, por ex: funções, clases, etc
            if not callable(namespace['metodo_necessario']):
                print(f'O metodo_necessario precisa ser um método, não podendo ser um atributo da classe {name}\n')
            else:
                print('Então é ele mesmo, o tão falado "metodo_necessario"\n')
        
        return type.__new__(mcs, name, bases, namespace)


class Pai(metaclass=Meta):
    pass

class Filha01(Pai):
    variavel = 'Sou uma variável'
    def metodo(self):
        print('Sou um método')
    # Feedback: "Você precisa criar o metodo_necessário na classe Filha01"

class Filha02(Pai):
    variavel = 'Sou uma variável'
    def metodo(self):
        print('Sou um método')
    metodo_necessario = 'Hehe, vou enganar o código'  # Spoiler: não vai ;D
    # Feedback: "O metodo_necessario precisa ser um método, não podendo ser um atributo da classe Filha02"

class Filha03(Pai):
    variavel = 'Sou uma variável'
    def metodo(self):
        print('Sou um método')
    def metodo_necessario(self):
        print('Sou o tão comentado "método necessário" B)')
