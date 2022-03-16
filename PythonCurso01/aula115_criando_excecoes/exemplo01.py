# Cria uma classe e faz ela herdar da classe Exception
class MeuErro(Exception):
    # Não preciso fazer mais nada
    pass

def teste():
    raise MeuErro('Erro detectado!')  # Lançando um erro

try:
    teste()
except MeuErro as e:
    print(f'Não foi possível executar devido ao erro: {e}')
