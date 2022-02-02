def apresentacao():
    print('Eu sou outro código!')


# Só executará isso quando isso estiver sendo executado no próprio arquivo novasFuncoes02. Caso executado em outro arquivo, o que o __name__ retornar será novasFuncoes02, fazendo que ele não seja executado
if __name__ == '__main__':
    print('Não serei executada em outros arquivos além desse')
    print('Nem eu')
    
