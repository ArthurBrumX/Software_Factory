# 15 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M – Masculino ou Sexo Inválido.

print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

nome = input("* Digite Seu Nome Completo: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

sexo = input("* Digite o seu sexo: ")
    # Nome Da Variável = sexo.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

if (sexo == "masculino") or (sexo == "Masculino"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    identificador = "M"
        # Nome Da Variável = identificador.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

    print ("- {}, Conforme Digitado, Voce é do sexo {}!".format(nome, identificador))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (sexo == "feminino") or (sexo == "Feminino"):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    identificador = "F"
        # Nome Da Variável = identificador.
        # Tipo Da Variavel = Str (String).
        # Função = Atribuição De Valor.

    print ("- {}, Conforme Digitado, Voce é do sexo {}!".format(nome, identificador))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

elif (sexo != "masculino") or (sexo != "Masculino") or (sexo != "feminino") or (sexo != "Feminino"):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, Este Sexo É Invalido!".format(nome))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável).

print ("=" * 60)

print ("*** Fim Da Consulta!! ***")

print ("=" * 60)

