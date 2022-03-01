lista = [0, 1, 1]

maximo = int(input('Informe a quantidade de números da Sequência Fibonacci você gostaria de ver: \n'))

print()

for i in range(maximo):
    if i >= 2:
        lista.append(lista[i] + lista[i-1])
    print(lista[i])

