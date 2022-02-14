# Entra na pasta onde está este arquivo, caso contrário ele faria tudo na pasta principal
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto02.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

# Forma mais recomendada:
# Não precisa fechar o arquivo (arquivo.close())
with open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'w+') as arquivo:
    arquivo.write('Olá Mundo!\n')
    arquivo.write('Hello World!\n')
    arquivo.write('Azeitona!!!\n')

    arquivo.seek(0, 0)
    print(arquivo.read())
