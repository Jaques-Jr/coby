"""
Estruturas Logicas: and (e), or (ou), not (não), is (é)

operadores unários:
- not,
Operadores binários:
- and, or, is

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser true
Para o 'or', um ou outro valor precisa ser true
Para o 'not', o valor de booleano é invertido, ou seja, se for true , vira falsa, se for falsa vira true

"""

ativo = False
logado = True

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print("ative sua conta animal!!")


