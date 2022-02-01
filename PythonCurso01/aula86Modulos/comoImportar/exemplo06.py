# Problemas ao sobreescrever o nome de uma função ao importar uma função do módulo
from random import randint as randomicoInteiro


# Esta função que possui o mesmo nome da que foi importada, acabaria por sobreescrever a que foi importada, por isso eu forneci um apelido para a função importada
def randint(*args):
    return 'Mensagem'


# Assim eu consigo usar ambas
for num in range(10):
    print(randomicoInteiro(0, 10))

print(randint())
