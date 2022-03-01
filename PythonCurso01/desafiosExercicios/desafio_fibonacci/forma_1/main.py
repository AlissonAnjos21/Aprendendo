lista_fibonacci = [0, 1, 1]

maximo = int(input('Informe quantos números da Sequência Fibonacci você gostaria de ver: \n'))

while len(lista_fibonacci) < maximo:
    print(len(lista_fibonacci))
    for i, j in enumerate(lista_fibonacci):
        if i >= 2:
            lista_fibonacci.append(lista_fibonacci[i] + lista_fibonacci[i-1])
        
    
