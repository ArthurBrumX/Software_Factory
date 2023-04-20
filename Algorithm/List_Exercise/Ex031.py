# 31 - Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou"Boa Noite!" ou "Valor Inválido!", conforme o caso.

print ("=" * 60)

print ("*** Boas Vindas!! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)


nome = input("* Digite Seu Nome: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

print ("* [M] -> Matutino")
print ("* [V] -> Vespertino")
print ("* [N] -> Noturno")

print ("=" * 60)

periodo = input("* Em que periodo voce estuda [M/V/N]: ")
    # Nome Da Variável = periodo.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

if (periodo == "M") or (periodo == "m"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("=" * 60)

    print ("*** Bom Dia {}!! ***".format(nome))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (periodo == "V") or (periodo == "v"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("=" * 60)

    print ("*** Boa Tarde {} !! ***".format(nome))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

elif (periodo == "N") or (periodo == "n"):
    # Elif = Senão Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("=" * 60)

    print ("*** Boa Noite {}!! ***".format(nome))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)















