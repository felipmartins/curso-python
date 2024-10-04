# Aula 14 - Parâmetros de uma função

def funcao_exemplo_6(param1: str, param2: str):
        param1 = param1.upper()
        return f"Este é um exemplo! {param1} - {param2}"

def funcao_exemplo():
        return f"Este é um exemplo!"

def funcao_exemplo_1(param1):
    return f"Este é um exemplo! {param1}"

def funcao_exemplo_2(param1, param2):
    return f"Este é um exemplo! {param1} - {param2}"


if __name__ == "__main__":
    # O que vamos abordar nesta aula:
    # 1. O que são parâmetros
    # 2. Parâmetros obrigatórios

    # Parâmetros são valores que a função recebe para realizar alguma operação.
    # Eles são passados entre parênteses e podem ser de diferentes tipos.

    resultado = funcao_exemplo()
    print(resultado)

    resultado_1 = funcao_exemplo_1("TESTE")
    print(resultado_1)

    resultado_2 = funcao_exemplo_2("TESTE", "TESTE 2")
    print(resultado_2)

    print(50 * "-")

    # 3. Parâmetros opcionais

    def funcao_exemplo_3(param1, param2="valor_2", param3="valor_3"):
        return f"Este é um exemplo! {param1} - {param2} - {param3}"

    resultado_3 = funcao_exemplo_3("TESTE", "MAIS UM TESTE")
    print(resultado_3)

    # 4. Parâmetros posicionais
    # 5. Parâmetros nomeados


    def funcao_exemplo_4(param1, param2="valor_2", param3="valor_3"):
        return f"Este é um exemplo! {param1} - {param2} - {param3}"

    resultado_4 = funcao_exemplo_3("TESTE", param3="MAIS UM TESTE")
    print(resultado_4)

    def pos_only_arg(param1, /):
        print(param1)

    def kwd_only_arg(*, param2):
        print(param2)

    def combined_example(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)

    pos_only_arg("TESTE")
    kwd_only_arg(param2="TESTE")
    combined_example("pos_only", standard="standard", kwd_only="kwd_only")

    # 6. Tipagem nos parâmetros

    def funcao_exemplo_6(param1: str, param2: str):
        param1 = param1.upper()
        return f"Este é um exemplo! {param1} - {param2}"

    resultado_6 = funcao_exemplo_6("ture", "1")
    print(resultado_6)

    # 7. Cuidados com valores padrão

    def funcao_exemplo_7(param1, param2=[], param3="valor_3"):
        param2.append(param1)
        return f"Este é um exemplo! {param1} - {param2} - {param3}"


    resultado_7 = funcao_exemplo_7("TESTE")
    resultado_8 = funcao_exemplo_7("UM NOVO TESTE")
    resultado_9 = funcao_exemplo_7("DEU RUIM")
    print(resultado_7)
    print(resultado_8)
    print(resultado_9)