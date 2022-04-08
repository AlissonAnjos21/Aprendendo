from dataclasses import dataclass

# Vem com o order false por padrão
@dataclass()
class Contador01:
    comeca: str
    termina: str

@dataclass(order=True)
class Contador02:
    comeca: str
    termina: str

c1_1 = Contador01(1, 21)
c2_1 = Contador01(2, 42)
c3_1 = Contador01(3, 63)
lista_c1 = [c1_1, c2_1, c3_1]

c1_2 = Contador02(1, 21)
c2_2 = Contador02(2, 42)
c3_2 = Contador02(3, 63)
lista_c2 = [c1_2, c2_2, c3_2]

# Erro!!! Não é possível usar o sorted aqui
# print(sorted(lista_c1))

# É ordenado pelo começa
print(sorted(lista_c2))  # [Contador02(comeca=1, termina=21), Contador02(comeca=2, termina=42), Contador02(comeca=3, termina=63)]
