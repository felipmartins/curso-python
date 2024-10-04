from typing import Any, Union, List, Dict, Tuple

def soma(a: int | float, b: Union[int, float]) -> Union[int, float]:
    return round(a + b, 2)


def return_list_of_numbers() -> List[Any]:
    return [11.1, 2, 3, 4.2, '5']


def return_dict_of_strings() -> Dict[str, int]:
    return {'a': 1, 'b': 2, 'c': 3}

print(soma(1, 2))
print(soma(1.1, 2.2))
print(soma(1.1, 2))
# print(soma('a', 'b'))

# Aula 16 - O que é tipagem e qual sua importância  

# O que vamos abordar nesta aula:
# 1. O que é tipagem

# Tipagem é a forma como uma linguagem de programação trata os tipos de dados.
# Existem várias formas de tipagem, como:

# 2. Tipagem forte e tipagem fraca

# Tipagem forte: a linguagem de programação não permite que um tipo de dado seja convertido em outro tipo de dado automaticamente.
# Tipagem fraca: a linguagem de programação permite que um tipo de dado seja convertido em outro tipo de dado automaticamente.

# 3. Tipagem estática e tipagem dinâmica

# Tipagem estática: a linguagem de programação verifica os tipos de dados em tempo de compilação.
# Tipagem dinâmica: a linguagem de programação verifica os tipos de dados em tempo de execução.

# 4. Tipagem nos parâmetros
# 5. Tipagem nos retornos
