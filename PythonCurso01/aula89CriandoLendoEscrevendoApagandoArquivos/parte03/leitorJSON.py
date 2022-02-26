import json
import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'arquivoJSON.json'
ler_arquivo = os.path.join(diretorio_geral, diretorio_local)

with open(ler_arquivo, 'r') as arquivo:
    captura_json = arquivo.read()
    print(captura_json)  # Ainda está em formato JSON

    arquivo_convertido_dict = json.loads(captura_json)  # Voltou a ser um dicionário

for chave, valor in arquivo_convertido_dict.items():
    print(chave)
    for chave1, valor1 in valor.items():
        print(chave1, valor1)
