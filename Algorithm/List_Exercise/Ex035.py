# 35 - O HipermercadoTabajara está com uma promoção decarnes que é imperdível.Confira:

                  # Até 5 Kg              Acima de 5 Kg

# File Duplo      R$ 34,90 por Kg         R$ 35,80 por Kg
# Alcatra         R$ 44,90 por Kg         R$ 46,80 por Kg
# Picanha         R$ 66,90 por Kg         R$ 67,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o clientereceberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 

# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print ("=" * 60)

print ("*** Hipermercado Tabajara ***")
    # Boas-Vindas Ao Usuario.

print ("=" * 60)

print ("* Sejá Bem-Vindo! ")
    # Apresentação Ao Usuário.

print ("=" * 60)

tipo_carne = input("* Qual tipo de carne voçê irá querer: ")
    # Nome Da Variável = tipo_carne.
    # Tipo Da Variável = Str (string).
    # Função = Entrada De Dados.

# =====================================================================================================================================

if (tipo_carne == "Filé Duplo") or (tipo_carne == "filé Duplo") or (tipo_carne == "file duplo") or (tipo_carne == "File Duplo"):
    # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    kg = float(input("* Quantos kilos irá querer: "))
        # Nome Da Variável = kg.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    if (kg <= 5):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 34.90
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> kg * 34.90

        cartao = input("* A compra será feita através do cartao da loja [S/N]: ")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 / 100

            print ("- O Valor Final a Ser Pago Será De: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).


        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O Valor Final a Ser Pago é De: R$ {}".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

    # ===========================================================================================

    elif (kg > 5):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 35.80
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> kg * 35.80

        cartao = input("* A compra será feita através do cartao da loja [S/N]")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 /100

            print ("- O valor FInal é de: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).
            
        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O valor Final é De: R${} ".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

# ========================================================================================================================================

elif (tipo_carne == "Alcatra") or (tipo_carne == "alcatra") or (tipo_carne == "ALCATRA"):
    # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    kg = float(input("* Quantos kilos irá querer: "))
        # Nome Da Variável = kg.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    if (kg <= 5):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 44.90
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> kg * 44.90

        cartao = input("* A compra será feita através do cartao da loja [S/N]")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 / 100


            print ("- O valor FInal é de: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O valor Final é De: R${} ".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

    # ===========================================================================================

    elif (kg > 5):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 46.80
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
             # Calculo: (Valor da Variável: ) -> kg * 46*80

        cartao = input("* A compra será feita através do cartao da loja [S/N]")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 / 100

            print ("- O valor FInal é de: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O valor Final é De: R${} ".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

# ========================================================================================================================================

elif (tipo_carne == "Picanha") or (tipo_carne == "picanha") or (tipo_carne == "PICANHA"):
    # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

    kg = float(input("* Quantos kilos irá querer: "))
        # Nome Da Variável = kg.
        # Tipo Da Variável = Float (Real).
        # Função = Entrada De Dados.

    if (kg <= 5):
        # If = Se
        # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 66.90
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> kg * 66.90

        cartao = input("* A compra será feita através do cartao da loja [S/N]: ")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 / 100

            print ("- O valor FInal é de: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O valor Final é De: R${} ".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

    # ===========================================================================================

    elif (kg > 5):
        # Elif = SeNão se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

        peso = kg * 67.80
            # Nome Da Variável = peso.
            # Função = Calculo Com Variáveis
            # Calculo: (Valor da Variável: ) -> kg * 67.80

        cartao = input("* A compra será feita através do cartao da loja [S/N]")
            # Nome Da Variável = cartao.
            # Tipo Da Variável = Str (string).
            # Função = Entrada De Dados.

        if (cartao == "Sim") or (cartao == "sim") or (cartao == "s") or (cartao == "S"):
            # If = Se
            # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            desconto = peso * 5 / 100
                # Nome Da Variável = desconto.
                # Função = Calculo Com Variáveis
                # Calculo: (Valor da Variável: ) -> peso * 5 / 100

            print ("- O valor FInal é de: R${} ".format(desconto))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

        elif (cartao == "Não") or (cartao == "nao") or (cartao == "não") or (cartao == "Nao"):
            # Elif = SeNão se
                # Se Essa Condição for Atendida, Execute o Codigo Abaixo.

            print ("- O valor Final é De: R${} ".format(peso))
                # Função = Saída De Dados.
                # Apresentando Mensagem Na Tela.
                # .format = Formata o Texto, Alocando o Valor De Uma Variável No Espaço: {}.
                    # Ex: .format(Nome_da_Variável).

# ========================================================================================================================================

print ("=" * 60)