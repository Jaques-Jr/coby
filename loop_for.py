"""
Loop for

Loop - Estrutura de repetição
For - Uma dessas estruturas

C ou Java

for (int i = 0; i < 10; i++){
    //execução do loop
}

python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencia ou sobre valores iteráveis

exemplos de iteráveis:

-string
    nome = 'jaques'
-lista
    lista = [1, 3, 5, 7, 9]
-range
    numeros = range(1, 10)
"""

nome = 'Jaques'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  #temos que transformar em uma lista

#Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)
 
#exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

#exemplo de for 3 (iterando sobre um range)

for numero in range(1, 10):
    print(numero)
