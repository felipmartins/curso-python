# Aula 9 - Listas

# Nesta aula vamos abordar os seguintes tópicos:
# Compreensão de listas

# O que são listas
# Listas são coleções de itens em uma ordem específica. Podem conter qualquer tipo de dado, inclusive outras listas.

lista_de_nomes = ['João', 'Maria', 'José', 'Ana']
lista_de_numero = [1]
lista_de_misturado = ['João', 1, 3.14, True]

print(list('felipe'))
print(list(['felipe']))

print(type(lista_de_nomes))

print(50 * '-')
# Como acessar elementos de uma lista

print(lista_de_nomes[0])
print(lista_de_nomes[1])
print(lista_de_nomes[2])
print(lista_de_nomes[3])
print(lista_de_nomes[-1])
# print(lista_de_nomes[10]) # IndexError: list index out of range

print(50 * '-')

lista_de_nomes = ['João', 'Maria', 'José', 'Ana']
lista_de_numero = [1]
lista_de_misturado = ['João', 1, 3.14, True]

print(lista_de_nomes[0:2])
print(lista_de_nomes[1:3])
print(lista_de_nomes[-1::-1])

print(50 * '-')

# Como modificar elementos de uma lista

lista_de_nomes = ['João', 'Maria', 'José', 'Ana']
lista_de_nomes[0] = 'Felipe'
lista_de_nomes[-1] = 'Sofia'

print(lista_de_nomes)

print(50 * '-')

nova_lista = []
nova_lista.append('Felipe')
nova_lista.append('Sofia')
nova_lista.append(7)
nova_lista.append(3.14)
nova_lista.append(True)

print(nova_lista)

nova_lista.insert(1, "MAIS UM ELEMENTO")

print(nova_lista)

nova_lista.pop()
nova_lista.pop(0)
print(nova_lista)

nova_lista.remove(7)

print(nova_lista)

print(50 * '-')

# Como percorrer os elementos de uma lista

lista_aleatoria = list('sihdioashdoiaasdol;ihasdopiasujdpoaksfvpoasjkpo[duasoiduasoisjdoiasjdoipas')

print(lista_aleatoria)

a_count = 0
for letra in lista_aleatoria:
    if letra == 'h':
        print('Hello!!!')
    elif letra == 'j':
        print('Bye bye!!!')
    elif letra == 'a':
        a_count += 1

print(a_count)

print(50 * '-')

# Compreensão de listas

# Compreensão de listas é uma forma de criar listas de forma mais concisa e elegante.

# lista_de_nomes_maiusculos = []

# for nome in lista_de_nomes:
#     lista_de_nomes_maiusculos.append(nome.upper())

lista_de_nomes_maiusculos = [nome.upper() for nome in lista_de_nomes]

print(lista_de_nomes_maiusculos)