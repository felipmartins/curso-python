# Aula 18 - Desempacotamento de valores

# O que vamos abordar nesta aula:
# 1. O que é desempacotamento de valores
# 2. Como funciona
# 3. Exemplos

# Desempacotamento de valores é a forma de acessar os valores de uma tupla, lista ou dicionário de forma mais simples.

# Exemplo

# Tupla

tupla = (5, 4, 3, 2, 1)

example = tupla
#5, 4, 3, 2, 1
a, b, c, d, e = tupla

print(example)
print(a)
print(b)
print(c)
print(d)
print(e)

print(50 * '-')

# Lista

lista = [1, 2, 3, 4, 5]

example = lista
#1, 2, 3, 4, 5
a, b, c, d, e = lista

print(example)
print(a)
print(b)
print(c)
print(d)
print(e)

print(50 * '-')

# Dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

a, b, c, d, e = dicionario.values()
f, g, h, i, j = dicionario.keys()

print(a)
print(b)
print(c)
print(d)
print(e)

print(f)
print(g)
print(h)
print(i)
print(j)

print(50 * '-')

# Desempacotamento de valores pode ser utilizado em funções.

# Exemplo

def soma(a, b, c, d, e):
    return a + b + c + d + e

tupla = (1, 2, 3, 4, 5)
print(soma(*tupla))

print(50 * '-')
lista = [1, 2, 3, 4, 5]
print(soma(*lista))

print(50 * '-')
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(soma(**dicionario))

print(50 * '-')

# Quando usamos menos variáveis do que o número de elementos na tupla, lista ou dicionário, podemos utilizar o operador *.

# Exemplo

tupla = (1, 2, 3, 4, 5)
a, b, *c = tupla
d, *e, f = tupla

print(a)
print(b)
print(c)

print(d)
print(e)
print(f)
print(50 * '-')
lista = [1, 2, 3, 4, 5]

a, b, *c, d = lista

print(a)
print(b)
print(c)
print(d)
print(50 * '-')
# Vimos esse mesmo conceito de desempacotamento quando falamos da função enumerate.

# Exemplo
lista = ['c', 'd', 'f', 'g', 'h']

for i, valor in enumerate(lista):
    print(i, valor)
print(50 * '-')
# Quando usamos menos variáveis do que o número de elementos na tupla, lista ou dicionário, podemos utilizar o operador **.

# Exemplo

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def soma(a, b, c, d, e):
  return a + b + c + d + e

print(soma(**dicionario))

