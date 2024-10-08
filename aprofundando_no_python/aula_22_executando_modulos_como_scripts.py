# Aula 22 - Executando módulos como scripts

# O que vamos abordar nesta aula:
# 1. Como executar módulos como scripts
# 2. Exemplos

# Módulos podem ser executados como scripts. Para isso, basta adicionar o código que você deseja executar no final do módulo e chamar a função principal.

# Exemplo

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def executa_operacao(a, b, operacao):
    return operacao(a, b)

if __name__ == '__main__':
    print(executa_operacao(1, 2, soma))
    print(executa_operacao(1, 2, subtracao))
    print(executa_operacao(1, 2, lambda a, b: a * b))


# Para executar o módulo como script, basta chamar a função principal.

# Exemplo

# python3 aprofundando_no_python/aula_22_executando_modulos_como_scripts.py