# 10 - Faça um algoritmo que verifique se o número digitado é menor, maior ou igual a 10 e apresente a mensagem referente ao número.

print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
print ("* Descubra Qual a diferença Do Número * ")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

numero = float(input("* Digite Um Numero: "))
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

if (numero < 10):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- Voçê digitou {}".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

    print ("- numero digitado é MENOR que 10!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (numero > 10):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- Voce digitou {}".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

    print ("- O numero digitado é MAIOR que 10!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

elif (numero == 10):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- Voce digitou {}".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

    print ("- O numero digitado é IGUAL a 10!")
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.

print ("=" * 60)