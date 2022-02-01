# Importa tudo de um módulo
from random import *

for num in range(10):
    # Assim eu não preciso usar o random.randint, porém assim também é possível haver o problema de sobreescrever funções ao criar outras com o mesmo nome
    print(randint(0, 10))
