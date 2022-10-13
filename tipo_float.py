"""
TIpo float
tipo real, decimal
casas decimais
obs: O separados de casas decimais na programação é o ponto e não a virgula.
"""

# errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print (valor)

#certo do ponto de vista do float
valor = 1.44
print(valor)

# é possivel
valor1, valor2 = 4, 35
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# podemos converter o float para o int (inteiros)
"""
OBS: Ao converter valores float para inteiros, nós perdemos precição.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j