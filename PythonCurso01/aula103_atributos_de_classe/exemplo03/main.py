class Pessoa:
    nome = 'Nome Padrão'
    def __init__(self):
        self.nome = 'Valdir'


p1 = Pessoa()
p2 = Pessoa()

print(p1.nome)  # Valdir
print(p2.nome)  # Valdir
print(Pessoa.nome)  # Nome Padrão
