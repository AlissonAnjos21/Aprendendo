from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def andar(self):
        pass

class Cachorro(Animal):
    def andar(self):
        print(f'{__class__.__name__} está andando com 4 patas')

class Aranha(Animal):
    def andar(self):
        print(f'{__class__.__name__} está andando com 8 patas')

# Os métodos andar de cada uma das classes filhas são diferentes, porém possuem o mesmo nome
cachorro = Cachorro()
cachorro.andar()

aranha = Aranha()
aranha.andar()
