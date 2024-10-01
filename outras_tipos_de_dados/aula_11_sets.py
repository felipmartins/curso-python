# Aula 11 - Sets (Conjuntos)

# O que vamos abordar nesta aula:

# 1. O que são sets

# Os conjuntos (sets) são coleções não ordenadas de elementos únicos.

# 2. Criando sets

set_1 = {1, 2, 3, 4, 5, 1, 1, 2, 3, 5, 1, 4} # set != dict
set_2 = set([1, 2, 3, 4, 5])
set_3 = set('felipe')

print(set_1)
print(set_2)
print(set_3)

print(50 * '-')

# 3. Adicionando elementos

set_4 = set()

set_4.add('a')
set_4.add('b')
set_4.add('c')
set_4.add('a')
set_4.add('b')
set_4.add('c')

print(set_4)

print(50 * '-')
# 4. Removendo elementos

set_5 = {'d', 'e', 'f', 'g', 'h', 'i', 'j'}

set_5.remove('i')
set_5.discard('j')
set_5.discard('k')
set_5.pop()

print(set_5)

print(50 * '-')

# 5. Operações com sets

# conjunto dos caninos
set_6 = {'cachorro', 'lobo'}

# conjunto dos felinos
set_7 = {'gato', 'leão'}

# conjunto dos mamiferos
set_8 = {'cachorro', 'lobo', 'gato', 'leão'}

print(set_6.union(set_7))
print(set_6.union(set_8))
print(50 * '-')
print(set_6.intersection(set_7))
print(set_6.intersection(set_8))
print(50 * '-')
print(set_6.difference(set_7))
print(set_6.difference(set_8))
print(set_8.difference(set_6))


todos_produtos_da_loja = {'arroz', 'feijão', 'macarrão', 'carne', 'frango', 'peixe', 'leite', 'ovos', 'pão', 'café', 'açúcar', 'sal', 'óleo', 'manteiga', 'queijo', 'presunto', 'mortadela', 'salsicha', 'linguiça', 'iogurte', 'suco', 'refrigerante', 'cerveja', 'vinho', 'whisky', 'vodka', 'tequila', 'rum', 'licor', 'conhaque', 'champagne', 'espumante', 'água', 'energético', 'chá', 'mate', 'leite condensado', 'creme de leite', 'maionese', 'mostarda', 'ketchup'}

produtos_da_loja_hoje = {'arroz', 'feijão', 'macarrão', 'queijo', 'presunto', 'mortadela', 'salsicha', 'linguiça', 'iogurte', 'suco', 'refrigerante', 'cerveja', 'vinho', 'whisky', 'vodka', 'tequila', 'rum', 'licor', 'conhaque', 'champagne', 'espumante', 'água', 'chá', 'mate', 'maionese', 'mostarda', 'ketchup'}

print(todos_produtos_da_loja.difference(produtos_da_loja_hoje))