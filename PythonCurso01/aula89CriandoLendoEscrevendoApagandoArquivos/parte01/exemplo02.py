import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'texto02.txt'
caminho_criacao = os.path.join(diretorio_geral, diretorio_local)

arquivo = open(caminho_criacao, 'w+')
arquivo.write('Escrevi essa linha e saí correndo\n')
arquivo.write('Um boli pra quem ta lendo :D\n')
arquivo.write('Hummm, bolo de murango\n')

arquivo.seek(0)
linhas = arquivo.readlines()
print(linhas, '\n')

for linha in linhas:
    print(linha)

arquivo.close()
