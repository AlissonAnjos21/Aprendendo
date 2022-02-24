class Animal:
    # O argumento "self" se refere a instância que chamará pela função, é como se quando eu chamasse o método ele enviasse a instância (nesse caso o p1) como um dos argumentos para falar que foi ele quem chamou. 
    # Ex (meramente ilustrativo, não deve ser replicado pois não funcionará): atributo.funcao(atributo)
    def dormir(self):
        print('O animal está a mimir!')

