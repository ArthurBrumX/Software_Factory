# 16 - Faça um Programa que leia três números e mostre o maior e o menor deles.

print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("*** Vamos Descobrir A Hierarquia Dos Numeros!! ***")

print ("-" * 60)

numero_1 = float(input("* Digite Um Número: "))
    # Nome Da Variável = numero_1.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

numero_2 = float(input("* Digite Outro Número: "))
    # Nome Da Variável = numero_2.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

numero_3 = float(input("* Digite Outro Número: "))
    # Nome Da Variável = numero_3.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

print ("=" * 60)

    # Lógica: 

        # n1 > n2 and n2 > n3
        # n1 > n3 and n3 > n2

        # n2 > n1 and n1 > n3
        # n2 > n3 and n3 > n1

        # n3 > n1 and n1 > n2
        # n3 > n2 and n2 > n1


if ( numero_1 > numero_2) and (numero_2 > numero_3):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Número é: {}!".format(numero_1))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_3))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).


elif (numero_1 > numero_3) and (numero_3 > numero_2):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Número é: {}!".format(numero_1))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_2))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (numero_2 > numero_1) and (numero_1 > numero_3):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Número é: {}!".format(numero_2))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_3))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (numero_2 > numero_3) and (numero_3 > numero_1):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Mairo Número é: {}!".format(numero_2))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_1))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (numero_3 > numero_1) and (numero_1 > numero_2):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
    
    print ("- O Maior Número é: {}!".format(numero_3))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_2))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (numero_3 > numero_2) and (numero_2 > numero_1):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("- O Maior Número é: {}!".format(numero_3))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

    print ("- O Menor Número é: {}!".format(numero_1))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)