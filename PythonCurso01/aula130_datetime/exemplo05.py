from datetime import date, datetime, timedelta

date_1 = datetime.strptime('14/05/2022 21:00:00', '%d/%m/%Y %H:%M:%S')
date_2 = datetime.strptime('21/05/2022 23:00:00', '%d/%m/%Y %H:%M:%S')
difference = date_2 - date_1

print(f'Diferença entre as datas: {date_2} e {date_1}')
print(difference)

print(f'\nDiferença em segundos ENTRE OS DIAS das datas: {date_2} e {date_1}')
print(difference.days)

print(f'\nDiferença em segundos ENTRE AS HORAS das datas: {date_2} e {date_1}')
print(difference.seconds)

print(f'\nDiferença em segundos ENTRE AS DATAS EM SI das datas: {date_2} e {date_1}')
print(difference.total_seconds())
