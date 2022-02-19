# Juntando os dois conceitos anteriores (função dentro de variável e função dentro de função)

def chefe():
    def empregado():
        print('Frase engraçadinha hahaha humor e piadas')
    return empregado

variavel_executadora = chefe()  # Funciona perfeitamente (não esquecer de colocar os parênteses)

"""
Explicação do porquê ao se atribuir uma função pura à uma variável não se usa os parênteses e em uma função que, executa uma função e retorna ela, se deve usar:

Para ficar menos confuso chamarei função que executa uma função e retorna de alfa

Quando se atribui alfa à uma variável e coloca-se os parênteses para executá-la, eu estou executando a chefe, esta retorna o empregado SEM EXECUTAR, por tal motivo quando o recebo em uma variável e a uso, eu preciso colocar os parênteses novamente, para que desta vez eu execute a função que foi retornada
"""

variavel_executadora()
