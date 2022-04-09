# Vou criar uma classe que terá as funcionalidades de uma lista
# Isso é algo um tanto quanto redundante de se fazer
# Isso servirá apenas para fins didáticos, e não deve ser implementado cotidianamente

class Lista:
    def __init__(self):
        self.__valores = []
        self.__indices = 0

    def adicionar(self, valor):
        self.__valores.append(valor)
    
    def __getitem__(self, indice):
        return self.__valores[indice]

    def __setitem__(self, indice, valor):
        if indice >= len(self.__valores):
            self.__valores.append(valor)
        self.__valores[indice] = valor

    def __delitem__(self, indice):
        del self.__valores[indice]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            valor = self.__valores[self.__indices]
            self.__indices += 1
            return valor
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__valores})'

    def __repr__(self):
        return self.__str__()

# Usando:
lista_comidas = Lista()
lista_comidas.adicionar('Salmão')
print(lista_comidas)
print(lista_comidas[0])
