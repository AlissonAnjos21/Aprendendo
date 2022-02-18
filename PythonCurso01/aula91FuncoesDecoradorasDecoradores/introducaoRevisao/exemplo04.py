def chefe(funcao):
    def empregado():
        funcao()
    return empregado

def tagarela():
    print('Só falo abobrinha HaHaHaHa')
    print('blabla blabla blabla blabla blabla blabla')

variavel_executadora = chefe(tagarela)

variavel_executadora()
