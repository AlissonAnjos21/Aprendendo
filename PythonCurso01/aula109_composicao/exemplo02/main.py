# Neste exemplo, usarei a função __del__ para demonstrar que os objetos instanciados de Autor também são deletados ao se deletar a instância de Livro a qual eles pertencem 

class Livro:
    def __init__(self, titulo, lancamento):
        self.titulo = titulo
        self.lancamento = lancamento
        self.autores = []


    def adicionar_autor(self, nome, nascimento):
        # Estou instanciando a classe Autor diretamente de outra classe
        # Quando eu apagar a classe, todos os objetos que foram instanciados desta maneira também serão apagados
        self.autores.append(Autor(nome, nascimento))


    def listar_autores(self):
        for autor in self.autores:
            print(f'Autor: {autor.nome}\nData de nascimento: {autor.nascimento}\n')


    # Essa função só executa quando o programa para e o coletor de lixo do Python é ativado
    def __del__(self):
        print(f'O livro {self.titulo} acaba de ser deletado')


    
class Autor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


    # Essa função só executa quando o programa para e o coletor de lixo do Python é ativado
    def __del__(self):
        print(f'O autor {self.nome} que nasceu no ano de {self.nascimento} acaba de ser deletado')


livro1 = Livro('O Grandioso Livro', 1021)
livro1.adicionar_autor('Marcelo Costa', 1001)

print(livro1.titulo)
livro1.listar_autores()
del livro1  # Deleta o objeto e chama o coletor de lixo do Python, consequentemente chamando a função __del__

# Com o exemplo acima, é possível perceber que mesmo que apenas o livro1 tenha sido deletado, os objetos de Autor que ele instanciou também são deletados por tabela

print('\n=============================\n')

livro2 = Livro('O Grandioso Livro Remake', 1221)
livro2.adicionar_autor('Beatriz Monteiro', 1201)

print(livro2.titulo)
livro2.listar_autores()
del livro2
