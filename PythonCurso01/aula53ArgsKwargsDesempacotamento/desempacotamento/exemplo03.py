# Desempacotamento com strings

# O desempacotamento funciona com qualquer tipo de iterável, logo, também funciona com strings

lista = [*'Sou uma string da boa']

print(lista)

# Essa forma é meio dificil de ler, então, evite usá-la
*outra_lista, = 'Sou OUTRA string da boa'  # Funciona de forma parecida da outra (A vírgula é importantissíma)

print(outra_lista)
