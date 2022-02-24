class Animal:
    def __init__(self, nome, idade, dormindo=False, alimentar=False):
        self.nome = nome
        self.idade = idade
        self.dormindo = dormindo
        self.alimentar = alimentar


    def se_alimentar(self, comida):
        if self.alimentar:
            print(f'O animal {self.nome} já está se alimentando.')
            return
            
        print(f'O animal {self.nome} está se alimentando de {comida}.')
        self.alimentar = True


    def parar_se_alimentar(self):
        if not self.alimentar:
            print(f'O animal {self.nome} não está se alimentando.')
            return
            
        print(f'O animal {self.nome} parou de se alimentar')
        self.alimentar = False


    def dormir(self, turno):
        if self.alimentar:
            print(f'O animal {self.nome} não pode dormir se alimentando.')
            return
        
        if self.dormindo:
            print(f'O animal {self.nome} já está dormindo')
            return

        print(f'O animal {self.nome} começou a dormir no turno {turno}')
        self.dormindo = True


    def parar_dormir(self):
        if not self.dormindo:
            print(f'O animal {self.nome} não está dormindo')
            return

        print(f'O animal {self.nome} parou de dormir.')
        self.dormindo = False

