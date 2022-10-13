"""
Tipo Booleano

àlgebra Booleana, criado por George Boole

2 constantes, Verdadeiro ou Falso

True - Verdadeiro
False - Falso

OBS: Sempre com a inicial maiuscula
"""

ativo = False

print (ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo negação, se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado 
será verdadeiro, ou seja sempre o contrário.
"""

print(not ativo)

logado = False

# Ou ( OR ):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True - True
True or False - True
False or True - True
False or False - False
"""

Print(ativo or logado)

# E (and) :
"""
Tambem é uma operação binária, ou seja, depende de dois valores. Ambos os valores
devem ser verdadeiros.

True and True - True
True and False - False
False and True - False
False and False - False
"""
