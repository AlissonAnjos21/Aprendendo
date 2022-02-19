# Args não precisa se chamar args
def somar(*numeros):
    resultado = 0
    for valor in numeros:
        resultado += valor
    return resultado

variavel = somar(1, 2, 3, 4)
print(variavel)
