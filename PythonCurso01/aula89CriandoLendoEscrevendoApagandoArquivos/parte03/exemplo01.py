# Arquivos JSON

import json

dicionario = {
    'Usuario01': {
        'nome': 'Jurandir',
        'idade': 42,
    },
    'Usuario02': {
        'nome': 'Valdir',
        'idade': 21,
    },
    'Usuario03': {
        'nome': 'Osvaldo',
        'idade': '13',
    }
}

dicionario_formato_json = json.dumps(dicionario, indent=True)  # Converte o dicionário para o formato JSON (o indent é opcional)

import os
diretorio_geral = os.path.dirname(__file__)
diretorio_local = 'arquivoJSON.json'
criacao_arquivo = os.path.join(diretorio_geral, diretorio_local)

print(dicionario_formato_json)

with open(criacao_arquivo, 'w+') as arquivo:
    arquivo.write(dicionario_formato_json)
