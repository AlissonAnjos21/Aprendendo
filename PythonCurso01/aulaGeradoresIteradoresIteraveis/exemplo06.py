# Detalhando melhor

palavra = 'Uma palavrinha'
iterador = iter(palavra)

print(next(iterador))  # U
print(next(iterador))  # m
print(next(iterador))  # a
print(next(iterador))  # ' '

# Só imprimirá 'palavrinha', pois os outros caracteres já foram usados
# Depois que todos os valores forem usados este iterador se esgotará
for v in iterador:
    print(v)

# print(next(iterador))  # (ERRO! Pois o iterador já foi até o seu limite)
