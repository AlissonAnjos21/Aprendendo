maximo = int(input('Informe a quantidade de números da Sequência Fibonacci você gostaria de ver: \n'))

print()

a = 0
b = 1
acc = a + b

for i in range(maximo):
    if i == 0:
        print(a)
    if i == 1:
        print(b)
    if i > 1:
        print(acc)
        a = b
        b = acc
        acc = a + b
