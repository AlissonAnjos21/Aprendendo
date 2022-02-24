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


        
