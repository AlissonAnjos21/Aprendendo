# Função reduce

from dados import lista
from functools import reduce

# A função reduce recebe uma função que possui dois atributos, sendo um deles um acumulador e o outro o valor a ser acumulado, após isso, deve ser feita a soma do valor com o acumulador. Além disso, deve se informar o que será somado e a partir de que número que ele começará a acumular (Normalmente se começa do 0).
total = reduce(lambda acumulador, x: x + acumulador, lista, 0)
print(total)
