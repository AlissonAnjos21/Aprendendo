"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""


# tarefas.append(input('Informe uma tarefa: \n'))

# for tarefa in tarefas:
    #  print(tarefa)


tarefas = []
while True:
    
    opcao = input('\nO quê você gostaria de fazer?\nDigite:\n1 - Para Adicionar Uma Tarefa\n2 - Para Listar as Tarefas\n3 - Para Desfazer a Última Ação\n4 - Para Refazer Uma Ação Desfeita\n\n')

    