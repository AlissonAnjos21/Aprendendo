# Entra na pasta onde está este arquivo, caso contrário ele faria tudo na pasta principal
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto01.txt'  # Local e nome do arquivo que eu quero criar
juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado = os.path.join(diretorio_geral, diretorio_local)

# Criar, ler, escrever e apagar arquivos

arquivo = open(juntando_os_caminhos_do_diretorio_e_nome_do_arquivo_que_sera_criado, 'w+')  # Write (escreve) + Leitura

# Poderia enviar tudo com apenas um write
arquivo.write('Primeira Linha\n')
arquivo.write('Segunda Linha\n')
arquivo.write('Terceira Linha\n')

# Retorna o cursor para o topo do arquivo
arquivo.seek(0, 0)
print('#################\n') 
print(arquivo.read())  # Lê o arquivo todo
print('#################\n')

# Retorna o cursor para o topo do arquivo novamente
arquivo.seek(0, 0)
print('*****************\n')
print(arquivo.readline())  # Lê linha por linha
print(arquivo.readline())
print(arquivo.readline())
print('*****************\n')

arquivo.seek(0, 0)
print('-----------------\n')
print(arquivo.readlines(), '\n')  # Salva todas as linhas dentro de uma lista
print('-----------------\n')

arquivo.seek(0, 0)
# Também é possível usar o for nesta lista
print('=================\n')
lista_arquivo = arquivo.readlines()
for linha in lista_arquivo:
    print(linha)
print('=================\n')

arquivo.close() # Fecha o arquivo
