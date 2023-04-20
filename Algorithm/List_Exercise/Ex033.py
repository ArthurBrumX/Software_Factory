# 33 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# • par ou ímpar;
# • positivo ou negativo;
# • inteiro ou decimal.

print ("=" * 60)

print ("*** Calculos! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
print ("* Vamos Realizar Alguns Calculos! *")
    # Apresentação Ao Usuário.

print ("=" * 60)

nome = input("* Digite Seu Nome: ")
    # Nome Da Variável = nome.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

n1 = float(input("* Digite Um Número: "))
    # Nome Da Variável = n1.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

n2 = float(input("* Digite Outro Numero: "))
    # Nome Da Variável = n2.
    # Tipo Da Variável = Float (Real).
    # Função = Entrada De Dados.

opcao = input("* Qual Operação voçe Deseja Realizar Usuário: ")
    # Nome Da Variável = opcao.
    # Tipo Da Variável = Str (string).
    # Função = Entrada De Dados.

if (opcao == "Adição") or (opcao == "Adicao") or (opcao == "adição") or (opcao == "adicao"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    soma = n1 + n2
        # Nome Da Variável = soma.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> n1 + (Valor Da Variável: ) -> n2

    par_impar = soma % 2
        # Nome Da Variável = par_impar.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> soma % (Resto Da Divisão Por: ) -> 2

    # =================================================================================================

    print ("=" * 60)

    if (par_impar == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print("- O Numero {} é Par!!".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).


    elif (par_impar == 1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Impar!!".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (soma > 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Positivo !!".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (soma <= -1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        
        print ("- O Número {} é Negativo".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (type(soma) == int):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Decimal!!".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (type(soma) == float):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Inteiro".format(soma))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================
    

elif (opcao == "Subtração") or (opcao == "subtração") or (opcao == "subtracao") or (opcao == "Subtracao"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    subtracao = n1 - n2
        # Nome Da Variável = subtracao.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> n1 - (Valor Da Variável: ) -> n2

    par_impar = subtracao % 2
        # Nome Da Variável = par_impar.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> subtracao % (Resto Da Divisão Por: ) -> 2

    # =================================================================================================

    print ("=" * 60)

    if (par_impar == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print("- O Número {} é Par!!".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (par_impar == 1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Impar!!".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (subtracao > 0):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Positivo!!".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (subtracao <= -1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Negativo".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (type(subtracao) == int):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Decimal!!".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (type(subtracao) == float):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Inteiro".format(subtracao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================


elif (opcao == "Multiplicação") or (opcao == "multiplicação") or (opcao == "Multiplicacao") or (opcao == "multiplicacao"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    multiplicacao = n1 * n2
        # Nome Da Variável = multiplicacao.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> n1 * (Valor Da Variável: ) -> n2

    par_impar = multiplicacao % 2
        # Nome Da Variável = par_impar.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> multiplicacao % (Resto Da Divisão Por: ) -> 2

    # =================================================================================================

    print ("=" * 60)

    if (par_impar == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print("- O Número {} é Par!!".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (par_impar == 1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Impar!!".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (multiplicacao > 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Positivo!!".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).


    elif (multiplicacao <= -1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Negativo".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (type(multiplicacao) == int):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Decimal!!".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (type(multiplicacao) == float):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Inteiro!! ".format(multiplicacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================


elif (opcao == "Divisã0") or (opcao == "divisão") or (opcao == "Divisao") or (opcao == "divisao"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    divisao = n1 / n2
        # Nome Da Variável = divisao.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> n1 / (Valor Da Variável: ) -> n2

    par_impar = divisao % 2
        # Nome Da Variável = par_impar.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> divisao % (Resto Da Divisão Por: ) -> 2

    # =================================================================================================

    print ("=" * 60)

    if (par_impar == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print("- O Número {} é Par!!".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (par_impar == 1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Impar!!".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).
    
    # =================================================================================================

    print ("=" * 60)

    if (divisao > 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Positivo!!".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (divisao <= -1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Negativo".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (type(divisao) == int):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Decimal!!".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (type(divisao) == float):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Inteiro".format(divisao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

elif (opcao == "Exponenciação") or (opcao == "exponenciação") or (opcao == "Exponenciacao") or (opcao == "exponenciacao"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    exponenciacao = n1 ** n2
        # Nome Da Variável = exponenciacao.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> n1 ** (Valor Da Variável: ) -> n2

    par_impar = exponenciacao % 2
        # Nome Da Variável = par_impar.
        # Função = Calculo Com Variáveis
            # Calculo: (Valor Da Variável: ) -> exponencicao % (Resto Da Divisão Por: ) -> 2

    # =================================================================================================

    print ("=" * 60)

    if (par_impar == 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print("- O Número {} é Par!!".format(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (par_impar == 1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Impar!!".fortmat(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (exponenciacao > 0):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Positivo!!".format(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (exponenciacao <= -1):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- O Número {} é Negativo".format(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    # =================================================================================================

    print ("=" * 60)

    if (type(exponenciacao) == int):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Decimal!!".format(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (type(exponenciacao) == float):
        # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
        # Comando: Type() = serve para descobrir o tipo primitivo da variavel

        print ("- O Número {} é Do Tipo Inteiro".format(exponenciacao))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).



    # =================================================================================================



print ("=" * 60)