from datetime import datetime

# Obtém determinada data em formato de timestamp, ou seja, a contagem em segundos desde 01/01 de 1970 até os o momento da data informada
date = datetime(2022, 5, 14)

date_to_timestamp = date.timestamp()
print('\nTimestamp até o dia 14 de maio de 2022:')
print(date_to_timestamp)

timestamp_to_date = datetime.fromtimestamp(date_to_timestamp)
print('Timestap para data:')
print(timestamp_to_date)  # 2022-05-14 00:00:00
