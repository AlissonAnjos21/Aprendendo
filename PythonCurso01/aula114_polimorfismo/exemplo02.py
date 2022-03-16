from abc import ABC, abstractmethod

class Contar(ABC):
    @abstractmethod
    def conta_ate_10(self):
        pass

# Classes com métodos de mesmo nome, só que funcionam de forma diferente
class For(Contar):
    def conta_ate_10(self):
        for i in range(10):
            print(i+1)

class While(Contar):
    def conta_ate_10(self):
        i = 1
        while i<=10:
            print(i)
            i+=1

obj_for = For()
obj_for.conta_ate_10()

print('\n##########################\n')

obj_while = While()
obj_while.conta_ate_10()