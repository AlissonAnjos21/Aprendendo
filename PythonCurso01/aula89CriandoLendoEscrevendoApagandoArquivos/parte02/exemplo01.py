# Entra na pasta onde está este arquivo, caso contrário ele faria tudo na pasta principal
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto01.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

# Criar, ler, escrever e apagar arquivos

arquivo = open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'w+')  # Write (escreve) + Leitura



arquivo.close() # Fecha o arquivo
