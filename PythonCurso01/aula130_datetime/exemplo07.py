from datetime import datetime
from locale import setlocale, LC_ALL

# Datas em outro idioma:

setlocale(LC_ALL, '')  # Determina o formato com base no idioma do usuário
# setlocale(LC_ALL, 'pt_BR.utf-8')

date = datetime.now()  # Pega a data de agora
print(date.strftime('%A, %d de %B de %Y'))
