"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""

from time import sleep

tarefas = []
while True:
    
    opcao = input('\nO quê você gostaria de fazer?\nDigite:\n1 - Para Adicionar Uma Tarefa\n2 - Para Listar as Tarefas\n3 - Para Desfazer a Última Ação\n4 - Para Refazer Uma Ação Desfeita\n\n')

    if opcao == '1':
        tarefas.append(input('\nInforme uma tarefa: \n'))

    if opcao == '2' and tarefas == []:
        print('\nA lista de tarefas está vazia, tente adicionar uma tarefa primeiro.')
    elif opcao == '2' and tarefas != []:
        print('\nEssas são todas as tarefas: ')
        for tarefa in tarefas:
            print(tarefa)
            sleep(0.5)

    sleep(1.5)
