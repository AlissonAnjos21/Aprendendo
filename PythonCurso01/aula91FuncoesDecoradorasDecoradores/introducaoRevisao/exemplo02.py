# Função dentro de função:

def chefe():
    def empregado():
        print('Sorriam e acenem rapazes, sorriam e acenem :D')
    

def chefe_02():
    def empregado_02():
        print('Rapadura é doce mas não é mole não')
    empregado_02()


chefe()  # Não acontece 
chefe_02()  # Executa perfeitamente o empregado_02
