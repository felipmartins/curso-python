# Aula 17 - Args e kwargs

# O que vamos abordar nesta aula:
# 1. O que são
# 2. Como funcionam
# 3. Exemplos

# Args e kwargs são utilizados para receber um número variável de argumentos em funções.

# Args

# Args é uma tupla/lista que armazena os argumentos passados para a função.

# Exemplo

def soma(a, b, *args):
    print(args)
    return sum(args)

print(soma(1, 2, 3, 4, 5))

print(50 * '-')
# Kwargs

# Kwargs é um dicionário que armazena os argumentos passados para a função.

# Exemplo

def soma_2(a, b, **kwargs):
    print(kwargs)
    return sum(kwargs.values())

print(soma_2(a=1, b=2, c=3, d=4, e=5))
print(50 * '-')
# Args e kwargs podem ser utilizados juntos.

# Exemplo

def soma_3(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values())

print(soma_3(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5))
print(50 * '-')

# Args e kwargs tambem podem ser utilizados em funções comuns.

# Exemplo

def soma_4(a, b, *args, **kwargs):

    print(a)
    print(b)
    print(args)
    print(kwargs)

    return a + b + sum(args) + sum(kwargs.values())

print(soma_4(1, 2, 3, 4, 5, f=1, g=2, c=3, d=4, e=5))
print(50 * '-')
# Args e kwargs tambem podem ser utilizados em funções com valores padrão.

# Exemplo

def soma_5(a, b=2, *args, **kwargs):

    print(a)
    print(b)
    print(args)
    print(kwargs)

    return a + b + sum(args) + sum(kwargs.values())

print(soma_5(1, f=1, g=2, c=3, d=4, e=5))
