# Outros usos para o desempacotamento

lista = [1, 2, 3, 4, 5]

val_primeiro, *val_meio, val_ultimo = lista  # val_primeiro = 1, val_meio = [2, 3, 4], val_ultimo = 5

print(val_primeiro, val_meio, val_ultimo)
