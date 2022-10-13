"""
recebendo dados de usuários
"""
# entrada de dados
print("qual o seu nome? ")
nome = input()

print('seja bem-vindo(a) %s' % nome)

print("qual a sua idade? ")
idade = input()

#processamento

#saida de dados
print('O(A) %s tem %s anos' % (nome, idade))

print(f'A {nome} nasceu em {2021 - int(idade)}')
