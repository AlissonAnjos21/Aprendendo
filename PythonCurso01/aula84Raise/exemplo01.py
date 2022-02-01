# Relançando erros

def divisao(n1, n2):
    # Tentando dividir algo, caso não seja possível ele vai para o except
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('O erro foi: ', erro)
        # Relançando o erro para usos futuros
        # Caso eu não relançasse o erro, os except posteriores não reconheceriam que aqui aconteceu um erro
        raise

# Se eu não relançasse seria como se eu tivesse conseguido realizar o try com sucesso (porque ele realmente foi realizado com sucesso), assim, ele não entraria no except pois os erros só seriam referentes a execução deste try, mas quando eu relanço eu aviso que ocorreu um erro e torno possível que o except abaixo identifique este erro
try:
    print(divisao(1, 0))
# Recebo o mesmo erro e consigo imprimir aqui
except ZeroDivisionError as mesmoErro:
    print(mesmoErro)
