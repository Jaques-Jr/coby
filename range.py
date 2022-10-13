"""

ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

Obs: Valor_de_parada não inclusiva (inicio padrão 0, e passo de 1 em 1)

# Exemplo forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: Vvalor_de_parada não inclusiva (inicio especificado pelo usuário, e passo de 1 em 1)

# exemplo forma 2
for num in range(4, 11):
    print(num)


# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: Valor_de_parada não inclusiva (inicio especificado pelo usuário, e passo especificado pelo user)

#exemplo forma 3
for num in range(5, 55, 5):
    print(num)

Forma 4 (inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: Valor_de_parada não inclusiva (inicio especificado pelo usuário, e passo especificado pelo user)

for num in range(11, 0, -1):
    print(num)


"""