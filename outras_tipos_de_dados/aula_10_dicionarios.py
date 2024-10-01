# Aula 10 - Dicionários

# O que vamos abordar nesta aula:

# Dicionários são coleções de itens em uma ordem específica,
# onde cada item tem um valor associado a uma chave. 

lista = ['a', 'b', 'c']

dicionario = {
    'cidade': 'São Paulo',
    'idade': 25, 
    'nome': 'João', 
    }
print(type(dicionario))
print(50 * '-')

# Acessando elementos de um dicionário atraves de suas chaves

# print(dicionario[0]) # Erro

print(dicionario['cidade'])

print(50 * '-')
# Modificando elementos de um dicionário

print(dicionario)

dicionario['cidade'] = 'Rio de Janeiro'
dicionario['nome'] = 'Maria'
dicionario['idade'] = 30

print(dicionario)

print(50 * '-')

# Adicionando elementos a um dicionário

dicionario['sexo'] = 'Feminino'

dicionario.update({'profissao': 'Engenheira'})

print(dicionario)

print(50 * '-')

# Removendo elementos de um dicionário

print(dicionario)

del dicionario['sexo']
dicionario.pop('profissao')

print(dicionario)

print(50 * '-')

# Como iterar pela chave e valor de um dicionário

for x in dicionario:
    print(x)

for x in dicionario.values():
    print(x)

for x, y in dicionario.items():
    print(x, y)