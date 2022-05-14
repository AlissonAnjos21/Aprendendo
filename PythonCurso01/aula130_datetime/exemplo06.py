from datetime import datetime

date_1 = datetime.strptime('14/05/2022 21:00:00', '%d/%m/%Y %H:%M:%S')
date_2 = datetime.strptime('21/05/2022 23:00:00', '%d/%m/%Y %H:%M:%S')

print(f'\n{date_1} é maior que {date_2}?')
print(date_1 > date_2)

print(f'\n{date_1} é igual a {date_2}?')
print(date_1 == date_2)

print(f'\n{date_1} é menor que {date_2}?')
print(date_1 < date_2)
