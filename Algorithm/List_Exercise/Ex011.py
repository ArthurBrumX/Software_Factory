# 11 - Faça um algoritmo que o usuário possa digitar o seu nome e a sua idade. Utilizando a tabela a baixo, verifique em qual item se enquadra a idade da pessoa e escreva a 
# mensagem:(nome) está com (idade) e pela tabela é considerado um (tipo).


print ("=" * 60)

print ("*** Olá, Seja Bem-Vindo! ***")
print ("*** Tabela De Idade ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Descubra Qual Sua Classifição!! *")
    # Apresentação Ao Usuário.

print ("¨" * 60)

nome = input("* Qual é o seu nome: ")
    # Nome Da Variável = nome.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

idade = int(input("* Qual é sua idade: "))
    # Nome Da Variável = idade.
    # Tipo Da Variavel = Str (String).
    # Função = Entrada De Dados.

if (idade <= 2):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, está com {} e pela tabela é considerado um bebê! ".format(nome, idade))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (idade >= 3) or (idade <= 11):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, está com {} e pela tabela é considerado uma criança! ".format(nome, idade))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (idade >= 12) or (idade <= 21):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, está com {} e pela tabela é considerado um jovem! ".format(nome, idade))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (idade >= 22) or (idade <= 64):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, está com {} e pela tabela é considerado um adulto! ".format(nome, idade))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (idade >= 65) or (idade <= 100):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {}, está com {} e pela tabela é considerado um ! ".format(nome, idade))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

elif (idade >= 101):
    # Elif = Se Não Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    print ("-" * 60)

    print ("- {} esta com {} e pela tabela é considerado uma pessoa muito velhinha".format(nome, idade)) 
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}
            # Ex: .format(Nome_da_Variável)

print ("=" * 60)