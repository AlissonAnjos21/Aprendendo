import os

diretorio = os.path.dirname(__file__)
arquivo = 'log.log'
fusao = os.path.join(diretorio, arquivo)

class LogMixin:
    @staticmethod
    def escrever(txt):
        with open(fusao, 'a+') as file:
            file.write(txt)
            file.write('\n')

    def log_info(self, txt):
        self.escrever(f'INFORMAÇÃO: {txt}')

    def log_erro(self, txt):
        self.escrever(f'ERRO: {txt}')
