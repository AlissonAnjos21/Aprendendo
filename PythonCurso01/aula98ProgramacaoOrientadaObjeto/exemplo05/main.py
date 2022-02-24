from animal import Animal

a1 = Animal('Vaca', 1)  # a1.nome = 'Vaca', a1.idade = 1
a2 = Animal('Humano', 21)  # a2.nome = 'Humano', a2.idade = 21

# Podemos ver que a variável "ano_atual" é igual para qualquer objeto instanciado
print(a1.ano_atual)
print(a2.ano_atual)
print(Animal.ano_atual)

print()
print()
print()

print(a1.get_nascimento_animal())
print(a2.get_nascimento_animal())
