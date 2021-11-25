try:
    print(ola)
    
# Assim é possível salvar o erro em si em um lugar para possíveis usos futuros.
except NameError as erro:
    print('Ocorreu um NameError, isso foi devido a: ', erro)

print('Continuação do código')
