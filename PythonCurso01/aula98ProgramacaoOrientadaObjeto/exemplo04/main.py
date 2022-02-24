from animal import Animal

a1 = Animal('Vaca', 1)  # a1.nome = 'Vaca', a1.idade = 1
a2 = Animal('Humano', 21)  # a2.nome = 'Humano', a2.idade = 21

a1.se_alimentar('Capim')  # Começa a se alimentar
a2.se_alimentar('Salmão')

a1.se_alimentar('Folha de Árvore')  # Ainda está se alimentando de Capim
