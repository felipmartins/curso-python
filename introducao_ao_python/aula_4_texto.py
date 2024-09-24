# Aula 4: Texto (Strings)

# Nesta aula vamos abordar os seguintes tópicos:

# Como escrever texto em Python (diferentes formas de representar texto)

a = 'texto dentro de aspas simples'
b = "texto dentro de aspas duplas"
c = '''texto dentro de
poadisopdiaopsi
 aspas triplas'''
d = """texto dentro de
aolisdjoaijsdoiasjd
aspas triplas duplas"""

print(a)
print(b)
print(c)
print(d)


# O que o \ afeta o texto em Python

# \n -> pula uma linha
# \t -> tabula o texto
# \' -> coloca uma aspas simples
# \" -> coloca uma aspas dupla

e = "ola\nmundo"
f = "ola\tmundo"
g = "ola\'mundo"

print(e)
print(f)
print(g)

# Como concatenar strings

h = "ola"
i = "mundo"

j = h + " " + i + "!"

print(j)
print(4*h)

# Como formatar strings

k = f"Este é um teste para formatar: {h} {i} - {h + " " + i + "!"} - {4*h}"

print(k)

# Como descobrir o tamanho de uma string

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# como acessar caracteres individuais ou fatias em uma string

print("esta é a primeira letra do meu a:", a[0])
print("esta é a última letra do meu a:", a[-1])

print("esta é uma fatia do meu a:", a[-1::-1])

# como acessar os "métodos" de uma string

print(a.endswith("duplas"))
print(a.endswith("simples"))

print(a.startswith("texto"))

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.count("te"))