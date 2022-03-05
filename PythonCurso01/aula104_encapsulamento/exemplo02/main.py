class Carro:
    def __init__(self):
        self.lista_carros = {}


    def inserir_carro(self, id, nome):
        if 'carros' in self.lista_carros:
            self.lista_carros['carros'].update({id:nome})
        else:
            self.lista_carros['carros'] = {id:nome}


    def remover_carro(self, id):
        del self.lista_carros['carros'][id]
    

    def mostrar_carros(self):
        for id, nome in self.lista_carros.items():
            print(id, nome)


c1 = Carro()
c1.inserir_carro(1, 'Corsa')
c1.inserir_carro(2, 'Mustang')
c1.inserir_carro(3, 'Camaro')

c1.lista_carros = "Vou quebrar essa classe toda 🤡"

# A classe foi quebrada pois a "lista_carros" não é mais um dicionário
# Logo, tudo abaixo não funcionará
c1.remover_carro(1)
c1.mostrar_carros()
