# Args:

# Os são úteis quando eu quero passar uma quantidade indefinida de parãmetros para uma função

# Sem args:
def soma_sem_args(num1, num2):
    return num1 + num2

# Com args:
def soma_com_args(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


sem_args = soma_sem_args(1, 2)
print(sem_args)

com_args = soma_com_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(com_args)
