# Funções decoradoras e decoradores

def saudacao():
    print('Bom dia meu chegado')

variavel_saudadora = saudacao  # Não pode usar parênteses

variavel_saudadora()  # Consigo executar a variável como função, já que atribui ela a função anteriormente
