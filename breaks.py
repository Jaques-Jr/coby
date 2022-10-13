"""
Saindo de loops com breaks

Funciona da mesma forma que nas linguagens C ou java.

Utilizamos o breaks para sair de loops de maneira porjetada.

"""

#ex 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

#ex2

while True:
    comando = input("digite 'sair' para sair: ")
    if comando == 'sair':
        break

