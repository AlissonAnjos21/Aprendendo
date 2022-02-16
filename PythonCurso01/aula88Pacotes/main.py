# Todas as importações tem que levar em conta o ponto de vista do arquivo main, pois é a partir dele que o programa será executado já que não é possível importar um pacote que esteja para "trás", ou seja, que esteja fora da pasta a ser executada

import pacoteValores.calcula_valor
import pacoteValores.pacoteConversao.converte

preco = 21

preco_aumentado = pacoteValores.calcula_valor.aumentar(preco, 10)
preco_reduzido = pacoteValores.calcula_valor.reduzir(preco, 10)

print(preco_aumentado)
print(preco_reduzido)

preco_aumentado_formatado1 = pacoteValores.calcula_valor.aumentar(preco, 10, True)
preco_reduzido_formatado1 = pacoteValores.calcula_valor.reduzir(preco, 10, True)

preco_aumentado_formatado2 = pacoteValores.pacoteConversao.converte.moeda_real(preco_aumentado)
preco_reduzido_formatado2 = pacoteValores.pacoteConversao.converte.moeda_real(preco_reduzido)

print(preco_aumentado_formatado1, preco_aumentado_formatado2)
print(preco_reduzido_formatado1, preco_reduzido_formatado2)
