"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis globais;
   - Variáveis globais são reconhecidas, ou seja, seu escopo compreeende todo o programa.

2 - Variáveis locais;
   - Variáveis locais são reconhecidos apenas no bloco onde foram declaraodos, ou seja, seu escopo
   está limitado ao bloco onde foi declarado.

Para declarar variáveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não
colocamos o tipo de dados dela.
Este tipo é inferido ao atribuirmos o valor á mesma.

Exemplo em C:

int numero = 42;

Exemplo em Java = 42;

"""

numero = 27
print(numero)
print(type(numero))


numero = 'jack'
print(numero)
print(type(numero))

numero = 30
if numero > 10:
    novo = numero + 10
    print(novo)


if numero < 10:
    novo = numero - 10
    print(novo)






