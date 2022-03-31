# Utilizando o type() para criar classes

# Método convencional
class Pessoa:
    def respirar(self):
        print('Olá, estou respirando!')

# Método diferenciado, com o type
ClassePai = type(
    # Nome da classe, classes a qual ela herda, atributos/métodos de classe respectivamente
    'ClassePai', 
    (Pessoa,),
     {
        'atributo_da_classe': 'Sou um atributo!'
    }
)

classe = ClassePai()
print(type(classe))  # <class '__main__.ClassePai'>
classe.respirar()  # 'Olá, estou respirando!'
