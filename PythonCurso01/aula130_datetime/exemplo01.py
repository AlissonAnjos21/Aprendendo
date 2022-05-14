from datetime import datetime

nova_data = datetime(2022, 5, 14, 2, 30, 20)  # Formato: ano, mês, dias, horas, minutos, segundos
print('\nData Padrão:')
print(nova_data)

# Converte a data para o formato de str
data_formatada = nova_data.strftime('%d/%m/%Y %H:%M:%S')  # as "/" e os ":" são opcionais, poderia ter qualquer coisa, ou até não ter nada
print('\nData Formatada:')
print(data_formatada)

print('\nHoras, minutos e segundos:')
print(nova_data.time())  # Ver unicamente as horas, minutos e segundos
