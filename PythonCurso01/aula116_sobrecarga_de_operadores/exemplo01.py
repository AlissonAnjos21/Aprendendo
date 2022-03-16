"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

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

    # Torna possível saber a multiplicação dos lados dos retângulos
    def __mul__(self, other):
        retangulo_x = self.x * other.x
        retangulo_y = self.y * other.y
        return Retangulo(retangulo_x, retangulo_y)

    # Torna possível saber a divisão dos lados dos retângulos
    def __truediv__(self, other):
        retangulo_x = self.x / other.x
        retangulo_y = self.y / other.y
        return Retangulo(retangulo_x, retangulo_y)

    # Quando eu der print no objeto
    def __repr__(self):
        val = f"<class 'Retangulo({self.x}, {self.y})'>"
        return val

r1 = Retangulo(100, 150)
r2 = Retangulo(100, 10)

# Sempre que eu usar um operador referente ao que eu modifiquei eu obterei o resultado definido pela função modificada
r3 = r1 * r2
print(r3)

print('\n###########################\n')

r4 = r1 / r2
print(r4)