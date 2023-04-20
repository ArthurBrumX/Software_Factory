# 12 - Faça um algoritmo que verifique se o número digitado é positivo ou negativo.

print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
print ("*** Positivo Ou Negativo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Descubra Se O Número é Positivo Ou Negativo! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

numero = float(input("* Digite Um Número: "))
    # Nome Da Variável = numero.
    # Tipo Da Variavel = Float (Real).
    # Função = Entrada De Dados.

if (numero >= 0):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("*** Usuário, o Número {} É Um número Positivo!! ***".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)
    

elif (numero < 0):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("*** Usuário, o Numero {} É Um número Negativo!! ***".format(numero))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

print ("=" * 60)