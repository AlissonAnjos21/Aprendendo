"""
Uma classe será dona de objetos de outra classe

Caso a classe principal seja apagada, todos os objetos utilizados pela mesma também serão apagados juntos a ela

"""

from classes import Livro

livro1 = Livro('O Livro Número 1', 2001)

livro1.adicionar_autor('Jurandir da Silva', 1991)
livro1.adicionar_autor('Bernardo Leite', 1984)
livro1.adicionar_autor('Valdir Carvalho', 1979)

print(livro1.titulo)
livro1.listar_autores()

print('\n======================================\n')

livro2 = Livro('O grande Livro', 1882)

livro2.adicionar_autor('Jurandir Oliveira', 1853)

print(livro2.titulo)
livro2.listar_autores()
