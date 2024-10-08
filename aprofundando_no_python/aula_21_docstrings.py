"""
Este é um arquivo de exemplo para a aula 21.
"""

# Aula 21 - Docstrings

# O que vamos abordar nesta aula:
# 1. O que são docstrings
# 2. Como funcionam
# 3. Exemplos

# Docstrings são strings que são utilizadas para documentar funções, métodos, classes e módulos.

# Exemplo

def soma(a, b):
    """
    Esta função recebe dois números e retorna a soma deles.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
    
    Returns:
        int: A soma dos números.
    """
    return a + b

print(soma(1, 2))

# Módulos e classes também podem ter docstrings.

# Exemplo

class Calculadora:
    """
    Esta classe é uma calculadora que realiza as operações básicas.
    """

    def soma(self, a, b):
        """
        Esta função recebe dois números e retorna a soma deles.

        Args:
            a (int): O primeiro número.
            b (int): O segundo número.
        
        Returns:
            int: A soma dos números.
        """
        return a + b

    def subtracao(self, a, b):
        """
        Esta função recebe dois números e retorna a subtração deles.

        Args:
            a (int): O primeiro número.
            b (int): O segundo número.
        
        Returns:
            int: A subtração dos números.
        """
        return a - b

    def multiplicacao(self, a, b):
        """
        Esta função recebe dois números e retorna a multiplicação deles.

        Args:
            a (int): O primeiro número.
            b (int): O segundo número.
        
        Returns:
            int: A multiplicação dos números.
        """
        return a * b

    def divisao(self, a, b):
        """
        Esta função recebe dois números e retorna a divisão deles.

        Args:
            a (int): O primeiro número.
            b (int): O segundo número.
        
        Returns:
            int: A divisão dos números.
        """
        return a / b


calculadora = Calculadora()

# Existem pacotes que podem ser utilizados para gerar a documentação de um código Python a partir das docstrings.