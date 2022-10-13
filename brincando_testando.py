nome = "jaques" " moreira"
print(nome)


if 5> 2:
    print("cinco é maior que dois!")


x = 5
y = "hello, world"


a = "hello"
print(a[4])


for x in "jack":
    print(x)


a = "hello, world"
print(len(a))


txt = " A melhor coisa da vida é free"
print("free" in txt)

txt = "o melhor estar por vir"
if "vir" in txt:
    print("Yes, 'vir' is present.")

txt = "a vida é desafio"
print("thug" not in txt)


b = "hello, world"
print(b[-2:-6])


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


x = abs(-7.25)

print(x)


x = pow(5, 3)

print (x)


import math

x = math.sqrt(64)

print(x)


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary:
print(y["age"])
print(y["city"])
print(y["name"])


import json


#a python object (dict):
x = {
    "name": "Jack",
    "age": 27,
    "city": "Betim"
}

#convert into JSON:
Y = json.dumps(x)

# the result is a json string:
print(y)











