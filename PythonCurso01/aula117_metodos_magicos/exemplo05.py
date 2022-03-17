# Fazendo com que todos os objetos intanciados sejam os mesmos
class Exemplo:
    def __new__(cls, *args, **kwargs):
        # Verifica se não existe na classe o atributo "exite"
        if not hasattr(cls, '_existe'):
            # Se não existir, ele cria este atributo e atribui o valor de object.__new__(cls)
            cls._existe = object.__new__(cls)
        return cls._existe

    def __init__(self):
        print('init executado')

exemplo01 = Exemplo()
exemplo02 = Exemplo()
exemplo03 = Exemplo()

print(exemplo01 == exemplo02)  # True
print(exemplo01 == exemplo03)  # True
print(exemplo02 == exemplo03)  # True

# Eles funcionam como um único objeto, assim que eu defino para um ele define para todos
exemplo01.nome = 'Valdir'
print(exemplo01.nome)  # Valdir
print(exemplo02.nome)  # Valdir
print(exemplo03.nome)  # Valdir
