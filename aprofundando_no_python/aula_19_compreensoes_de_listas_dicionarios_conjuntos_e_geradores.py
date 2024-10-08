# Aula 19 - Compreensões de listas, dicionários, conjuntos e geradores

# O que vamos abordar nesta aula:
# 1. O que são compreensões
# 2. Como funcionam
# 3. Exemplos

# Compreensões são uma forma de criar listas, dicionários, conjuntos e geradores de forma mais simples e rápida.

# Exemplo
# Lista

lista = [1, 2, 3, 4, 5]
nova_lista = []
for elem in lista:
    nova_lista.append(elem + 2)

nova_lista_comprehension = [elem + 2 for elem in lista]

print(nova_lista)
print(nova_lista_comprehension)

print(50 * '-')

# Dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
novo_dicionario = {}
for chave, valor in dicionario.items():
    novo_dicionario[2*chave] = valor + 2
    
novo_dicionario_comprenhension = {2*chave : valor + 2 for chave, valor in dicionario.items()}


print(novo_dicionario)
print(novo_dicionario_comprenhension)
print(50 * '-')

# Conjunto

conjunto = {1, 2, 3, 4, 5}
novo_conjunto = set()
for elem in conjunto:
    novo_conjunto.add(elem + 2)

novo_conjunto_comprehension = {elem + 2 for elem in conjunto}

print(novo_conjunto)
print(novo_conjunto_comprehension)
print(50 * '-')

# Gerador

gerador = (elem+2 for elem in range(5))
print(gerador)
print(list(gerador))
