"""
listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinamico
e tbm de podermois colocar qualquer tipo de dado.

Linguagem C/Java: arrays
  - 

"""

"""
thislist = ("apple", "banana", "cherry")
print(thislist)


thislist = ["apple", "banana", "cherry","apple", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))
"""

"""
thislist = list(("apple", "banana", "cherry"))
print(thislist)
"""
"""
thislist = ["apple", "banana", "cherry", "coco"]
print(thislist[3])
"""
"""
thislist = ["apple", "banana", "cherry", "coco"]
print(thislist[-2])
"""
"""
thislist = ["apple", "banana", "cherry", "coco", "melon", "mango", "kiwi", "orange"]
print(thislist[2:5])
"""
"""
thislist = ["apple", "banana", "cherry", "coco"]
print(thislist[-4:-1])
"""
"""
thislist = ["apple", "banana", "cherry",]
if "apple" in thislist:
    print("Yes, 'apple is in the fruits list")
"""
"""
Para alterar o valor do item

thislist = ["apple", "banana", "cherry", "coco"]
thislist[2] = "Talita"
print(thislist)

alterando intervalo de valores, no caso altera o banana e cherry pelo valor 1 e 2.
thislist = ["apple", "banana", "cherry", "coco"]
thislist[1:3] = ["valor1", "valor2"]
print(thislist)

"""
"""
Inserindo itens sem substituir nenhum valor existente.
método insert()

thislist = ["apple", "banana", "cherry", "coco"]
thislist.insert(0, "tata")
print(thislist)
"""
"""
Adicionando novo item no final da lista usamos o append()

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""
"""
Usando o extend() para anexar elementos de outra lista a lista atual

thislist = ["apple", "banana", "cherry"]
marte = ["mango", "pineapple", "papaya"]
thislist.extend(marte)
print(thislist)
"""
"""
Removendo itens de uma lista usamos remove()

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

removendo o indice especificado usamos o pop()

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

Se não especificar o índice o pop() remove o ultimo item da lista

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

A palavra del tbm remove o indice especificado

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

Também deleta a lista inteira

thislist = ["apple", "banana", "cherry"]
del thislist

Limpar a lista usamos o método clear() a lista ainda permanece porém sem itens 

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

Percorrer uma lista, podemos percorrer o valor de uma lista usando um for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

Usando o range() e len() para criar interável adequado.
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  


usando o loop while 

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  
  
usando loop de compreensão de lista

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

  
"""
"""
Compreensão de lista quando vc desejar criar uma nova lista usando somente uma determinada letra"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "k" in x:
    newlist.append(x)

print(newlist)

