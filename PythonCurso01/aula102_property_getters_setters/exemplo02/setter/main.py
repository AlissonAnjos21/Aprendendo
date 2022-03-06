# Reforço setter:

class Comida:
    def __init__(self):
        self.alimento = ''

    @property
    def categoria(self):
        return 'Salgado'


    @categoria.setter
    def categoria(self, categoria):
        self.alimento = categoria


c1 = Comida()
print(c1.categoria)  # Salgado

print(c1.alimento)  # ''

c1.categoria = 'Doce'  # Estou chamando e atribundo ao método setter caregoria

# Recebe isso pois o método setter categoria atribui este valor à alimento
print(c1.alimento)  # Doce

# Estou chamando o método getter categoria
print(c1.categoria)  # Salgado
