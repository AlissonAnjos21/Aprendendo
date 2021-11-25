# Função filter

from dados import lista

# A função filter recebe uma função que usará para verificar se determinada condição retorna True ou False, após isso, ela retorna um iterador com os valores completos de todos os elementos que corresponderam a condição.

maior_cinco = filter(lambda x: x > 5, lista)
print(list(maior_cinco))
