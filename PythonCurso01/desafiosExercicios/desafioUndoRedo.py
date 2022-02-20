"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""

from time import sleep

def acao():
    valor = input('\nO quê você gostaria de fazer?\nDigite:\n1 - Para Adicionar Uma Tarefa\n2 - Para Listar as Tarefas\n3 - Para Desfazer a Última Ação\n4 - Para Refazer Uma Ação Desfeita\n\n')
    if valor.isnumeric():
        valor = int(valor)
        if valor not in [1, 2, 3, 4]:
            valor = 'default'
    else:
        valor = 'default'
    return valor


def adiciona(item):
    tarefas.append(item)


def listar(tarefas):
    if tarefas == []:
        print('\nA lista de tarefas está vazia, tente adicionar uma tarefa primeiro.')
    else:
        print('\nEstas são todas as tarefas: ')
        for tarefa in tarefas:
            print(tarefa)
            sleep(0.25)


tarefas = []
while True:

    opcao = acao()
        
    if opcao == 1:
        item = input('\nInforme uma tarefa: \n')
        adiciona(item)

    if opcao == 2:
        listar(tarefas)
    
        







    if opcao == 'default':
        print('\nO valor digitado não corresponde as opções!')
        
    sleep(0.5)
