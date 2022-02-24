class Animal:
    # O atributo self sempre deve ser o primeiro no momento da declaração dos argumentos, porém quando se trata de fornecer estes argumentos, o mesmo não é necessário ser recebido
    def __init__(self, nome, idade, dormindo=False, alimentar=False):
        
        # Apesar de possuirem o mesmo nome, o self.nome representa ao atributo nome que existe nesta classe, enquanto o argumento nome representa apenas o valor que foi enviado durante a criação da instância 
        self.nome = nome
        self.idade = idade
        self.dormindo = dormindo
        self.alimentar = alimentar

        # É possível criar, sem o self, variáveis neste método, porém elas só estarão disponíveis no escopo do método
        teste = 'Teste'

    def metodo_exemplo_teste(self):
        # print(teste) - Erro!!! O teste está fora do escopo do método
        print(self.nome)  # Funciona perfeitamente

