# Classe que servirá como molde para uma pessoa
# Os atributos da classe são as variáveis de instância (variáveis da classe)
# Um método é uma função que pertence a uma classe

from animal import Animal

# Embora a classe seja a mesma, ambos são objetos diferentes
a1 = Animal()
a2 = Animal()

a1.nome ='Homo sapiens'
a1.tamanho_medio = 1.6
a1.alimentacao = 'Onivoro'

a2.nome = 'Felis catus'
a2.tamanho_medio = 0.24
a2.alimentacao = 'Carnívoro'

print(a1)
print(a2)
