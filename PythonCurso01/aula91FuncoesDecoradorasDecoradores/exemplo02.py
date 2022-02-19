# Uma forma mais eficiente de atribuir uma função como decorador de outra função

# Função decoradora:
def chefe(funcao):
    def empregado():
        funcao()
        print('Continuo trabalhando muito bem')
    return empregado()

# Decorador:
@chefe  # Isso é equivalente a: qualquer_funcao = chefe(qualquer_funcao)
def qualquer_funcao():
    print('Sou uma função qualquer')

qualquer_funcao()
