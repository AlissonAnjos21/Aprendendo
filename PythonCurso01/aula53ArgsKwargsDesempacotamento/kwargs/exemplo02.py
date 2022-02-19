# Assim como nos args, também não é necessário que os kwargs se chamem assim, é apenas uma convenção, eles funcionam com qualquer nome

def fala_chave_e_valor(**chave_valor_dicionario):
    for k, v in chave_valor_dicionario.items():
        print(k, v)


fala_chave_e_valor(nome='Naruto', sobrenome='Uzumaki')
