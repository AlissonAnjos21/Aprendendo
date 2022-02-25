# Métodos de Classe
# São métodos que são referentes a classe em si, e não ao objeto instanciado

from casa import Casa

c1 = Casa('N°21', 12)
print(c1.numero, c1.tempo_uso)  # Obtemos o mesmo resultado do "tempo_uso" que foi informada durante a criação
c1.get_ano_entrada()

print()
print()
print()

c2 = Casa.tempo_uso_pelo_ano_entrada('N°42', 2001)
print(c2.numero, c2.tempo_uso)
c2.get_ano_entrada()  # Obtemos o mesmo resultado do que foi informado durante a criação
