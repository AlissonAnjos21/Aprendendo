class Exemplo01:
    def __init__(self):
        pass

    # Faz o objeto se comportar como um função
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)


class Exemplo02:
    def __init__(self):
        pass

    # Faz o objeto se comportar como um função
    def __call__(self, *args, **kwargs):
        if args[0] == 1:
            print('Sou 1')
        if args[0] == 2:
            print('Sou 2')
        if args[0] == 3:
            print('Sou 3')
        

exemplo01 = Exemplo01()
exemplo01(21, 210, 2100, melhor_numero=21)

exemplo02 = Exemplo02()
exemplo02(1)  # Sou 1
exemplo02(2)  # Sou 2
