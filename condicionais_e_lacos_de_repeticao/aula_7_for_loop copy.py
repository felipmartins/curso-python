# Aula 7 - For Loop

# Nesta aula vamos abordar os seguintes tópicos:
# Estrutura de um for loop
# Função range
# Quando usar um for loop
# Como podemos aplicar um for loop em variaveis como strings

# Estrutura de um for loop

# O for loop é uma estrutura de repetição que permite executar um bloco de código várias vezes.


for qualquer_coisa in range(10):
    print(f"{qualquer_coisa} - ola")

print(50 * "-")

frase = "Eu gosto de quadrinhos!!"

for l in frase.upper():
    print(l)

print(50 * "-")


for x in frase:
    if x == "o":
        print("Achei mais uma letra 'o'")