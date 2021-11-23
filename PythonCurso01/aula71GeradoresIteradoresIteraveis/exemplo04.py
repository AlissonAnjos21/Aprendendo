# Exemplos de aplicações de geradores

def numeros():
    for v in range(100):
        yield v

n = numeros()

# for v in n:
#     print(v)

# Ao invés do for eu poderia usar a função next
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
# Assim por diante...
