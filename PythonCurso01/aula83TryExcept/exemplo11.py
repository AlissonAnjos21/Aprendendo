# Usando try/except como condicional


def conversao(input_value):
    try:
        input_value = int(input_value)
        return input_value

    except ValueError:
        try:
            input_value = float(input_value)
            return input_value

        except ValueError:
            # O uso do pass faz ele retornar None por padrão, já que ele deixa de executar a função
            pass

while True:
    numero = conversao(input('Digite um número: '))
    if numero is not None:
        print(numero * 2)
    else:
        print('O que foi digitado não é um número!')

