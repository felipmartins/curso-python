# Aula Extra - Continue e Break

# Nesta aula extra vamos abordar os seguintes tópicos:

# Continue
# Break

print(50 * '-')

# Continue é uma palavra reservada que é utilizada para pular 
# a execução de um loop em uma determinada condição.

# Exemplo:

for i in range(10):
    if i == 5:
        continue
    print(i)
# Neste exemplo, o loop for irá imprimir os números de 0 a 9, 
# exceto o número 5, pois quando i for igual a 5, 
# o continue irá pular a execução do loop.

print(50 * '-')

# Break é uma palavra reservada que é utilizada 
# para sair de um loop em uma determinada condição.

# Exemplo:

for i in range(10):
    if i == 5:
        break
    print(i)
# Neste exemplo, o loop for irá imprimir os números de 0 a 4, 
# pois quando i for igual a 5, o break irá sair do loop.

print(50 * '-')

