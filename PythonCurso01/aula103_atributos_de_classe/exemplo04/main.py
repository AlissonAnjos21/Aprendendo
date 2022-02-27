class Pessoa:
    nome = 'Nome Padrão'


p1 = Pessoa()
p2 = Pessoa()

p1.nome = 'Valdir'
print(p1.nome)  # Valdir
print(p2.nome)  # Nome Padrão
print(Pessoa.nome)  # Nome Padrão

print('\n===============\n')

Pessoa.nome = 'SEM NOME'

print(p1.nome)  # Valdir (inseri na própria instância, logo, só muda quando eu mudar nela)
print(p2.nome)  # SEM NOME
print(Pessoa.nome)  # SEM NOME
