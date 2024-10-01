# Aula 12 - Tuplas

# O que vamos abordar nesta aula:

# 1. O que são tuplas

# Tuplas são sequências imutáveis, ou seja, não podem ser alteradas após a sua criação.
# As tuplas são muito parecidas com as listas, mas são imutáveis.

# 2. Criando tuplas

tuple_1 = tuple(['a', 'b', 'c', 'd', 'e'])
tuple_2 = ('a', 'b', 'c', 'd', 'e')
tuple_3 = 'a', 'b', 'c', 'd', 'e'

print(type(tuple_1))
print(type(tuple_2))
print(type(tuple_3))
print(50 * '-')
print(tuple_1)
print(tuple_2)
print(tuple_3)

print(50 * '-')

# 3. Acessando elementos

print(tuple_1[0])
print(tuple_1[-1])

print(tuple_2[1:4])

print(tuple_3[0::2])
print(50 * '-')
# 4. Métodos de tuplas

# count() - Retorna o número de vezes que um valor específico aparece na tupla
# index() - Retorna o índice da primeira ocorrência de um valor específico

print(tuple_1.count('a'))

print(tuple_3.index('e'))
print(tuple_3[4])


# print(tuple_3.index('z')) # ValueError: tuple.index(x): x not in tuple