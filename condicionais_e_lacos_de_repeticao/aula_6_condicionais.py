# Aula 6: Condicionais em Python

# Nesta aula vamos abordar os seguintes tópicos:

# Operadores de comparação (==, !=, >, <, >=, <=, in, is)

x = 10
y = 20
z = 20

print(x == y) # False
print(z == y) # True

print(x != y) # True
print(z != y) # False

print(x > y) # False
print(z > y) # False

print(x < y) # True
print(z < y) # False

print(x >= y) # False
print(z >= y) # True

print(x <= y) # True
print(z <= y) # True

palavra = "Dentista"

print("D" in palavra) # True
print("d" in palavra) # False

print(x is y) # False
print(z is y) # True

print (50*"-")

# - Negando condições com not

print(not x == y) # True
print(not z == y) # False

print("D" not in palavra) # False
print("d" not in palavra) # True

print (50*"-")

# - Operadores lógicos (and (E) e or (OU))

x = 10
y = 20
z = 20

print(x > y and z == y) # False E True => False
print(x < y and z == y) # True E True => True

print(x > y or z != y) # False OU False => False
print(x > y or z == y) # False OU True => True
print(x < y or z == y) # True OU True => True

print (50*"-")


# Estruturas condicionais (if, elif, else)

if not x > y:
    print("x é menor que y")

if y > x:
    print("y é maior que x")


segunda_string = "Pessoaaaaaa"

if "h" in segunda_string:
    print(f"A letra 'h' está presente em {segunda_string}")
elif "k" in segunda_string:
    print(f"A letra 'k' está presente em {segunda_string}")
elif "a" in segunda_string:
    print(f"A letra 'a' está presente em {segunda_string}")
else:
    print(f"A letra 'h' não está presente em {segunda_string}")

print (50*"-")
# - Match case (Python 3.10)

match segunda_string:
    case "Pessoa Desenvolvedora":
        print("A string é 'Pessoa Desenvolvedora'")
    case "Pessoa":
        print("A string é 'Pessoa'")
    case "Desenvolvedora":
        print("A string é 'Desenvolvedora'")
    case _:
        print("A string não é 'Pessoa Desenvolvedora'")

# - Operador ternário

print("x é maior do que o y") if x > y else print("x é menor do que o y")