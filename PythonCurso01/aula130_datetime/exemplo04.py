from datetime import datetime, timedelta

date = datetime.strptime('14/05/2022 21:00:00', '%d/%m/%Y %H:%M:%S')
new_date_1 = date + timedelta(days=21)  # Adiciona 21 dias na data informada
new_date_2 = date + timedelta(seconds=21)  # Adiciona 21 segundos na data informada
new_date_3 = date + timedelta(seconds=2*60*60)  # Adiciona 2 horas na data informada

print(new_date_1)
print(new_date_2)
print(new_date_3)
