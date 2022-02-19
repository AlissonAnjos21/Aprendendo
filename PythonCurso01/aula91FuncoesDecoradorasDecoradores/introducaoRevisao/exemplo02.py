# Função dentro de função:

def chefe_01():
    def empregado_01():
        print('Sorriam e acenem rapazes, sorriam e acenem :D')
    

def chefe_02():
    def empregado_02():
        print('Rapadura é doce mas não é mole não')
    empregado_02()


chefe_01()  # Não acontece 
chefe_02()  # Executa perfeitamente a empregado_02
