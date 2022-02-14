"""
w   -   Apenas escreve
w+  -   Escreve e lê
r   -   Apenas lê
a+  -   Lê e escreve

"""

# Entra na pasta onde está este arquivo, caso contrário ele faria tudo na pasta principal
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto03.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

# Forma mais recomendada:
# Não precisa fechar o arquivo (arquivo.close())
with open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'a+') as arquivo:
    
