import os

diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'seraApagado.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

with open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'w+') as arquivo:
    arquivo.write('Eu serei apagado')
    arquivo.seek(0)
    print(arquivo.read())

import time

time.sleep(10)  # Espera 10 segundos

# Excluindo o arquivo:
os.remove(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado)  # Arquivo em si / Localização do arquivo + arquivo
print('Apagado com sucesso!')
