"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

"""

from time import sleep

backup = []
tarefas = []


def acao():
    valor = input('\nO quê você gostaria de fazer?\nDigite:\n1 - Para Adicionar Uma Tarefa\n2 - Para Listar as Tarefas\n3 - Para Desfazer a Última Ação\n4 - Para Refazer Uma Ação Desfeita\n\n')
    if valor.isnumeric():
        valor = int(valor)
        if valor not in [1, 2, 3, 4]:
            valor = 'default'
    else:
        valor = 'default'
    return valor


def adicionar():
    item = input('\nInforme uma tarefa: \n')
    tarefas.append(item)


def listar():
    if tarefas == []:
        print('\nA lista de tarefas está vazia, tente adicionar uma tarefa primeiro.')
    else:
        print('\nEstas são todas as tarefas: ')
        for tarefa in tarefas:
            print(tarefa)
            sleep(0.25)


def desfazer():
    if tarefas == []:
        print('\nNão é possível desafazer, pois a lista de tarefas está vazia!')
    else:
        backup.append(tarefas.pop())


def refazer():
    if backup == []:
        print('\nNão existe nada para refazer!')
    else:
        tarefas.append(backup.pop())


while True:
    opcao = acao()
    if opcao == 1:
        adicionar()
    if opcao == 2:
        listar()
    if opcao == 3:
        desfazer()
    if opcao == 4:
        refazer()   
    if opcao == 'default':
        print('\nO valor digitado não corresponde as opções!')
    sleep(1.5)
