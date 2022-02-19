# Executando como um retorno a função a ser decorada

 def chefe(funcao):
     def empregado(*args, **kwargs):
         resultado = funcao(*args, **kwargs)
         print('Foi executada com sucesso!')
         return resultado  # Como eu atribui que o resultado é igual a função(), ela já está sendo executada, logo, ao retornar o resultado eu já estou executando ela
    return empregado
    