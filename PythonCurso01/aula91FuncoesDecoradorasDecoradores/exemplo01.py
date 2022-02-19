# Funções decoradoras e decoradores

def chefe(funcao):
    def empregado():
        funcao()
        print('Executo qualquer coisa, trabalho muito bem :D')
    return empregado  # Lembrando que o empregado não deve ser retornado executando
