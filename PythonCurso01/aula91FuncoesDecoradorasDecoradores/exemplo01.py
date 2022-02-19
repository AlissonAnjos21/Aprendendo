# Funções decoradoras e decoradores

def chefe(funcao):
    def empregado():
        funcao()
        print('Trabalho muito bem :D')
    return empregado  # Lembrando que o empregado não deve ser retornado executando


def qualquer_funcao():
    print('Sou uma função de exemplo')


# Lembre-se também que a função que você envia para o chefe não pode estar sendo executada (Não pode ter parênteses)
qualquer_funcao = chefe(qualquer_funcao)  # Estou decorando a função "qualquer_funcao" com a função "chefe", ou seja, antes de executar a "qualquer_funcao", ela sempre passará dentro da função "chefe" antes

qualquer_funcao()  # Executando fica nítido que ela passou dentro da "chefe" porque ela executou o print que existe em "empregado"


