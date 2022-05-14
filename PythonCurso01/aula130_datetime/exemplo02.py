from datetime import datetime, timedelta

# Converte uma str para o formato de data
str_to_date = datetime.strptime('14/05/2022', '%d/%m/%Y')  # Primeiro eu informo a str, depois eu informo em que formato de data ela está
print('\nString que virou data:')
print(str_to_date)