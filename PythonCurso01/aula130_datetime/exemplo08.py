from datetime import datetime
from calendar import mdays

# Informa o último dia do mês:

date = datetime.now()
month = int(date.strftime('%m'))

print('\nÚltimo dia do mês:')
print(mdays[month])
