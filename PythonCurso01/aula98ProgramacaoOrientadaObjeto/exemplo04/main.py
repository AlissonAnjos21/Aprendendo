from animal import Animal

a1 = Animal('Vaca', 1)  # a1.nome = 'Vaca', a1.idade = 1
a2 = Animal('Humano', 21)  # a2.nome = 'Humano', a2.idade = 21

a1.se_alimentar('Capim')  # Começa a se alimentar

a1.se_alimentar('Folha de Árvore')  # Ainda está se alimentando de Capim
a1.parar_se_alimentar()
a1.parar_se_alimentar()  # Não está se alimentando

a1.se_alimentar('Folha de Árvore')  # Agora consegue se alimentar de Folha de Árvore

print()
print()
print()

a2.dormir('Matutino')
a2.dormir('Matutino')
a2.parar_dormir()
a2.parar_dormir()
a2.dormir('Vespertino')
