# Aprofundamento em Atributos de classe (Variáveis de classe)]

class Pessoa:
    nome = 'Nome Padrão'
    def __init__(self):
        self.nome = 'Valdir'


p1 = Pessoa()
p2 = Pessoa()

# Igual para todas
print(p1.nome)  
print(p2.nome)
print(Pessoa.nome)
