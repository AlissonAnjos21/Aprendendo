try:
    print(ola)
    
# Nesse caso apenas caso ocorra um erro específico ele irá até o except (Nesse caso o NameError).
except NameError:
    print('Ocorreu um NameError')

print('Continuação do código')
