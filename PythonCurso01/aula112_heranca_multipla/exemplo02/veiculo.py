class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        if self.ligado:
            return
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return
        self.ligado = False
        