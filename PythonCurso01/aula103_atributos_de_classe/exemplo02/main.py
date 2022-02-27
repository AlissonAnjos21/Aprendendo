class Pessoa:
    nome = 'Nome Padrão'


p1 = Pessoa()
p2 = Pessoa()

p1.nome = "Marcelo"
print(p1.nome)
print(p1.__dict__)  # {'nome': 'Marcelo'}
# Quando eu tento mudar um atributo da classe através de uma instância, ela não altera o valor do atributo da classe, e sim cria um atributo diretamente na instância

print('\n========================\n')

print(p2.nome)
print(p2.__dict__)  # {}
