# Executando a função decorada como um retorno 

def chefe(funcao):
    def empregado(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        print('Foi executada com sucesso!')
        return resultado  # Como eu atribui que o resultado é igual a função(), ela já está sendo executada, logo, ao retornar o resultado eu já estou executando ela
    return empregado


@chefe
def copiadora_21000(item_a_ser_copiado):
    print(item_a_ser_copiado)


# Em conclusão: neste caso não faz diferença você executar a função diretamente ou atribuir uma variável a função executando e depois retornar essa variável, mas talvez hajam casos em que isso faça uma grande diferença
copiadora_21000('Esse texto será copiado')
