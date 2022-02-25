class Casa:
    ano_atual = 2022


    def __init__(self, numero, tempo_uso):
        self.numero = numero
        self.tempo_uso = tempo_uso
    
    
    # Método convencional, ou seja, método referente à instância
    def get_ano_entrada(self):
        print(self.ano_atual - self.tempo_uso)


    # Método da classe, refere-se a classe como um todo, e não aos objetos específicos
    # Ao invés do orgumento nomeado como "self", nomeia-se, por convenção, o argumento como "cls" para ilustrar a ideia de que ele é referente a classe
    # Para que ele se torne realmente um método da classe, é necessário decorá-lo com o @classmethod
    @classmethod
    def tempo_uso_pelo_ano_entrada(cls, numero, ano_entrada):
        # Perceba que "tempo_uso" neste caso é apenas uma variável local deste escopo
        tempo_uso = cls.ano_atual - ano_entrada
        return cls(numero, tempo_uso)