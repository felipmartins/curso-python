# Aula 20 - Expressões lambda

# O que vamos abordar nesta aula:
# 1. O que são expressões lambda
# 2. Como funcionam
# 3. Exemplos

# Expressões lambda são funções anônimas que podem ter qualquer número de argumentos, mas apenas uma expressão.

# Exemplo

def soma(a, b):
    return a + b
print(soma(1, 21))

outra_soma = lambda a, b: a + b
print(outra_soma(1, 21))


# Exemplo

def quadrado(a):
    return a ** 2
print(quadrado(81))

outro_quadrado = lambda a: a ** 2
print(outro_quadrado(81))

# Expressões lambda podem ser utilizadas em funções como argumentos.

# Exemplo
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def executa_operacao(a, b, operacao):
    return operacao(a, b)

print(executa_operacao(11, 22, soma))
print(executa_operacao(22, 11, subtracao))
print(executa_operacao(11, 22, lambda a, b: a * b))
print(executa_operacao(11, 22, lambda a, b: a / b))
print(executa_operacao(2, 10, lambda a, b: a ** b))




