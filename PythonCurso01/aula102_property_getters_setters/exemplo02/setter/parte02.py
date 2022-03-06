# Reforço setter:

class Comida:
    def __init__(self):
        self.alimento = ''

    @property
    def categoria(self):
        # Assim, sempre que eu chamar a categoria como um atributo, ele enviará o valor de alimento que foi anteriormente definido pelo setter
        return self.alimento


    @categoria.setter
    def categoria(self, categoria):
        self.alimento = categoria


c1 = Comida()
print(c1.categoria)  # ''
print(c1.alimento)  # ''

"""
Resumo do que acontece abaixo:
Eu uso o setter categoria e defino que o valor de alimento é igual à "Doce", depois eu chamo o getter categoria e ele retorna o valor de alimento. Como ele retorna o valor de alimento e como ele é um getter e getters são tratados como atributos, o método categoria que é tratado como um atributo, possui o mesmo valor que o atributo alimento que foi definito pelo setter
"""
c1.categoria = 'Doce'
print(c1.categoria)  # Doce
print(c1.alimento)  # Doce
