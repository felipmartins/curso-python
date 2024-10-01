# Aula 8 - While Loop

# Nesta aula vamos abordar os seguintes tópicos:
# Estrutura de um while loop
# condição de parada
# cuidados com loops infinitos
# Quando usar um while loop

# Estrutura de um while loop

a = 0

while a < 10:
    print('Loop finito')
    a += 1


ligado = True

while ligado:
    x = input('Digite "sair" para sair do loop while: ')
    if x == 'sair':
        ligado = False
        print('Saiu com sucesso!')
