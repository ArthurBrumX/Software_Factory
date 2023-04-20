# 46 - Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitaro tempo de casada (anos).

print ("=" * 60)

print ("*** Seja Bem-Vindo! ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

nome = input("* Digite o Seu Nome: ")
    # Nome Da Variável = nome.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

sexo = input("* Digite o Seu Sexo: ")
    # Nome Da Variável = sexo.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

estado_civil = input("* Qual seu estado civil atual: ")
    # Nome Da Variável = estado_civil.
    # Tipo Da Variável = Str (String).
    # Função = Entrada De Dados.

print ("=" * 60)

if (sexo == "F") or (sexo == "f") or (sexo == "Feminino") or (sexo == "feminino"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.


    if (estado_civil == "casada") or (estado_civil == "Casada") or (estado_civil == "CASADA"):
        # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.


        tempo = input("* Quanto tempo de casada voce tem: ")
            # Nome Da Variável = valor_conta.
            # Tipo Da Variável = Float (Real).
            # Função = Entrada De Dados.

        print ("- Voçê se chama {}, é do sexo {} e tem {} anos de casada!".format(nome, sexo, tempo))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

    elif (estado_civil == "Solteira") or (estado_civil == "solteira") or (estado_civil == "solteiro") or (estado_civil == "Solteiro"):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        print ("- Voçê se chama {} e é do sexo {}!".format(nome, sexo))
            # Função = Saída De Dados.
            # Apresentando Mensagem Na Tela.
            # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                # Ex: .format(Nome_da_Variável).

elif (sexo == "M") or (sexo == "m") or (sexo == "Masculino") or (sexo == "masculino"):
    # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.
    
    print ("- Voçê se chama {} e é do sexo {}!".format(nome, sexo))
        # Função = Saída De Dados.
        # Apresentando Mensagem Na Tela.
        # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
            # Ex: .format(Nome_da_Variável).


print ("=" * 60)













