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

    
class Autor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

        