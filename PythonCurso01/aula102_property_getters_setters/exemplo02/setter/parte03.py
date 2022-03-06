# Reforço setter:

class Comida:
    def __init__(self):
        # Estou deixando o categoria como "privado", ou seja, estou pedindo para não acessarem ele
        self._categoria = ''

    @property
    def categoria(self):
        # Assim, sempre que eu chamar a categoria como um atributo, ele enviará o valor de _categoria que foi anteriormente definido pelo setter
        return self._categoria


    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria


c1 = Comida()
print(c1.categoria)  # ''
print(c1._categoria)  # ''

c1.categoria = 'Doce'
print(c1.categoria)  # Doce
print(c1._categoria)  # Doce
