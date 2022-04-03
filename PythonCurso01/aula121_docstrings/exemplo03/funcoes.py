"""Ensinando como documentar funções.

Quando se trata de documentar funções, a primeira linha da função precisa ser a documentação. Caso a 
documentação possua mais de uma linha, a mesma pode continuar a expandir, porém a primeira linha sempre
precisa fazer parte da documentação.
Veniam et deserunt ex consectetur aliquip sint excepteur reprehenderit eu sint aute. Exercitation occaecat ad consectetur sint exercitation eu. Consequat magna labore ea ad velit.
Duis nostrud et cillum nulla amet. Incididunt sit aute culpa deserunt mollit aute ea ullamco do minim consectetur reprehenderit excepteur.
Consequat officia sunt non ad sit nostrud aliquip ea. Officia ullamco duis elit non cillum non veniam commodo qui qui consectetur consequat laborum deserunt.
Duis do aliqua sint aute ea excepteur tempor culpa pariatur. Ut velit do pariatur minim duis commodo enim amet. Quis sunt anim mollit labore excepteur commodo veniam Lorem. 
Lorem ut laboris ut mollit in excepteur veniam dolore est pariatur. Consequat dolore occaecat id labore ullamco esse ea reprehenderit. 
Labore incididunt Lorem qui amet aute anim ipsum elit pariatur amet occaecat. Ut enim eu aliqua excepteur ea excepteur commodo Lorem irure.
"""

variavel_1 = "valor 1"

def subtracao(x, y):
    """Subtração de x e y"""
    return x - y

def soma(x, y, z=None):
    """Soma x, y e z.
    
    Soma os valores de x, y e z. Caso o programador não queira um terceiro valor (z)
    ele pode optar por não usá-lo.
    """
    if z:
        return x + y + z
    return x + y

variavel_2 = "valor 2"
variavel_3 = "valor 3"
variavel_4 = "valor 4"
