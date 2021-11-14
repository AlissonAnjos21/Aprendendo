# Outra aplicação dos geradores

def valores():
    valor1 = 'Valor 1'
    yield valor1
    valor2 = 'Valor 2'
    yield valor2
    valor3 = 'Valor 3'
    yield valor3

value = valores()

# for v in value:
#     print(v)

# Poderia usar a função next tmb
print(next(value))
print(next(value))
print(next(value))
