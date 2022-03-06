"""
Reforço:
O setter é uma função que configurará o valor de algo
O getter é uma função que retorna o valor de algo

É possível ter um getter sem um setter, porém NÃO É POSSÍVEL ter um setter sem um getter

O @property indica que um método será tratado como um atributo

"""

# Reforço getter:
class Comida1:
    def categoria(self):
        return 'Salgado'


class Comida2:
    @property
    def categoria(self):
        return 'Salgado'


c1 = Comida1()
print(c1.categoria())  # O retorno do método é "salgado", logo, o print imprimirá a palavra "salgado"

print()
print('-----------------------------------------------------')
print()

c2 = Comida2()
# O print abaixo gera um erro, pois eu defini o método categoria como um @property, ou seja, o método categoria deve ser tratado como um atributo. Então ao chamar c2.categoria(), é como se eu estivesse escrevendo c2.Salgado()
# print(c2.categoria())

# Ao chamar deste modo é como se eu pedisse para imprimir um atributo chamado categoria
print(c2.categoria)  # Salgado
