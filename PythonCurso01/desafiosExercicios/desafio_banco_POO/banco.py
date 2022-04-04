class Banco:
    def __init__(self, conta, cliente):
        self.conta = conta
        self.cliente = cliente
        self.lista_servicos = []

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    def adicionar_servico(self, conta, cliente):
        self.lista_servicos.append({conta:cliente})

    def validar(self):
        for servico in self.lista_servicos:
            for conta_servico, cliente_servico in servico.items():
                    if cliente_servico.nome == self.cliente.nome and conta_servico.numero_conta == self.conta.numero_conta and cliente_servico.conta.agencia == self.conta.agencia:
                        print('Operação validada!')
                        self.conta.validacao = True
