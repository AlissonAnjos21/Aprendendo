"""
Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __truediv__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self, x, y):
        return x * y

    # Verifica se são iguais
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # Verifica se é menor que
    def __lt__(self, other):
        area_1 = self.area(self.x, self.y)
        area_2 = self.area(other.x, other.y)

        if area_1 < area_2:
            return True
        else:
            return False
    
    # Verifica se é maior que
    def __gt__(self, other):
        area_1 = self.area(self.x, self.y)
        area_2 = self.area(other.x, other.y)

        if area_1 > area_2:
            return True
        else:
            return False

r1 = Retangulo(100, 150)
r2 = Retangulo(100, 150)

print(f'É igual? {r1 == r2}')
print(f'É menor? {r1 < r2}')
print(f'É maior? {r1 > r2}')
