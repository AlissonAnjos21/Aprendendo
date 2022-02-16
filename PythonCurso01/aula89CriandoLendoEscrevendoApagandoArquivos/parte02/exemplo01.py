# Entra na pasta onde está este arquivo, caso contrário ele faria tudo na pasta principal
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto01.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

# Uma possibilidade não recomendada:
# (É possível, mas não recomendado)

try:
    arquivo = open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'w+')  # Write (Escreve) | + (Leitura)
    arquivo.write('Olá amigo, você é um amigo\n')
    arquivo.write('Folha de mostarda!\n')
    arquivo.write('Salmão...\n')

    arquivo.seek(0, 0)
    print(arquivo.read())

finally:
    arquivo.close() # Fecha o arquivo
