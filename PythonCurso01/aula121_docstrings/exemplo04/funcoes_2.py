"""Ensinando como documentar funções.

Veniam et deserunt ex consectetur aliquip sint excepteur reprehenderit eu sint aute. Exercitation occaecat ad consectetur sint exercitation eu. Consequat magna labore ea ad velit.
Duis nostrud et cillum nulla amet. Incididunt sit aute culpa deserunt mollit aute ea ullamco do minim consectetur reprehenderit excepteur.
Consequat officia sunt non ad sit nostrud aliquip ea. Officia ullamco duis elit non cillum non veniam commodo qui qui consectetur consequat laborum deserunt.
Duis do aliqua sint aute ea excepteur tempor culpa pariatur. Ut velit do pariatur minim duis commodo enim amet. Quis sunt anim mollit labore excepteur commodo veniam Lorem. 
Lorem ut laboris ut mollit in excepteur veniam dolore est pariatur. Consequat dolore occaecat id labore ullamco esse ea reprehenderit. 
Labore incididunt Lorem qui amet aute anim ipsum elit pariatur amet occaecat. Ut enim eu aliqua excepteur ea excepteur commodo Lorem irure.
"""

variavel_1 = "valor 1"

def subtracao(x, y):
    """Subtração de x e y
    
    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número
    :type y: int or float

    :return: A subtração entre o primeiro e o segundo número
    :rtype: int or float
    """
    return x - y

def soma(x, y, z=None):
    """Soma x, y e z.
    
    Soma os valores de x, y e z. Caso o programador não queira um terceiro valor (z)
    ele pode optar por não usá-lo.

    :param x: Primeiro número
    :type x: int or float
    :param y: Segundo número
    :type y: int or float
    :param z: Terceiro número (opcional)
    :type z: int, float or None

    :return: A soma entre o primeiro, o segundo e o terceiro número
    :rtype: int or float
    """
    if z:
        return x + y + z
    return x + y

variavel_2 = "valor 2"
variavel_3 = "valor 3"
variavel_4 = "valor 4"
