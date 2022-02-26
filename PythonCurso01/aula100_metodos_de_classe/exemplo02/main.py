# Métodos de Classe - Mais um exemplo
# Resumo: as instâncias conseguem ter acesso aos seus próprios atributos tanto aos da classe. Porém a classe não consegue ter acesso aos atributos da instãncia, e sim, apenas aos seus atributos

class Conta:

    taxa_juros = 0.5
    
    def __init__(self, usuario, montante):
        self.usuario = usuario
        self.montante = montante


    def gera_juros(self):
        # A instância consegue ter acessoa a "taxa_juros", uma variável no escopo da classe
        juros = (self.montante * self.taxa_juros)
        return juros

    
    def imprimir_atributos(self):
        # A instância consegue ter acessoa a "taxa_juros", uma variável no escopo da classe
        print(f'Usuários: {self.usuario}\nMontante: {self.montante}\nTaxa de Juros: {self.taxa_juros}')


    @classmethod
    def alterar_taxa_juros(cls, nova_taxa):
        cls.taxa_juros = nova_taxa / 100
        
        # O print abaixo gera um erro, pois usuario não é um valor da classe, e sim da instância, logo, não é possível acessá-lo sem usar uma instância
        
        # print(cls.usuario)


p1 = Conta('Marcelo', 121)
print(p1.gera_juros())
p1.imprimir_atributos()

print('----------------------------------------------')

p2 = Conta('Jurandir', 50)
p2.imprimir_atributos()

print('\n##############################################\n')

Conta.alterar_taxa_juros(10)  # Altera para 10% em TODAS AS CLASSES, ou seja, eu não preciso ficar mudando de classe em classe
p1.imprimir_atributos()
print('----------------------------------------------')
p2.imprimir_atributos()
