# Aula 13 - Como definir e usar funções

# O que vamos abordar nesta aula:

# 1. O que são funções

# Funções são blocos de código que são executados quando chamados.
# Elas podem receber dados para processar e podem retornar dados.

# 2. Definindo funções

def verifica_se_o_numero_eh_par(numero: int): # numero = 20
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
        return True
    else:
        print(f'O número {numero} é ímpar.')
        return False

# 3. Chamando funções
verifica_se_o_numero_eh_par(1)
verifica_se_o_numero_eh_par(2)
verifica_se_o_numero_eh_par(1007)
verifica_se_o_numero_eh_par(1008)
verifica_se_o_numero_eh_par(999999999)
verifica_se_o_numero_eh_par(18092739817232)

# 4. Argumentos de funções

# Argumentos são os dados que passamos para a função processar.
# Eles podem ser obrigatórios ou opcionais.


# 5. Retornando valores

valor_1 = verifica_se_o_numero_eh_par(7)
valor_2 = verifica_se_o_numero_eh_par(8)

print(valor_1)
print(valor_2)